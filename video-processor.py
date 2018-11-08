#!/usr/bin/env python3

"""
Requirements:
    - Handbrake CLI: https://handbrake.fr/downloads2.php
    - ffmpeg

Installing ffmpeg on OSX with Homebrew

    brew install libvpx
    brew install ffmpeg --with-libvpx
"""
import sys
import os
import getopt
import subprocess
from datetime import date
from collections import defaultdict

ENCODINGS = [
    ('Apple 2160p60 4K HEVC Surround', 'hd', '__filename__.mp4'),
    ('VP9 MKV 2160p60', 'hd', '__filename__.webm'),
    #('Android 1080p30', 'hd', '__filename__-h264.mp4'),
    ('Android 480p30', 'sd', '__filename__.mp4'),
]
 
# FUNCTIONS
def find_handbrake():
    """
    source: https://github.com/onlyhavecans/HandBreak-It
    Finds and returns the handbrake binary as string.
    It uses brute force but it should be OS agnostic.
    Should be private.
    """
    if sys.platform == 'win32':
        if os.path.isfile("HandBrakeCLI.exe"):
            return os.path.abspath("HandBrakeCLI.exe")
        else:
            raise Exception("HandbrakeCLI.exe not installed next to script!")
    elif os.path.isfile("/Applications/HandBrakeCLI"):
        return "/Applications/HandBrakeCLI"
    elif call(['which', '-s', 'HandBrakeCLI']):
        output = check_output(['which', 'HandBrakeCLI'])[0]
        return output.strip()
    else:
        raise Exception("HandbrakeCLI not installed!")

def silent_make_folder(folder_name):
    try:
        os.mkdir(folder_name)
        print(f'Created folder {folder_name}')
    except FileExistsError:
        pass

def generate_video_metadata(input_name, src_large_list, src_small_list, thumbnail, created_at=None):
    if not created_at:
        today = date.today()
        year = int(input('Enter year (%d): ' % today.year) or today.year)
        month = int(input('Enter month (%d): ' % today.month) or today.month)
        day = int(input('Enter day (%d): ' % today.day) or today.day)
        created_at = date(year, month, day)

    content = f"""---
layout: timelapses
title:  "{input_name}"
date:   {created_at.year}-{created_at.month}-{created_at.day} 00:00:01 +0100
src_large: {','.join(src_large_list)}
src_small: {','.join(src_small_list)}
thumbnail: {thumbnail}
categories:
summary:
---
"""
    file_name = f'{created_at.year}-{created_at.month}-{created_at.day}-{input_name}.md'
    with open(file_name, 'w') as f:
        f.write(content)
    print(f'Created meta file at: {file_name}')

def generate_thumbnail(input_path, output_path):
    # scale to 720:x
    # quality is 5 (1-30)
    # skip first two seconds (in event of dark/black start)
    # only capture one frame
    subprocess.run(['ffmpeg', '-i', input_path, '-filter:v', 'scale=720:-1', '-ss', '2', '-qscale:v', '5', '-vframes', '1', output_path], capture_output=True)
    print(f'Created thumbnail at: {output_path}')


# CODE
if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h', ['help', 'dry-run', 'auto-date', 'video-tag'])
    except getopt.GetoptError:
        print('video-processor.py [--dry-run] [--auto-date] [--video-tag]')
        sys.exit(2)

    options = [opt for (opt, arg) in opts]

    if '--help' in options or '-h' in options:
        print('video-processor.py [--dry-run] [--auto-date] [--video-tag]')
        sys.exit()
    elif not len(args):
        print('Filename or folder name must be passed')
        sys.exit()

    dry_run = True if '--dry-run' in options else False
    auto_date = True if '--auto-date' in options else False
    video_tag = True if '--video-tag' in options else False
    input_path = args[0]

    if os.path.isdir(input_path):
        file_paths = [f'{input_path}/{file_name}' for file_name in os.listdir(input_path)]
    else:
        file_paths = [input_path]

    for file_path in file_paths:
        # make sure not folder
        if(os.path.isdir(file_path)):
            print(f'Skipping directory: {file_path}')
            continue

        # make sure is valid movie type
        extension = os.path.splitext(os.path.basename(file_path))[1]
        if extension not in ['.mov', '.mp4', '.mpeg', '.mkv', '.webm', '.avi']:
            print(f'Skipping file, as extension {extension} is not valid')
            continue

        input_name = os.path.splitext(os.path.basename(file_path))[0] # just the file_name without the folder or extension

        print(f'Processing file: {input_name}')

        handbrakeCLI = find_handbrake()

        # encode video
        folder_files_dict = defaultdict(list)
        for preset, folder_name, file_name in ENCODINGS:
            file_name = file_name.replace('__filename__', input_name)
            output_path = os.path.join(folder_name, file_name)
            folder_files_dict[folder_name].append(output_path)

            print(f'Encoding file with `{preset}` preset. Output: {output_path}')
            if not dry_run:
                silent_make_folder(folder_name)
                print(subprocess.run([handbrakeCLI, '--preset', preset, '-i', file_path, '-o', output_path], capture_output=True))


        if not dry_run:
            # thumbnail
            silent_make_folder('thumbnails')
            thumbnail_path = f'thumbnails/{input_name}.jpg'
            generate_thumbnail(file_path, thumbnail_path)

            # metadata
            if video_tag:
                print(f'{{% include video.html title="{input_name}" controls=True %}}')
            else:
                generate_video_metadata(input_name, folder_files_dict['large'], folder_files_dict['small'], thumbnail_path, created_at=date.today() if auto_date else None)

        print('\n')

    print('Done!')
