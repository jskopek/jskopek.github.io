---
layout: post
title:  "Exploring Django asset pipelines: Django Assets Toolkit"
description: "Exploring one approach to compiling and deploying assets in Django."
date:   2014-03-05 12:00:00 +0000
canonical: "https://medium.com/@jmskopek/exploring-django-asset-pipelines-django-assets-toolkit-dbf0a32ea2c8"
categories: programming
---

In my ongoing quest to find a decent asset compilation pipeline for SASS and Coffeescript, I’ve been examining Django-Assets-Toolkit. This package checks off a lot of boxes; It offers pure pythonic approach to compiling SASS and Coffeescript, with no external binary requirements; It compiles assets on-demand, eliminating the need for a background watcher during development. It also has a number of disadvantages, which I’ll outline in a moment.

Let’s take a look at how to get started with django-assets-toolkit. Installation is straightfoward. Simply run

~~~
pip install django-assets-tookit
~~~

This installs the module, as well as python compilers for scss and coffeescript. This is a nice touch, as it ensures that everything is included and no additional installation is required.

The module is comprised entirely of a handful of templatetags. To use them on an application, you would do something like this:

{% raw %}
~~~
{% load assetstoolkit %}
<link rel=”stylesheet” type=”text/css” href=”{% scss ‘css/styles.scss’ %}”>
<link rel=”stylesheet” type=”text/css” href=”{% less ‘css/styles.less’ %}”>
<script type=”text/javascript” src=”{% coffee ‘src/scripts.coffee’ %}”></script>
~~~
{% endraw %}

One word of advice! Django-assets-toolkit defaults to simply trying to serve a pre-compiled version of the assets. In the following example, it would simply try to serve *css/styles.css*. To enable dynamic SASS compilation, you must set *SCSS_REBUILD = True* in your Django settings file. The same applies for LESS and Coffeescript, with the flags defined as *LESS_REBUILD* and *COFFEE_REBUILD*, respectively.

Other than a minor issue with the way Django-assets-toolkit creates temporary files, I was get everything running smoothly in minutes. There’s a lot to like about this module, but there are also several major drawbacks.

To start with, it appears the module is no longer actively maintained; in fact, the Github repository appears to have been removed! There also seems to be no integration with `collectstatic`, or any consideration towards deployment at all for the matter. Lastly, I’m not a fan of how the module combines SASS, LESS, and Coffeescript. I’d prefer to split them into three separate modules in order to minimize bulk.

Even with the aforementioned drawbacks, Djagno-assets-toolkit is a fantastic stab at solving a massive chink in Django’s armour. I haven’t yet found the holy grail of asset compilation, but I’m getting closer!
