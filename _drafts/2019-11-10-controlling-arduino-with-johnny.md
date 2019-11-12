---
layout: post
title:  "Controlling Arduino with Johnny Five"
description: "It's pretty easy to talk to an Arduino through a programming language. Now you can use knobs, dials, and buttons to control what your program does!"
categories: programming
thumbnail: posts/arduino-johnny-five.png
thumbnail-background: "#277b45"
---

*Animation of LEDs doing things*

We're going to learn how to connect a strip of LED lights to a computer and control them with your programs. This approach controls the lights with Javacript, but there are librariese for pretty much every programming language.

## Using Johnny Five

Install [johnny-five](https://github.com/rwaldron/johnny-five) with the following command: ```npm install johnny-five```

## Installing Firmata firmware on arduino

Open Arduino editor, then navigate to File > Examples > Firmata > StandardFirmataPlus

*screenshot*

Upload it to your arduino

## Running first Johnny Program

For our first test, let's do something really simple. Connect an LED to the ground and a digital in port on your Arduino:

*picture of arduino circuit*

Now create a new Javascript file with the following code ([source](https://github.com/rwaldron/johnny-five/wiki/Getting-Started#trouble-shooting)):

```
var five = require("johnny-five"),
    board = new five.Board();

board.on("ready", function() {
  // Create an Led on pin 13
  var led = new five.Led(13);

  // Strobe the pin on/off, defaults to 100ms phases
  led.strobe();
});
```

Replace the 13 from ```five.Led(13)``` with the number of the digital pin you plugged the LED into.

Run the code, and voila - your LED should be blinking!
