#!/usr/bin/env python3

import os
import requests

desc_dir = os.path.join('supplier-data', 'descriptions')
descriptions = []

for txt in os.listdir(desc_dir):
    description = {}

    with open(os.path.join(desc_dir, txt)) as fp:
        description['name'] = fp.readline().strip()
        description['weight'] = int(fp.readline().split()[0])
        description['description'] = fp.readline().strip()
        description['image_name'] = txt.replace('txt', 'jpeg')

    descriptions.append(description)

post_endpoint = "http://localhost/fruits/"
for description in descriptions:
    response = requests.post(post_endpoint, data=description)
