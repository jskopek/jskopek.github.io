var ffmpeg = require('fluent-ffmpeg');
var fs = require('fs');
var path = require('path');
var _ = require('underscore');
var minimist = require('minimist');

function generate(videoDir, generateHd, generateSd, generateThumbnail) {
    var files = fs.readdirSync(videoDir)
    var videos = _.filter(files, (file) => file.match(/\.mov$/));

    videos.forEach((videoFilename) => {
        try {
            fs.mkdirSync(path.join(videoDir, 'thumbnails'));
            fs.mkdirSync(path.join(videoDir, 'hd'));
            fs.mkdirSync(path.join(videoDir, 'sd'));
        } catch(e) {}

        var inputFile = path.join(videoDir, videoFilename);
        var videoName = path.basename(videoFilename, path.extname(videoFilename));

        if(generateSd) { ffmpeg(inputFile).videoCodec('libx264').size('50%').output(path.join(videoDir, 'sd', videoName + '.mp4')).run(); }
        if(generateHd) { ffmpeg(inputFile).videoCodec('libvpx').inputOptions(['-quality good', '-cpu-used 1', '-qmin 10', '-qmax 42']).output(path.join(videoDir, 'hd', videoName + '.webm')).run(); }
        if(generateThumbnail) {
            ffmpeg(inputFile).on('end', () => {
                fs.renameSync(path.join(videoDir, 'thumbnails', videoFilename, 'tn.png'), path.join(videoDir, 'thumbnails', videoName + '.png'));
            }).screenshots({count: 1, folder: path.join(videoDir, 'thumbnails', videoFilename), size: '320x240'});
        }

        console.log('{% include video.html title="' + videoName + '" %}');
    });

}

var args = minimist(process.argv.slice(2));
console.log(args);

var videoDir = args['_'];
var generateHd = args['nohd'] ? false : true;
var generateSd = args['nosd'] ? false : true;
var generateThumbnail = args['nothumbnail'] ? false : true;

generate(videoDir, generateHd, generateSd, generateThumbnail);
