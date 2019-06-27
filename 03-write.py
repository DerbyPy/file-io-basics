from pathlib import Path

fname =  Path(__file__).with_suffix('.txt')
with open(fname, 'w') as fo:
    fo.write('Maybe Neither?\n')
