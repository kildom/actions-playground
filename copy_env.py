
import os;
import sys;
import re;

output = '#!/bin/bash\n'

skip_vars = ('_', 'PWD')

for key, value in os.environ.items():
    if key in skip_vars:
        continue
    m = re.fullmatch(r'[\+,\-\.\/0-9:=A-Z_a-z]*', value)
    if m is None:
        output += f"read -r -d '' {key} <<'EnDOfThIssTrIng'\n{value}\nEnDOfThIssTrIng\n"
        output += f"export {key}\n"
    else:
        output += f'export {key}={value}\n'

with open(sys.argv[1] or 'job_vars', 'w') as fd:
    fd.write(output)
os.chmod(sys.argv[1] or 'job_vars', 0o755)
