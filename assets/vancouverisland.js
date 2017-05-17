$(function() {
    $('video:not(.noloop)').each(function() { this.loop = true; });
    $('video.autoplay').each(function() { this.play(); });
    $('video:not(.autoplay)').on('mouseover', function() { easePlaybackIn(this); });
    $('video:not(.autoplay)').on('mouseout', function() {
        if($(this).hasClass('fullscreen')) { return; }
        easePlaybackOut(this); 
    });
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
