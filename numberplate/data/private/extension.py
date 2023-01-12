from PIL import Image
import os
for i in os.listdir():
    img = Image.open(i)
    img.resize((128,128))
    filename = i.split('.')
    filename = filename[0]
    img.save(f'{filename}.png', 'png')
    os.remove(i)