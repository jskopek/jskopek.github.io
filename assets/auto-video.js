$(function() {
    $('video:not(.noloop)').each(function() { this.loop = true; });
    $('video.autoplay').each(function() { this.play(); });

    $('video').appear();
    $('video').on('disappear', function(e) {
        e.currentTarget.pause();
        $(e.currentTarget).nextAll('video')[0].play();
        //debugger;
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
