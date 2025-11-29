#!/usr/bin/python3
import marshal

with open("/tmp/hidden_4.pyc", "rb") as f:
    f.read(16)  # skip header of pyc file
    code = marshal.load(f)

names = sorted(name for name in code.co_names if not name.startswith("__"))
for name in names:
    print(name)
