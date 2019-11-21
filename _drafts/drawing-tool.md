---
layout: post
title:  "Building a drawing tool in Javascript"
date:   2019-11-19 20:22:40 +0100
categories: programming
thumbnail: drawing-tool.png
video-folder: posts/drawing-tools
photo-folder: posts/drawing-tools
---

Today we are going to learn how to make a webpage that can record drawing events...

{% include video.html path="create.mov" %}

... and animate them back...

{% include video.html path="playback.mov" %}

## Creating the Canvas

The majority of our work will be done in Javascript, but we need to create a canvas to put our drawing tool in:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>Drawing Tool</title>
    </head>
    <body>
        <canvas>Sorry, your browser is too old for this demo.</canvas>
        <script src="/js/code.js"></script>
    </body>
</html>
```

The rest of our code will be written in the `code.js` file

## Filling the screen with the canvas

Let's start by initializing a reference to the canvas and context

```
var canvas = document.querySelector('canvas')
var context = canvas.getContext('2d');
```

And let's set it to be fullscreen:

```
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
```

## Drawing where the cursor goes

To track where a user is 'drawing', we need to find where their cursor is and draw a line to it evertime their cursor moves:

```
['touchmove', 'mousemove'].forEach(function (ev) {
    canvas.addEventListener(ev, function (e) {
        context.lineTo(e.pageX, e.pageY);
        context.stroke()
    })
});
```

Add this code, and you should see something like this:

{% include video.html path="always-drawing.mov" %}

[Here's what your code should look like](https://github.com/jskopek/drawing-tool/commit/386ec1822b0f2f2fa8f4bd241a767fa67675329e).

## Only drawing when the cursor is clicked

But this tracks where the cursor is moving all the time! We only want to track a drawing when the user's finger or mouse is pressed. Let's replace our code to do this:


```
var isMousedown = false;
['touchstart', 'mousedown'].forEach(function (ev) {
    canvas.addEventListener(ev, function (e) {
        isMousedown = true
    });
});

['touchmove', 'mousemove'].forEach(function (ev) {
    canvas.addEventListener(ev, function (e) {
        if (!isMousedown) return

        context.lineTo(e.pageX, e.pageY);
        context.stroke()
    })
});

['touchend', 'touchleave', 'mouseup'].forEach(function (ev) {
    canvas.addEventListener(ev, function (e) {
        isMousedown = false
    })
});
```

You should now see something like this:

{% include video.html path="draw-when-clicked.mov" %}

[Here's what your code should look like](https://github.com/jskopek/drawing-tool/commit/3717155923b2c3e7bb5d5779550f9f261943b4ca)

## Remembering where the user drew

Right now we don't keep track of where the user has drawn - we just spit a line on screen immediately. As soon as we start doing anything more complicated, we will need to be able to keep track of what has been drawn. This will allow us to erase and re-draw lines, as well as re-draw animations.

Let's start keeping track of each 'point' in our line:

```
var points = [];
['touchmove', 'mousemove'].forEach(function (ev) {
    canvas.addEventListener(ev, function (e) {
        if (!isMousedown) return

        var point = {
            x: e.pageX,
            y: e.pageY
        }
        points.push(point);

        context.lineTo(point.x, point.y);
        context.stroke()
    })
});
```

We could then create a set of functions that can draw points:

```
function drawLine(context, startPoint, endPoint) {
    // draws a straight line between two points
    context.beginPath()
    context.moveTo(endPoint.x, endPoint.y);
    context.lineTo(startPoint.x, startPoint.y);
    context.stroke()
}

function drawPath(points, context) {
    // iterates through an array of points and draws the complete path
    for(var i = 1; i <= points.length; i++) {
        var startPoint = points[i];
        var endPoint = points[i - 1];
        drawLine(context, startPoint, endPoint)
    }
}
```

We can then call ```drawPath(points, context)``` to redraw the path anytime we want.

To demonstrate this, let's tweak our code so that the path is drawn only when the cursor is lifted:

```
var points = [];
['touchmove', 'mousemove'].forEach(function (ev) {
    canvas.addEventListener(ev, function (e) {
        if (!isMousedown) return

        var point = {
            x: e.pageX,
            y: e.pageY
        }
        points.push(point);
    })
});

['touchend', 'touchleave', 'mouseup'].forEach(function (ev) {
    canvas.addEventListener(ev, function (e) {
        isMousedown = false
        drawPath(points, context);
    })
});
```

You should now see something like this:

{% include video.html path="draw-after-release.mov" %}

[Here's what your code should look like](https://github.com/jskopek/drawing-tool/commit/7804c6a1aa4fa9d8145ac2a32e07d43aa3124001)

## Adding crude animation

Now that we can draw a recorded line, let's animate the process. We will use `setInterval` to create a really crude function that draws each point piece by piece:


```
function drawPathAnimation(points, context, animationInterval) {
    // iterates through an array of points and draws an animation of the complete path
    let i = 1;
    let drawInterval = setInterval(() => {
        if(i >= points.length) {
            clearInterval(drawInterval)
            return;
        }

        var startPoint = points[i];
        var endPoint = points[i - 1];
        drawLine(context, startPoint, endPoint)

        i++;
    }, animationInterval || 30);
}
```

If you replace the call to `drawPath` with `drawPathAnimation`, you should see this:

{% include video.html path="draw-path-animation.mov" %}

[Here's what your code should look like](https://github.com/jskopek/drawing-tool/commit/98b1876331b07668a10e798cc17fedc2fbcb8912)

Allright! Now we're starting to get somewhere

## Refactoring the code that generates paths

Let's clean up the code that tracks when a path is being drawn. We will create a function that monitors for a clicked cursor drag event and stores the points in the line:

```
function getCursorCoords(e) {
    // takes a touch event and returns a dictionary of {x, y} values
    var touchEvt = (e.touches && e.touches[0]) ? e.touches[0] : e;
    return {
        x: parseInt(touchEvt.pageX),
        y: parseInt(touchEvt.pageY)
    }
}


function monitorDrawEvents(canvas, userCallbacks) {
    // monitors any draw events on the canvas
    // a draw event is when a cursor is moved while the mouse is pressed
    // optional callbacks:
    //  - onUpdate(startPoint, endPoint): returns a starting and ending point dict, which contain x & y values, when a pressed cursor is moved
    //  - onComplete(points): returns an array of points that make up a complete path when the cursor is released
    let callbacks = Object.assign({
        onUpdate: (startPoint, endPoint) => {},
        onComplete: (points) => {}
    }, userCallbacks);

    var isMousedown = false;
    var points = [];
    var point;


    ['touchstart', 'mousedown'].forEach((eventName) => {
        canvas.addEventListener(eventName, function (e) {
            isMousedown = true
        })
    });

    ['touchmove', 'mousemove'].forEach((eventName) => {
        canvas.addEventListener(eventName, function (e) {
            if (!isMousedown) return

            e.preventDefault()

            var newPoint = getCursorCoords(e)
            points.push(newPoint)

            callbacks.onUpdate(point, newPoint)

            point = newPoint
        })
    });

    ['touchend', 'touchleave', 'mouseup'].forEach((eventName) => {
        canvas.addEventListener(eventName, function (e) {
            isMousedown = false

            callbacks.onComplete(points)

            points = []
            point = undefined;
        })
    });
}
```

Now that we have this function, let's re-implement our main appliaction code:

```
var canvas = document.querySelector('canvas');
var context = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

monitorDrawEvents(canvas, {
    onComplete: (points) => {
        drawPathAnimation(points, context);
    }
});
```

Add this code, and you should see something like this:

{% include video.html path="monitor-draw-events.mov" %}

[Here's what your code should look like](https://github.com/jskopek/drawing-tool/commit/0138aa9450b4215a1b792eff8324f4962a75dc61)


## Erasing Lines

We've now got a basic drawing tool that can store each line, and re-draw it. Coming up next, we will learn to create an eraser that can erase individual lines.

