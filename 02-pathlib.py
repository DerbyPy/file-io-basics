from pathlib import Path

print('This file is: ', repr(__file__))
print('As a Path obj: ', repr(Path(__file__)))

fname =  Path(__file__).with_suffix('.txt')
print('Swap the suffix:', repr(fname))

with open(fname) as fo:
    contents = fo.read().strip()
    print(type(contents))
    print(contents)
