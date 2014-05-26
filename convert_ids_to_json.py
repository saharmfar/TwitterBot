#!usr/bin/python

import json

with open("target_user_ids.txt", "r") as f:
    lines = f.readlines()
    
for (i, line) in enumerate(lines):
    lines[i] = line.replace('\n', '')    
    
with open("target_user_ids.json", "w") as f:
    json.dump(lines, f)


