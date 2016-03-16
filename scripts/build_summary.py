#!/usr/bin/env python3.5
import json
import os

base_dir = os.path.dirname(os.path.realpath(__file__))
manifest_path = base_dir + '/../docroot/static/manifest.json'
with open(manifest_path, 'r') as stream:
	manifest = json.load(stream)

count = 0
tags = []
for key, data in manifest.items():
	count += 1
	if 'tags' in data:
		tags.extend(data['tags'])
tags = set(tags)

print('\nYou have {} entries and {} tags.'.format(count, len(tags)))
