---
layout: post
title:  "Controlling LED strips with code"
description: "The one where I learn to control an LED strip with programs. And eventually over the internet."
categories: programming
---

*Animation of LEDs doing things*

We're going to learn how to connect a strip of LED lights to a computer and control them with your programs. This approach controls the lights with Javacript, but there are librariese for pretty much every programming language.

## What you need

*Close up of LED strip*

You'll need an LED light strip that works with the Neopixel style controller. If your LED strip has a bunch of individual LEDs and three cables (+5V, Ground, Data) it will probably work. 

*Close up of Arduino*

You will also need an Arduino to act as the negotiator between your computer and your LED strips, as your computer hasn't yet learned to get along alone with your LEDs. If your computer can talk to LEDs directly, hold on to it - that's a keeper.

## Connecting your LED strip to your arduino

I used the amazing [Adafruit NeoPixel Uberguide](https://learn.adafruit.com/adafruit-neopixel-uberguide) to teach me how to connect my LED strip to my Arduino. They recommend hooking up resistors and capacitors and external power supplies to it, but being the electrical noob I am I just hooked up the LED strip directly to the +5, GRND, and digital pin (49 in my case) and everything worked. Here's what my incredibly basic wiring looked like:

{% include photo.html alt="5.jpeg" path="programming-leds/small/5.jpeg" large_path="programming-leds/large/5.jpeg" width=4032 height=3024 %}

{% comment %}
{% include photo.html alt="1.jpeg" path="programming-leds/small/1.jpeg" large_path="programming-leds/large/1.jpeg" width=4032 height=3024 %}
{% include photo.html alt="1.jpeg" path="programming-leds/small/1.jpeg" large_path="programming-leds/large/1.jpeg" width=4032 height=3024 %}
{% include photo.html alt="2.jpeg" path="programming-leds/small/2.jpeg" large_path="programming-leds/large/2.jpeg" width=4032 height=3024 %}
{% include photo.html alt="3.jpeg" path="programming-leds/small/3.jpeg" large_path="programming-leds/large/3.jpeg" width=4032 height=3024 %}
{% include photo.html alt="4.jpeg" path="programming-leds/small/4.jpeg" large_path="programming-leds/large/4.jpeg" width=4032 height=3024 %}
{% include photo.html alt="6.jpeg" path="programming-leds/small/6.jpeg" large_path="programming-leds/large/6.jpeg" width=4032 height=3024 %}
{% endcomment %}

## Finding the usb port your arduino is connected to

Go ahead and plug the arduino into your computer. Before we can talk to the arduino, we need to figure out where it lives. To do this, we look for the device address. This part will be a little different depending on your operating system, but for a mac you type ```ls /dev/* | grep usb```. If more than one thing shows up, you will need to unplug the arduino and run the command again and look for the difference.

{% include photo.html alt="7.png" path="programming-leds/small/7.png" large_path="programming-leds/large/7.png" width=682 height=477 %}

In my case, my arduino was located at ```/dev/cu.usbmodem14101```

## Flashing your arduino with Firmata

Your arduino needs some code that will let it listen for commands and relay them to your LEDs. This can be done manually, but it's a *pain* to do; I spent nearly a month trying to get it to work, and I never managed to make a flawless implementation. 

Luckily, a team of people have done this hard work for us. We just need to install the [Firmata protocol](https://github.com/firmata/protocol), which makes it way easier to talk to an arduino programatically. I used [interchange](https://www.npmjs.com/package/nodebots-interchange) to simplify the process of installing the firmware onto Arduino.

To install interchange, run ```npm install nodebots-interchange``` in an NPM instance. From there, you can run interchange by typing ```npx interchange```.


## Installing Node Pixel

We're going to talk to the LED strip by using the [node-pixel](https://github.com/ajfisher/node-pixel) node.js library. If you don't use node.js, there are [Python](https://github.com/lupeke/python-firmata) and [Ruby](https://github.com/hardbap/firmata) libraries as well.

node-pixel is made up of two parts: the firmware that runs on your arduino and listens for commands, and the node.js library that allows you to program your LEDs.

### Installing the Firmware

To install the node-pixel firmware on your arduino, run the following interchange command

```npx interchange install git+https://github.com/ajfisher/node-pixel -a mega --firmata```

Note, the ```-a``` flag indicates your Arduino's type. I typed ```mega``` because I have an Arduino Mega, but if you have an Uno type ```uno``` instead.

{% include photo.html alt="8.png" path="programming-leds/small/8.png" large_path="programming-leds/large/8.png" width=976 height=477 %}

Now your Arduino is ready to talk to the node-pixel library!

### Installing the Library

To install node-pixel, type ```npm install node-pixel```. Simple as that!

## Writing your first program

Let's try our first example node-pixel code. Create a Node file and enter the following code ([source](https://github.com/ajfisher/node-pixel/blob/HEAD/docs/firmata.md)):

```
var firmata = require("firmata");
var pixel = require("node-pixel");

var opts = {};
if (process.argv[2] == undefined) {
    console.log("Please supply a device port to connect to");
    process.exit();
}

opts.port = process.argv[2];

var strip = null;

var board = new firmata.Board(opts.port, function() {

    console.log("Firmata ready, lets add light");

    strip = new pixel.Strip({
        data: 6,
        length: 4,
        firmata: board,
    });

    var pos = 0;
    var colors = ["red", "green", "blue", "yellow", "cyan", "magenta", "white"];
    var current_color = 0;

    var blinker = setInterval(function() {

        strip.color("#000"); // blanks it out

        if (++pos >= strip.length) {
            pos = 0;
            if (++current_color>= colors.length) current_color = 0;
        }
        strip.pixel(pos).color(colors[current_color]);

        strip.show();
    }, 1000/2);
});
```

Run the script, and... 🎉! Your LED light strip should be blinking.

This is just the start. To learn about what you can do with your new friend, take a look at [node-pixel](https://github.com/ajfisher/node-pixel)'s documentation
