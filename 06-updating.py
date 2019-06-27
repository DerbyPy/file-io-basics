# See also: http://kunststube.net/encoding/
from pathlib import Path
import sqlite3

fname =  Path(__file__).with_suffix('.txt')

fname.write_text('Star Wars rules!')
print('Current file contents: \n', fname.read_text())

with fname.open('r+') as fo:
    contents = fo.read()
    contents = contents.replace('ru', 'droo').replace('es', 's')
    contents += ' :oP'
    # Something is missing right here
    fo.write(contents)

print('New file contents: \n', fname.read_text())
