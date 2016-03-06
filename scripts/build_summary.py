#!/usr/bin/env python3.5
import sys
import json

manifest_json = sys.argv[1]
manifest = json.loads(manifest_json)

count = 0
tags = []
for key, data in manifest.items():
	count += 1
	if 'tags' in data:
		tags.extend(data['tags'])
tags = set(tags)

print('\nYou have {} entries and {} tags.'.format(count, len(tags)))
