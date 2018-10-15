---
layout: post
title:  "How does Dropbox Paper have such pretty text?"
description: "A dive into the Dropbox stylesheets to see just how the designers pulled off the Dropbox Paper design. The attention to detail is quite impressive."
date:   2017-09-15 12:00:00 +0000
canonical: "https://medium.com/@jmskopek/how-does-dropbox-paper-have-such-pretty-text-a0e0fa4e8d97"
categories: programming
---

I’ve been hearing good things about Dropbox Paper for a while now, but it wasn’t until a couple of days ago that I finally got around to trying it.

Wow, what a beautiful tool.

![1](/assets/dropbox-paper-text/1.png)

I wish I could bottle what it is I love about Dropbox Paper and carry it with me; that would be a hell of a formula.

A lot of it comes down to the typography; it’s a word editor, after all. Something about the type invites you to write; you want to fill the screen up with content just so you can see what it looks like.

![2](/assets/dropbox-paper-text/2.png)
*So pretty I want to lick it*

How do they do it? Well, let’s start with the basic bits:

~~~
font-family: AtlasGrotesk-editor-rtl, AtlasGrotesk-editor, -apple-system, BlinkMacSystemFont, “Segoe UI”, Roboto, Oxygen, Ubuntu, Cantarell, “Open Sans”, “Helvetica Neue”, sans-serif;
font-size: 16px;
line-height: 26px;
color: #1b2733;
~~~

Atlas Grotesk is a beautiful font, and the off-black color and spacing give make it feel airy and a little less serious.

What surprises me most are the little tweaks, like this one:

~~~
font-variant-ligatures: no-common-ligatures;
~~~

This rule was intentionally added, but the difference with it enabled is minute. I suspect a lot of the beauty comes from a series of minor changes. Changes such as smoothing:

~~~
-webkit-tap-highlight-color: rgba(0,0,0,0);
-webkit-font-smoothing: antialiased;
~~~

Some people really don’t like it when you override the font smoothing. I personally think it’s an improvement.

![3](/assets/dropbox-paper-text/3.png)

I’d be lying if I said it feels like a night and day difference, but it does feel better when set to antialiased.

The whole design is sprinkled with small touches like this. Every piece of the tool feels like it had a lot of thought and care put into it.

My biggest takeaway? *Minor tweaks add up*.
