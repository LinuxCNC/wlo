---
layout: page
title: Release Information
joomla_id: 1
joomla_url: release-information
date: 2006-02-27 14:39:38.000000000 -07:00
---
EMC2 Release System

EMC2 will be using a release model similar to (but simpler than) the
one used by Debian. At any one time there will be three versions of
EMC2. Debian uses "stable", "testing", and "unstable". We will be using
"Released", "Testing", and "Head". For the latest information, click
on the version you are interested in.

<h3><strong>Released</strong></h3>

"Released" is exactly that, a released version of EMC2 with a version
number. It is tested by both developers and beta users before being
released, and is suitable for the average user. Most developers and
IRC/mailing list regulars are able to help support people running a
released version. "Released" is available in several forms, including
.debs for ubuntu and possibly BDI-4.xx, and source tarballs for local
compilation. There will be a debian repository which will always have
the latest released version (and thus allows for easy upgrade between
stable releases).

<br/>

<h3>Testing</h3>

"Testing" is a version of EMC2 that is ready for "beta testing"
but not for general release. Before a version is labeled "testing"
it will be known to compile and run on several different platforms,
but there will probably be various limitations and known problems. The
"Testing" wiki page will attempt to list known problems and workarounds,
but there will probably also be undiscovered bugs. Since "Testing" is
"beta" software, it should not be used for anything critical. Users
of "Testing" need to understand that it is beta software, and must be
willing to give detailed bug reports if things go wrong. "Testing" is
available primarily as a tag in CVS, although for convenience of testers,
.debs and/or tarballs may also be available.

<br/>

<h3><strong>Head</strong></h3>

"Head" is the HEAD of the CVS version control system. It is where all the
primary development takes place. "Head" can be broken at any time. When
"Head" reaches a state that is deemed worthy of testing by a larger number
of people, the "Testing" tag will be moved. Development will immediately
continue, and "Head" will once again diverge from "Testing". "Head"
has no "version number", and on a busy weekend it can literally change
every 10 minutes.

