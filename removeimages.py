#!/usr/bin/env python3

import re
import os
import sys
from pathlib import Path

for fullpath in Path('content').rglob('*.md'):
    print(fullpath)
    with open(fullpath, 'r') as file:
        content = file.read()
        image_removed = re.sub("!\[([\w\d\.\s]+)\]\(/images/(.*)\.(jpg|png|gif)\)", "", content)
        file.close()
    with open(fullpath, 'w') as file:
        print(image_removed)
        file.write(image_removed)






