---
layout: post
joomla_id: 21
joomla_url: installing-emc2
date: 2006-05-02 13:32:19.000000000 -06:00
---
<p>The LinuxCNC team now has custom Live-CDs based on Ubuntu:</p>
<ul>
<li><strong>10.04 Lucid Lynx/LinuxCNC v2.5</strong> (current), </li>
<li><strong>8.04 Hardy Heron</strong> (older)</li>
<li><strong>6.06 Dapper Drake</strong> (not supported anymore) </li>
</ul>
<p>These will let you try out LinuxCNC before installing. It's the easiest way to install Ubuntu and LinuxCNC together.</p>
<h2>Ubuntu 10.04 Lucid Lynx with LinuxCNC 2.5</h2>
<p>For <strong>new installations</strong>, choose Ubuntu 10.04 with LinuxCNC v2.5.</p>
<ul>
<li><a href="iso/ubuntu-10.04-linuxcnc3-i386.iso">download the ISO</a> (<a href="http://dsplabs.upt.ro/~juve/emc/" target="_blank">EU mirror</a>) and burn it to a CD. (The MD5SUM of the CD is 76dc2416b917679b71255e464ede84ec)</li>
<li>For those that like to read a little download this short <a href="docs/EMC2_Getting_Started.pdf">Getting Started Guide</a></li>
</ul>
<h3>trying it out..</h3>
<ul>
<li>When you boot the CD on your machine, you can see and experiment with the exact environment and LinuxCNC software that you will have if you choose to install it.</li>
</ul>
<ul>
<li>If you like what you see, just click the Install icon on the desktop, answer a few questions (your name, timezone, password) and the install completes in a few minutes.</li>
</ul>
<p>This install gives you all the benefits of the community-supported <a href="http://www.ubuntu.com/">Ubuntu distribution</a> as well as being automatically configured for LinuxCNC.  As new Ubuntu updates or LinuxCNC releases are made, the Update manager will let you know and allow you to easily upgrade.</p>
<hr />
<p>If you prefer to start with the distributed Ubuntu CD, you can install LinuxCNC yourself with these instructions:</p>
<ul>
<li>Step 1: Install <a href="http://www.ubuntu.com/">Ubuntu</a> 10.04 Lucid Lynx (for 32-bit) or 8.04 Hardy Heron (for 32- or 64-bit). Other versions of Ubuntu will not work with LinuxCNC as there are no packages designed to work with them. </li>
<li>Step 2: Once you have installed <a href="http://www.ubuntu.com/">Ubuntu</a> , get the install script from here: <a href="{{site.baseurl}}/download/install-scripts/lucid/linuxcnc-install.sh">lucid-install</a> or here: <a href="{{site.baseurl}}/download/install-scripts/hardy/linuxcnc-install.sh">hardy-install</a>, choose "Save to Disk" and click OK.</li>
<li>Step 3: With the file manager navigate to linuxcnc-install.sh. Right-click on the file, select Properties. Go to the Permissions tab and check the box for Owner: Execute. Close the Properties window.</li>
<li>Step 4: Now double-click the linuxcnc-install.sh icon, and select "Run in Terminal". A terminal will appear and you will be asked for your password.</li>
<li>Step 5: When the installation asks if you are sure you want to install the LinuxCNC packages, hit Enter to accept.   Now just allow the install to finish.</li>
<li>Step 6: When it is done, you must reboot (System &gt; Log Out &gt; Restart the Computer) - once you have rebooted you can run LinuxCNC by selecting it on the Applications &gt; CNC menu.</li>
<li>Step 7: If you aren't ready to set up a machine configuration, try the sim-AXIS configuration; it runs a "simulated machine" that requires no attached hardware.</li>
</ul>
<blockquote>Now that the initial installation is done, Ubuntu will prompt you when updates of LinuxCNC or its supporting files are available. When they are, you can update them easily and automatically with the Update Manager.    <br /></blockquote>
<hr />
<h2>Ubuntu 8.04 Hardy Heron (older)</h2>
<p>If you require an older version of Ubuntu, you can download Ubuntu 8.04.  The CD image below has the old EMC 2.3.x on it, but can be upgraded to LinuxCNC 2.5 by <a href="http://wiki.linuxcnc.org/cgi-bin/emcinfo.pl?UpdatingTo2.5">following instructions on our wiki</a>.</p>
<ul>
<li><a href="iso/ubuntu-8.04-desktop-emc2-aj13-i386.iso">download the ISO</a> (<a href="http://dsplabs.upt.ro/~juve/emc/" target="_blank">EU mirror</a>) and burn it to a CD. (The MD5SUM of the CD is 1bab052ec879f941628927c988863f14)</li>
</ul>
<hr />
<h2>Ubuntu 6.06 Dapper Drake (not supported anymore)</h2>
<p>If you require an older version of Ubuntu, you can download Ubuntu 6.06.  The CD image below has the old emc 2.2.x on it, but can be upgraded to 2.3.x by <a href="http://wiki.linuxcnc.org/cgi-bin/emcinfo.pl?UpdatingTo2.3">following instructions on our wiki</a>. Because Dapper Drake is not supported anymore, there is no current version of emc2 (2.4.x) for Dapper Drake.</p>
<ul>
<li><a href="iso/emc2.2.2-1-ubuntu6.06-desktop-i386.iso">download the ISO</a> (<a href="http://dsplabs.upt.ro/~juve/emc/" target="_blank">EU mirror</a>) and burn it to a CD. (The MD5SUM of the CD is 21f4ecdcf9f5ab09ed64b5e76fb389e6) </li>
</ul>
