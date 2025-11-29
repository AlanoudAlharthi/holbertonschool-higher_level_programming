#!/usr/bin/python3
import marshal
import types

# Open the .pyc file and skip the header
with open("/tmp/hidden_4.pyc", "rb") as f:
    f.read(16)  # Skip header (magic number + timestamp/hash)
    code = marshal.load(f)

# Create a module from the code
hidden_4 = types.ModuleType("hidden_4")
exec(code, hidden_4.__dict__)

# Print all names not starting with '__', sorted alphabetically
for name in sorted(name for name in dir(hidden_4) if not name.startswith("__")):
    print(name)
