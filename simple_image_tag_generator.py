num_images = int(input('How many images? '))
path = input('What is the path to the image folder on the static server? ')
alt_text = input('What is the alt text? ')

for i in range(num_images):
    print(f'{{% include photo.html alt="{alt_text}" path="{path}" num={i + 1} %}}')
