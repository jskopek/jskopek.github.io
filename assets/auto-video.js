$(function() {
    $('video:not(.noloop)').each(function() { this.loop = true; });
    $('video.autoplay').each(function() { this.play(); });
    $('video:first')[0].play();

    $('video').appear();
    $('video').on('appear', function(e) {
        if(!e.currentTarget.paused) { return; } // already playing

        var videoBottomPixel = $(e.currentTarget).offset().top + $(e.currentTarget).height() / 2 // absolute bottom px of the current video
        var windowBottomPixel = $(window).scrollTop() + $(window).height(); // absolute bottom px of the scrolled window
        if(videoBottomPixel <= windowBottomPixel) {
            // if the video's bottom is entirely in view, play it and pause other videos
            $('video').each(function() { this.pause(); });
            e.currentTarget.play();
        }
    });

    // fullscreen toggle
    $('video').on('click', function (e) {
        $(this).toggleClass('fullscreen');
        $('body').toggleClass('fullscreen');
        if(!$(this).hasClass('fullscreen')) { easePlaybackOut(this); }
    });
    $('body').on('click', function(e) {
        if(e.target.tagName.toLowerCase() == 'video') { return; }
        $('video.fullscreen').click();
    });

});

// deprecated
function easePlaybackIn(el) {
    el.playbackRate = 0.5;
    setTimeout(function() { el.playbackRate = 0.8; }, 200);
    setTimeout(function() { el.playbackRate = 1; }, 400);
    el.play();
}
function easePlaybackOut(el) {
    el.playbackRate = 0.8;
    setTimeout(function() { el.playbackRate = 0.5; }, 200);
    setTimeout(function() { el.pause(); }, 400);
}
