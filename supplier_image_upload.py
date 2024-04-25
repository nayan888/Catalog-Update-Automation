#!/usr/bin/env python3

import os
import requests

image_dir = os.path.join('supplier-data', 'images')
jpeg_images = [img for img in os.listdir(image_dir) if img.endswith('.jpeg')]

url = "http://localhost/upload/"

for img in jpeg_images:
    with open(os.path.join(image_dir, img), 'rb') as opened_img:
        r = requests.post(url, files={'file': opened_img})
