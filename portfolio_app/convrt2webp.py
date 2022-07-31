from glob import glob
from PIL import Image
paths=glob('sub_app/static/img/*.jpg')+glob('sub_app/static/img/*.png')

for p in paths:
    image = Image.open(p)
    image = image.convert('RGB')
    image.save(p[:-3]+'webp', 'webp')