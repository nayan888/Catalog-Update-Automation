#!/usr/bin/env python3

import os
from PIL import Image

image_dir = os.path.join('supplier-data', 'images')
tiff_images = [img for img in os.listdir(image_dir) if img.endswith('.tiff')]

for img in tiff_images:
    img_path = os.path.join(image_dir, img)
    image = Image.open(img_path)
    new_image = image.rotate(-90).resize((600,400)).convert('RGB')

    file, ext = os.path.splitext(img)
    outpath = os.path.join(image_dir, file + '.jpeg')
    new_image.save(outpath, "JPEG")
