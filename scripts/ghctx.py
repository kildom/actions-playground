

from argparse import ArgumentParser
import re
import sys
import inputs

parser = ArgumentParser()
parser.add_argument('-p', '--posix', action='store_true')
parser.add_argument('-n', '--new-line', action='store_true')
parser.add_argument('name')
args = parser.parse_args()

parts:'list[str]' = args.name.split('.')

item = inputs.contexts
for part in parts:
    key = part.strip()
    if key not in item:
        print(f'Invalid key "{key}"', file=sys.stderr)
        exit(1)
    item = item[key]

result = str(item)

if args.posix:
    result = inputs.posix_path(result)

if args.new_line:
    print(result)
else:
    print(result, end='')
