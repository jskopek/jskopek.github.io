import sys
import os
import re
from PIL import Image
from PIL import ExifTags
import traceback


def reorient_from_exif(image):
    try:
        if hasattr(image, '_getexif'): # only present in JPEGs
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation]=='Orientation':
                    break
            e = image._getexif()       # returns None if no EXIF data
            if e is not None:
                exif=dict(e.items())
                orientation = exif[orientation]

                if orientation == 3:
                    return image.transpose(Image.ROTATE_180)
                elif orientation == 6:
                    return image.transpose(Image.ROTATE_270)
                elif orientation == 8: 
                    return image.transpose(Image.ROTATE_90)
                else:
                    return image
    except:
        return image

path = '.'
if len(sys.argv) >= 2:
    path = sys.argv[1]

for expected_folder in ['large', 'small']:
    if expected_folder not in os.listdir(path):
        print(f'Could not find `{expected_folder}` folder; creating now')
        os.mkdir(f'{path}/{expected_folder}')

small_path = os.path.join(path, 'small')
large_path = os.path.join(path, 'large')

filenames = []
for filename in os.listdir(path):
    if re.search('\.(jpg|jpeg|png|gif)$', filename):
        filenames.append(filename)

filenames = sorted(filenames)


for index, file_path in enumerate(filenames):
    file_name, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.replace('.','')

    
    im = Image.open(f'{path}/{file_path}')
    width, height = im.size
    im = reorient_from_exif(im)
    file_path = f'{index + 1}.{file_extension}'
    im.save(f'{large_path}/{file_path}', file_extension, quality=80)

    #im.thumbnail(width, height)
    im.save(f'{small_path}/{file_path}', file_extension, quality=50)

    print(f'{{% include photo.html alt="{file_path}" path="{small_path}/{file_path}" large_path="{large_path}/{file_path}" width={width} height={height} %}}')



