from pathlib import Path

fname =  Path(__file__).with_suffix('.txt')

with open(fname, 'w') as fo:
    fo.write('Can\'t we all just get along?\n')

with open(fname, 'a') as fo:
    fo.write('21 seasons of conflict from TNG, DS9, and Voyager would indicate...no\n')

with open(fname, 'a') as fo:
    fo.write('Besides, we all know the Enterprise could take the Millennium Falcon any time.\n')
