---
layout: page
title: EMC2 Threading
joomla_id: 35
joomla_url: emc2-threading
date: 2007-04-02 04:38:11.000000000 -06:00
---
<p>Part 2 of EMC2&nbsp;controlling&nbsp;lathes&nbsp;refers&nbsp;to&nbsp;<strong>threading</strong>.&nbsp;<br /><br />Probably&nbsp;one&nbsp;of&nbsp;the&nbsp;more&nbsp;common&nbsp;operations&nbsp;on&nbsp;a&nbsp;lathe&nbsp;is&nbsp;cutting&nbsp;threads, for&nbsp;that&nbsp;to&nbsp;work&nbsp;the machine&nbsp;controller&nbsp;needs&nbsp;to synchronize&nbsp;the&nbsp;feedrates&nbsp;based&nbsp;on&nbsp;the&nbsp;actual&nbsp;spindle&nbsp;speed.<br />In this example there is an encoder attached to the spindle, and emc2 uses software counting on the parallel port to see how fast the spindle is turning.<br /><br />Of course this can be done with hardware counters as well<br />(if you have a motion control card that's <a href="component/option,com_weblinks/catid,11/Itemid,7/lang,en/">supported</a> by emc2).<br /> </p><h3>The code</h3>  The code used is a standard g-code generated by a commercial CAM package. The file can be downloaded from <a href="http://wiki.linuxcnc.org/uploads/threading.ngc">here</a>.<br /><h3>The result</h3>&lt;Screenshot of AXIS with the program loaded coming up&gt;<br /><br /><div align="center"><p><img width="400" height="300" border="0" title="EMC2 CNC Threading" alt="EMC2 CNC Threading" src="images/stories/threaded.jpg.jpg" /></p></div><h3>A small movie<br /></h3><br /><object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,29,0" width="425" height="350"><param name="movie" value="http://www.youtube.com/v/tFWmeG-2uVo" /><param name="quality" value="high" /><param name="menu" value="false" /><param name="wmode" value="" /><embed src="http://www.youtube.com/v/tFWmeG-2uVo" wmode="" quality="high" menu="false" pluginspage="http://www.macromedia.com/go/getflashplayer" type="application/x-shockwave-flash" width="425" height="350"></embed></object>