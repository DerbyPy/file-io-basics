from pathlib import Path

fname =  Path(__file__).with_suffix('.txt')

with open(fname, 'w') as fo:
    fo.write('Star Wars!\n')

with open(fname, 'w') as fo:
    fo.write('Star Trek!\n')
