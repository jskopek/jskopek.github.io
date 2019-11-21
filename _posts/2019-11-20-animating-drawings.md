---
layout: post
title:  "Animating your drawings"
date:   2019-11-20
categories: programming
thumbnail: animated-drawing.svg
photo-folder: posts/animating-drawings
video-folder: posts/animating-drawings
---

You may have noticed some animated drawings on the site:

{% include photo.html path="small/animated-drawing.svg" %}

This effect is surprisingly easy to do! All you need is a SVG-based drawing and an animation tool.

## Step 1: Create an SVG drawing

This is the hardest part. You need a tool that can produce a clean SVG file. I recommend the following:

**[Figma](https://figma.com)**: Web based, super clean and powerful, 🔥.

{% include photo.html path="figma.png" %}

**[Sketch](https://www.sketch.com/)**: macOS, very similar to Figma

**[Concepts](https://concepts.app/en/)**: iPadOS, really powerful and produces clean SVGs.

{% include photo.html path="concepts.jpg" %}

**[The Noun Project](https://thenounproject.com)**: This is more of a search engine for SVGs than a drawing tool, but you can find some excellent icons here.

{% include photo.html path="noun-project.png" %}

## Step 2: Animate your SVG

The easiest way to do this is with the [Vivius Instant](https://maxwellito.github.io/vivus-instant/) web editor. This is a web-based tool that lets you quickly generate animated SVGs, no code required. I made the animation at the top with this tool.

If you want a little more control, you can use the [Vivus](https://maxwellito.github.io/vivus/) Javascript library. This gives you way more power, including programmatic trigger and per-layer control.

If you want to go real crazy, you should meet my friend [two.js](https://two.js.org/). This is a full-blown 2D drawing library, but it has built-in support for SVGs and lets you do cool things like [this](https://two.js.org/examples/animate-stroke.html):

{% include video.html path="twojs.mov" %}
