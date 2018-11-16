import sys
import os
import re
from PIL import Image

path = '.'
if len(sys.argv) >= 2:
    path = sys.argv[1]

for expected_folder in ['large', 'small']:
    if expected_folder not in os.listdir(path):
        print('Invalid folder structure present; should have "%s" folder in path' % expected_folder)

small_path = os.path.join(path, 'small')
large_path = os.path.join(path, 'large')

filenames = []
for filename in os.listdir(small_path):
    if re.search('\.(jpg|jpeg|png|gif)$', filename):
        filenames.append(filename)

filenames = sorted(filenames)


#num_images = int(input('How many images? '))
#path = input('What is the path to the image folder on the static server? ')
#alt_text = input('What is the alt text? ')
#
for filename in filenames:
    im = Image.open(f'{small_path}/{filename}')
    width, height = im.size
    print(f'{{% include photo.html alt="{filename}" path="{small_path}/{filename}" large_path="{large_path}/{filename}" width={width} height={height} %}}')
