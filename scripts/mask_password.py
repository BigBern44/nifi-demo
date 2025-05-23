#!/usr/bin/env python3
import sys
import json
import hashlib

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        data = json.loads(line)
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict) and 'password' in item:
                    item['password'] = hashlib.sha256(item['password'].encode()).hexdigest()
        print(json.dumps(data))
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}", file=sys.stderr)