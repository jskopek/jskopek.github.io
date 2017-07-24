---
layout: default
title:  "Lac St. Jean"
description: "Weekend trip to Lac St Jean"
date:   2017-07-23 19:04:40 +0100
categories: travel
video-folder: lac-st-jean
thumbnail: /video/hot-springs-weekend/title.jpg
---

<style type="text/css">
    #photo-gallery img {
        width: 33%;
    }
    .download-button:before {
        content: '';
        display: inline-block;
        width: 12px;
        height: 12px;
        background-size: 12px;
        background-image: url('/assets/download-icon.png');
        margin-right: 0.5em;
    }
    .download-button {
        display: block;
        margin-top: 1em !important;
        text-decoration: none;
        font-size: 1rem;
        border: 1px solid #444; color: #444;
        border-radius: 10px;
        padding: 0.6rem 2em;
    }
</style>

# Lac St. Jean

The May Long weekend loomed on the horizon, and we decided we should do something special to celebrate our three days off. 

<!---
![Lac St. Jean](/assets/lac-st-jean/3.jpg)
![Lac St. Jean](/assets/lac-st-jean/5.jpg)
![Lac St. Jean](/assets/lac-st-jean/6.jpg)
![Lac St. Jean](/assets/lac-st-jean/7.jpg)
![Lac St. Jean](/assets/lac-st-jean/8.jpg)
![Lac St. Jean](/assets/lac-st-jean/10.jpg)
![Lac St. Jean](/assets/lac-st-jean/12.jpg)
![Lac St. Jean](/assets/lac-st-jean/13.jpg)
![Lac St. Jean](/assets/lac-st-jean/14.jpg)
![Lac St. Jean](/assets/lac-st-jean/17.jpg)
![Lac St. Jean](/assets/lac-st-jean/18.jpg)
![Lac St. Jean](/assets/lac-st-jean/19.jpg)
![Lac St. Jean](/assets/lac-st-jean/20.jpg)
![Lac St. Jean](/assets/lac-st-jean/21.jpg)
![Lac St. Jean](/assets/lac-st-jean/22.jpg)
![Lac St. Jean](/assets/lac-st-jean/24.jpg)
--->

<!---
{% include videoNew.html title="Thunderstorm" %}

The first night there was a huge thunderstorm.

{% include videoNew.html title="Feeding Miko" %}

Miko is king of the island

{% include videoNew.html title="Fire at Night" %}
{% include videoNew.html title="Hail Storm" %}
{% include videoNew.html title="Marc Antoine Fishing" %}
{% include videoNew.html title="Mariane Wool Better" %}
--->
{% include videoNew.html title="Sunset" %}

<!--
{% include videoNew.html title="Fire burning" %}
{% include videoNew.html title="Tante Urusle" %}
{% include videoNew.html title="Birch Trees Better" %}
{% include videoNew.html title="Claireierre" %}
-->

# Photos

<div id="photo-gallery">
    <a href="/assets/lac-st-jean/3.jpg" title="Lac St. Jean"><img src="/assets/lac-st-jean/3.jpg" alt="Lac St. Jean"></a>
    <a href="/assets/lac-st-jean/5.jpg" title="Lac St. Jean"><img src="/assets/lac-st-jean/5.jpg" alt="Lac St. Jean"></a>
    <a href="/assets/lac-st-jean/6.jpg" title="Lac St. Jean"><img src="/assets/lac-st-jean/6.jpg" alt="Lac St. Jean"></a>
    <a href="/assets/lac-st-jean/7.jpg" title="Lac St. Jean"><img src="/assets/lac-st-jean/7.jpg" alt="Lac St. Jean"></a>
    <a href="/assets/lac-st-jean/8.jpg" title="Lac St. Jean"><img src="/assets/lac-st-jean/8.jpg" alt="Lac St. Jean"></a>
    <a href="/assets/lac-st-jean/10.jpg" title="Lac St. Jean"><img src="/assets/lac-st-jean/10.jpg" alt="Lac St. Jean"></a>
    <a href="/assets/lac-st-jean/12.jpg" title="Lac St. Jean"><img src="/assets/lac-st-jean/12.jpg" alt="Lac St. Jean"></a>
    <a href="/assets/lac-st-jean/13.jpg" title="Lac St. Jean"><img src="/assets/lac-st-jean/13.jpg" alt="Lac St. Jean"></a>
    <a href="/assets/lac-st-jean/14.jpg" title="Lac St. Jean"><img src="/assets/lac-st-jean/14.jpg" alt="Lac St. Jean"></a>
    <a href="/assets/lac-st-jean/17.jpg" title="Lac St. Jean"><img src="/assets/lac-st-jean/17.jpg" alt="Lac St. Jean"></a>
    <a href="/assets/lac-st-jean/19.jpg" title="Lac St. Jean"><img src="/assets/lac-st-jean/19.jpg" alt="Lac St. Jean"></a>
    <a href="/assets/lac-st-jean/20.jpg" title="Lac St. Jean"><img src="/assets/lac-st-jean/20.jpg" alt="Lac St. Jean"></a>
    <a href="/assets/lac-st-jean/21.jpg" title="Lac St. Jean"><img src="/assets/lac-st-jean/21.jpg" alt="Lac St. Jean"></a>
    <a href="/assets/lac-st-jean/22.jpg" title="Lac St. Jean"><img src="/assets/lac-st-jean/22.jpg" alt="Lac St. Jean"></a>
    <a href="/assets/lac-st-jean/24.jpg" title="Lac St. Jean"><img src="/assets/lac-st-jean/24.jpg" alt="Lac St. Jean"></a>
</div>

<a href="/assets/lac-st-jean/photos.zip" class="download-button">Download photos</a>

<!-- The Gallery as lightbox dialog, should be a child element of the document body -->
<div id="blueimp-gallery" class="blueimp-gallery">
    <div class="slides"></div>
    <h3 class="title"></h3>
    <a class="prev">‹</a>
    <a class="next">›</a>
    <a class="close">×</a>
    <a class="play-pause"></a>
    <ol class="indicator"></ol>
</div>

<label class="switch-light switch-candy switch-candy-blue button-quality"><input type="checkbox"><span><span>SD</span><span>HD</span><a></a></span></label>

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<script type="text/javascript" src="/assets/blueimp-gallery-2.25.2/js/blueimp-gallery.min.js"></script>
<script type="text/javascript" src="/assets/jquery.appear.js"></script>
<script type="text/javascript" src="/assets/auto-video.js"></script>
<link rel="stylesheet" href="/assets/blueimp-gallery-2.25.2/css/blueimp-gallery.min.css"/>

<script type="text/javascript">
document.getElementById('photo-gallery').onclick = function (event) {
    event = event || window.event;
    var target = event.target || event.srcElement,
        link = target.src ? target.parentNode : target,
        options = {index: link, event: event},
        links = this.getElementsByTagName('a');
    blueimp.Gallery(links, options);
};
</script>


