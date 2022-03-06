#!/usr/bin/env python3

from markdownify import markdownify as md
import argparse
import re
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='file to convert')
args = parser.parse_args()

input_file = args.input_file

print(input_file)

if not re.search('.dist.php', input_file):
    test_file = re.sub('\.php', '.dist.php', input_file)
    print(test_file)
    try:
        os.stat(test_file)
        print('file dist exists, ignoring')
        sys.exit(0)
    except:
        os.rename(input_file, test_file)
        print('file renamed, rerun job')
        sys.exit(0)


output_file = os.path.splitext(input_file)[0]
output_file = os.path.splitext(output_file)[0]
output_file = output_file + '.md'
print(output_file)

# sys.exit(0)

with open(input_file, 'r') as file:
    content = file.read()
    html = md(content)
    firstline = html.split('\n', 1)[0]
    if re.search('php include', firstline):
        print('ignore file')
        # os.remove(input_file)
        sys.exit(0)
    # print(firstline)
    ## fix images path
    html = html.replace('](images/', '](/images/')
    # html = re.sub("{lien:db:(\d+):", "", html)
    # html = re.sub("(html:lien})", "", html)
    html = re.sub("(\s)({lien:db:)(\d+):(.*):(.*)(\.html:lien})(\s)", " \\4 ", html)
    html = re.sub("(’)({lien:db:)(\d+):(.*):(.*)(\.html:lien})(,)", "'\\4 ", html)
    html = re.sub("(\s)({lien:db:)(\d+):(.*):(.*)(\.html:lien})(,)", " \\4,", html)
    # html = re.sub("(\ )({lien:db:)(\d+):(.*):(.*)(\.html:lien})(,)", " \\4,", html)
    # html = re.sub("(\ )({lien:db:)(\d+):(.*):(.*)(\.html:lien})(\s)", " \\4,", html)
    # html = re.sub("(\ )({lien:db:)(\d+):(.*):(.*)(\.html:lien})(\.)", " \\4.", html)
    html = re.sub("(\s)({lien:db:)(\d+):(.*):(.*)(\.html:lien})(\.)", " \\4.", html)
    html = re.sub("(<\?php echo \$_SERVER\[\'REQUEST_URI\'\]; \?>)", "", html)
    html = re.sub("(php include\(\"modules/flag\\_spoiler\.php\"\); \?)", "", html)
    # print(html)
    result = '---\ntitle: "'+ firstline + '"\n---\n\n' + html
    # print(output)
    with (open(output_file, 'w')) as output:
        output.write(result)
        output.close()
    file.close()


