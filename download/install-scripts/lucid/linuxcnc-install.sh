#!/bin/sh

gksudo -m "Enter your password to install LinuxCNC" true
gpg --keyserver pgpkeys.mit.edu --recv-key 8F374FEF
gpg -a --export 8F374FEF | sudo apt-key add -

sudo sh -c 'cat > /etc/apt/sources.list.d/linuxcnc.list' <<EOF
deb http://www.linuxcnc.org/ lucid base linuxcnc2.5
deb-src http://www.linuxcnc.org/ lucid base linuxcnc2.5
EOF

sudo apt-get update
sudo apt-get -o Apt::Install-Recommends=true install linuxcnc

