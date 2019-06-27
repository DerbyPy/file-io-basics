# See also: http://kunststube.net/encoding/
from pathlib import Path
import sqlite3

fname =  Path(__file__).with_suffix('.txt')

# We can read the binary version, which may or may not be helpful
with open(fname, 'rb') as fo:
    contents = fo.read().strip()
    print(type(contents))
    print(contents)

# Default encoding (made explicit) is utf-8, but that won't work here:
with open(fname, 'r', encoding='utf-8', errors='replace') as fo:
    contents = fo.read().strip()
    print(type(contents))
    print(contents)

# The thing about encoding is, you can guess, but even when you are wrong, it may not always throw
# an error:
with open(fname, 'r', encoding='macroman') as fo:
    contents = fo.read().strip()
    print(type(contents))
    print(contents)

# This is actually what we intended
with open(fname, 'r', encoding='shift_jis') as fo:
    contents = fo.read().strip()
    print(type(contents))
    print(contents)
