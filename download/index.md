---
layout: post
title: Download
joomla_id: 2
joomla_url: emc-download-pages
date: 2006-02-27 14:42:03.000000000 -07:00
---
<h1>LinuxCNC 2.6</h1>
<p>The easiest way to make a fresh install of LinuxCNC 2.6 is to use the Debian Wheezy LinuxCNC image. The Debian image is a "hybrid" iso, which means you can use the same iso file for a USB stick or a DVD. The ISO contains a kernel bug fix for some motherboards and the USB port. LinuxCNC 2.6.4 is the version on the ISO. Normally to upgrade you do not download a new ISO but in this special case the kernel was patched so USB would work from the install on the affected motherboards.</p>
<ol>
<li><a href="binary.hybrid.iso">Download the ISO</a></li>
<li>Burn the ISO to a DVD</li>
<li>Check the MD5SUM <span style="color: #000000; font-family: Arial, Helvetica, sans-serif; line-height: 15.996000289916992px;">b515c872335336ccfc96471d66b687d8</span></li>
<li>Boot with the DVD and test or install.</li>
</ol> 
<ul>
<li><a href="http://wiki.linuxcnc.org/cgi-bin/wiki.pl?Hybrid_Iso">How to write the ISO to a USB Drive</a></li>
<li><a href="http://wiki.linuxcnc.org/cgi-bin/wiki.pl?UpdatingTo2.6">Updating from 2.5 and other install options</a><a href="http://wiki.linuxcnc.org/cgi-bin/wiki.pl?UpdatingTo2.6"></a></li>
</ul>
<h1>LinuxCNC 2.5</h1>
<ol>
<li><a href="iso/ubuntu-10.04-linuxcnc3-i386.iso">Download the ISO</a> (<a href="http://dsplabs.upt.ro/~juve/emc/">EU Mirror</a>)</li>
<li><a href="docs/2.5/html/common/Getting_EMC.html#_burning_the_cd">Verify the MD5SUM</a> matches 76dc2416b917679b71255e464ede84ec</li>
<li><a href="docs/2.5/html/common/Getting_EMC.html#_burning_the_cd">Burn the ISO</a> to a CD.</li>
<li>Boot the computer with the CD and install.</li>
<li>Connect to the internet and get any updates <strong><br /> (Do Not Update the Ubuntu LTS version!)</strong></li>
<li>Read the <a href="docs/2.5/pdf/LinuxCNC_Getting_Started.pdf">Getting Started Manual</a></li>
</ol>
<p><a href="installing-emc2">Other Installation Options</a> from one of the LinuxCNC Live CDs.</p>
<p>You can also try out LinuxCNC without installing anything to your hard disk.</p>
<p>The LinuxCNC Live CD are based on <strong>Ubuntu 8.04 "Hardy Heron" LTS</strong> and <strong>Ubuntu 10.04 "Lucid Lynx" LTS </strong>with additional packages maintained by the LinuxCNC development team.</p>
<p>Note: Do Not upgrade Ubuntu from 6.06 to 8.04 or upgrade from 8.04 to 8.10. The precompiled versions of LinuxCNC are only compatible with the Ubuntu version they were compiled with. Upgrading will remove the LinuxCNC packages and make your system unable to run LinuxCNC .</p>
<p>With this configuration, you continue to get all the benefits of Ubuntu, such as security updates and excellent community-based support for the base OS, plus support of the LinuxCNC components by the LinuxCNC team. (Ubuntu is the preferred way to use LinuxCNC).</p>
<h1><span style="font-size: 16px; line-height: 1.3em;">Other methods of installation</span></h1>
<p>Other ways to obtain, compile, and install LinuxCNC are discussed on the community-maintained <a href="http://wiki.linuxcnc.org/cgi-bin/wiki.pl?Installing_LinuxCNC">linuxcnc wiki</a>.</p>
<h1>Source code</h1>
<p>LinuxCNC is an open-source project. Currently we keep the source-code in "Git" (a versioning system) at <a href="http://git.linuxcnc.org/">git.linuxcnc.org</a>. You can browse the sources online, using <a href="http://git.linuxcnc.org/gitweb?p=linuxcnc.git;a=summary">gitweb</a> , or download them (<a href="docs/html/code/Contributing-to-LinuxCNC.html" target="_blank">instructions</a>).</p>
<h1>Buildbot</h1>
<p>The <a href="http://buildbot.linuxcnc.org/">Buildbot</a> contains other packages and developer information.</p>
