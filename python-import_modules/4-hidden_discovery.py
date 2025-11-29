#!/usr/bin/python3
import marshal

def main():
    with open("/tmp/hidden_4.pyc", "rb") as f:
        f.read(16)  # skip header
        code = marshal.load(f)
    for name in sorted(code.co_names):
        if not name.startswith("__"):
            print(name)

if __name__ == "__main__":
    main()
