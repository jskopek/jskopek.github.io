# Blog

This is where all the implementation details of the blog will go

It's worth pointing out that all of this is *early*, and there are many janky things here that will be polished over time. This blog is very much a work in progress!

## Photos

There is an include that helps embed photos in a blog post. An example is shown below:

    {% include photo.html alt="5.jpg" path="costa-rica/arenal/small/5.jpg" medium_path="costa-rica/arenal/medium/5.jpg" large_path="costa-rica/arenal/large/5.jpg" width=1368 height=912 %}

To show images side-by-side, wrap them in a div element with a .gallery-tiled class. This will cause them to share the width. Example:


    <div class="gallery-tiled">
        {% include photo.html alt="5.jpg" path="costa-rica/arenal/small/5.jpg" medium_path="costa-rica/arenal/medium/5.jpg" large_path="costa-rica/arenal/large/5.jpg" width=1368 height=912 %}
        {% include photo.html alt="4.jpg" path="costa-rica/arenal/small/4.jpg" medium_path="costa-rica/arenal/medium/4.jpg" large_path="costa-rica/arenal/large/4.jpg" width=1368 height=912 %}
    </div>

Right now, only the large_path and path are used. Medium path may be used in the future, or it's something I might just throw out.

I've written a script to generate resized images in the correct folder structure. It's available at `scripts/photo-resizer.py`. Just give it a folder that has a number of images in it as the only argument. Encoding and organization can also be done by hand. I use ImageOptim on mac to optimize image size and an Automator action to resize images down. Medium is 50% of original, small is 25% of original.

## Video

Just like with photos, I have a video include file that helps embed video. There are actually two:

    {% include video.html title="V1-0024_Driving Wet" %}
    {% include controllableVideo.html title="V1-0024_Driving Wet" %}

The video include is designed for posts that have autoplaying video. These videos will play automatically when they appear on the page, and have no controls. They loop automatically. The following scripts must be included at the bottom of an auto-playing page:

    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script type="text/javascript" src="/assets/jquery.appear.js"></script>
    <script type="text/javascript" src="/assets/auto-video.js"></script>

The controllable video include does not play automatically and shows controls.

In order for the video includes to work, a specific structure must be used. A video-folder must be defined at the top of the post, for example:

    ---
    ...
    layout: post
    video-folder: posts/vancouver-island/
    ...
    ---

This folder is relative to the static url for the blog. The folder must have a `hd`, `sd`, and `thumbnail` folders. Video filenames are determined based on the title, although this will probably change real real soon.

Video processing is a pain at the moment, although I am working on a script to help with this. The `video-processor.py` script will take a file or a folder of files and generate hd, sd, and thumbnail content for the video(s). It defaults to generating three encodings:

- Apple 2160p60 4K HEVC Surround (HD, iOS/macOS)
- VP9 MKV 2160p60 (HD, Chrome)
- Android 480p30 (SD, All)

The video-processor.py script was originally written to handle timelapses, and so it generates a timelapse markdown file by default. However, it can generate video include tags by passing a `--video-tag` argument to the script. The `--dry-run` argument will simulate the process but will not create anything. And the `--auto-date` argument will use today's date when needed, rather than asking you to enter it manually. You can always type `--help` to get the details as well.
