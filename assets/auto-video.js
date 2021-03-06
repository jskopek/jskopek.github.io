$(function() {
    $('video:not(.noloop)').each(function() { this.loop = true; });
    $('video.autoplay').each(function() { this.play(); });

    //$('video').each(function() { this.pause(); });
    $('video:first')[0].play();

    $('video').appear();
    $('video').on('appear', function(e) {
        if(!e.currentTarget.paused) { return; } // already playing
        if(getUrlParameter('autoplay') == 'false') { return; } // check for disable param

        // handle an edge case; the top video will not always 'activate', so we do a special check to see if the window is scrolled to the top and the first video is playing
        if(($(window).scrollTop() == 0) && (!$('video:first')[0].playing)) {
            $('video').each(function() { this.pause(); });
            $('video:first')[0].play();
            return;
        }

        var videoBottomPixel = $(e.currentTarget).offset().top + $(e.currentTarget).height() / 2 // absolute bottom px of the current video
        var windowBottomPixel = $(window).scrollTop() + $(window).height(); // absolute bottom px of the scrolled window
        if(videoBottomPixel <= windowBottomPixel) {
            // if the video's bottom is entirely in view, play it and pause other videos
            $('video').each(function() { this.pause(); });
            e.currentTarget.play();
        }
    });

	$('.button-quality input').on('click', function(e) {
        var isSd = $(this).is(':checked');
        $('video').each(function() {
            var isPlaying = !this.paused;
            $(this).attr('src', isSd ? $(this).data('srcHd') : $(this).data('srcSd'));
            if(isPlaying) { this.play(); }
        });
	});

    // fullscreen toggle
//    $('video').on('click', function (e) {
//        $(this).toggleClass('fullscreen');
//        $('body').toggleClass('fullscreen');
//        if(!$(this).hasClass('fullscreen')) { easePlaybackOut(this); }
//    });
//    $('body').on('click', function(e) {
//        if(e.target.tagName.toLowerCase() == 'video') { return; }
//        $('video.fullscreen').click();
//    });

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


var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : sParameterName[1];
        }
    }
};
