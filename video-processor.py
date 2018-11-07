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
import subprocess
from datetime import date
from collections import defaultdict

input_path = sys.argv[1]
dry_run = True if len(sys.argv) > 2 and sys.argv[2] == '--dry-run' else False  # bit of a hack

ENCODINGS = [
    ('Apple 2160p60 4K HEVC Surround', 'large', '__filename__.mp4'),
    ('VP9 MKV 2160p60', 'large', '__filename__.webm'),
    #('Android 1080p30', 'large', '__filename__-h264.mp4'),
    ('Android 480p30', 'small', '__filename__.mp4'),
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
    input_name = os.path.splitext(os.path.basename(input_path))[0] # just the file_name without the folder or extension

    handbrakeCLI = find_handbrake()

    # create necessary folder names
    folder_names = [folder_name for encoding, folder_name, file_name in ENCODINGS]
    for folder_name in folder_names:
        silent_make_folder(folder_name)

    # encode video
    folder_files_dict = defaultdict(list)
    for preset, folder_name, file_name in ENCODINGS:
        file_name = file_name.replace('__filename__', input_name)
        output_path = os.path.join(folder_name, file_name)
        folder_files_dict[folder_name].append(output_path)

        print(f'Encoding file with `{preset}` preset. Output: {output_path}')
        if not dry_run:
            subprocess.run([handbrakeCLI, '--preset', preset, '-i', input_path, '-o', output_path], capture_output=True)


    # thumbnail
    silent_make_folder('thumbnails')
    thumbnail_path = f'thumbnails/{input_name}.jpg'
    generate_thumbnail(input_path, thumbnail_path)

    # metadata
    generate_video_metadata(input_name, folder_files_dict['large'], folder_files_dict['small'], thumbnail_path)

    print('Done!')
