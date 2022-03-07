#!/usr/bin/env python3

import re
import os
import sys
from pathlib import Path

for fullpath in Path('content').rglob('*.md'):
    print(fullpath)
    with open(fullpath, 'w') as file:
        content = file.read()
        image_removed = re.sub("!\[([\w\d\.\s]+)\]\(/images/(.*)\.(jpg|png|gif)\)", "", content)

        file.write(content)

        file.close()




