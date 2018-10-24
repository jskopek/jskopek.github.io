// parse slide data (url, title, size ...) from DOM elements 
// (children of gallerySelector)
var parseThumbnailElements = function(css_selector) {
    let items = []
    document.querySelectorAll(css_selector).forEach((figureEl) => {
        let linkEl = figureEl.querySelector('a');
        let size = linkEl.getAttribute('data-size').split('x');

        // create slide object
        let item = {
            el: figureEl,
            src: linkEl.getAttribute('href'),
            w: parseInt(size[0], 10),
            h: parseInt(size[1], 10)
        };
        if(figureEl.querySelector('figcaption')) {
            item.title = figureEl.querySelector('figcaption').innerHTML;
        }
        if(figureEl.querySelector('img')) {
            item.msrc = figureEl.querySelector('img').getAttribute('src');
        }
        items.push(item);
    });
    return items;
}

var initPhotoSwipeFromDOM = function(css_selector) {
    // loop through all gallery elements and bind events
    document.querySelectorAll(css_selector).forEach((imageEl, index) => {
        imageEl.addEventListener('click', (e) => {
            e.preventDefault();

            let pswpElement = document.querySelector('.pswp');
            let items = parseThumbnailElements(css_selector);

            // Pass data to PhotoSwipe and initialize it
            let gallery = new PhotoSwipe(pswpElement, PhotoSwipeUI_Default, items, {
                index: index,
                getThumbBoundsFn: function(index) {
                    // See Options -> getThumbBoundsFn section of documentation for more info
                    let thumbnail = items[index].el.getElementsByTagName('img')[0]; // find thumbnail
                    let pageYScroll = window.pageYOffset || document.documentElement.scrollTop;
                    let rect = thumbnail.getBoundingClientRect(); 

                    return {x:rect.left, y:rect.top + pageYScroll, w:rect.width};
                }
            });
            gallery.init();
        });
    });
}
