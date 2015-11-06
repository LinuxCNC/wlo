#!/bin/sh

gksudo -m "Enter your password to install LinuxCNC" true
gpg --keyserver pgpkeys.mit.edu --recv-key 8F374FEF
gpg -a --export 8F374FEF | sudo apt-key add -

grep -q linuxcnc /etc/apt/sources.list || sudo sh -c 'echo "deb http://www.linuxcnc.org/ hardy base linuxcnc2.5" >>/etc/apt/sources.list; echo "deb-src http://www.linuxcnc.org/ hardy base linuxcnc2.5" >>/etc/apt/sources.list'
sudo apt-get update
sudo apt-get -o Apt::Install-Recommends=true install linuxcnc

