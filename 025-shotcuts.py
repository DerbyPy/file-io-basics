from pathlib import Path

fname =  Path(__file__)

with open(fname) as fo:
    line_num = 1
    for line in fo:
        print(f'line {line_num}: ', line.rstrip())
        line_num += 1
