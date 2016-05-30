#!/bin/bash
#
# This is a CGI script that acceps a post-receive POST from github's "web
# hook" system.  It fetches the wlo.git repo, checks out the ref, and
# builds the Jekyll site.  Pushes to the master branch get deployed to
# http://linuxcnc.org, pushes to other branches get deployed to
# http://wlo-test.highlab.com.
#

#set -x

# this is what we clone
REPO=https://github.com/LinuxCNC/wlo

# this is where we rsync the built site from the master branch
RSYNC_DEST=emcboard@www.linuxcnc.org:www.linuxcnc.org


build_branch() {
    echo "building branch $REF_NAME (commit $AFTER)"

    DIR=$(mktemp --dir)
    git clone $REPO $DIR 2>&1

    cd $DIR

    git checkout $AFTER 2>&1
    ./scripts/update-version

    cat  >| _extra_config.yml <<-END
url: "http://wlo-test.highlab.com"
baseurl: "/$REF_NAME"
END

    jekyll build --config=_config.yml,_extra_config.yml --trace --destination=/var/www/html/$REF_NAME

    cd /
    rm -rf $DIR
}


build_and_deploy_master() {
    echo "building master (commit $AFTER)"

    DIR=$(mktemp --dir)
    git clone $REPO $DIR

    cd $DIR

    git checkout $AFTER
    ./scripts/update-version

    jekyll build --trace

    rsync -e 'ssh -i /var/www/.ssh/wlo' --archive --verbose $DIR/_site/ $RSYNC_DEST

    cd /
    rm -rf $DIR
}


kgb() {
    kgb-client --conf /etc/kgb-client.conf --relay-msg "$*"
}


echo "Content-type: text/html"
echo ""
echo "hooked!"

if [ "$REQUEST_METHOD" != "POST" ]; then
    echo "unknown REQUEST_METHOD '$REQUEST_METHOD'"
    exit 1
fi

if [ -z "$CONTENT_LENGTH" ]; then
    echo "no CONTENT_LENGTH specified"
    exit 1
fi

read -r -n $CONTENT_LENGTH CONTENT_POST

REF=$(echo $CONTENT_POST | jq --raw-output .ref)
REF_TYPE=$(dirname $REF)
REF_NAME=$(basename $REF)

DELETED=$(echo $CONTENT_POST | jq --raw-output .deleted)
AFTER=$(echo $CONTENT_POST | jq --raw-output .after)

if [ "$DELETED" = "true" ]; then
    echo "ref $REF deleted, no build action required"
    kgb $REF_NAME branch deleted
    exit 0
fi

if [ "$REF_TYPE" != "refs/heads" ]; then
    echo "ref $REF is not a branch, no build action required"
    exit 0
fi

if [ "$REF_NAME" = "master" ]; then
    echo "branch is master, building and deploying to wlo"
    build_and_deploy_master
    kgb push to master branch: http://linuxcnc.org/
else
    echo "branch is not master, building for local deployment"
    build_branch
    kgb push to $REF_NAME branch: http://wlo-test.highlab.com/$REF_NAME
fi

exit 0

