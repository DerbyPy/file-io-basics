from pathlib import Path
import sqlite3

fname =  Path(__file__).with_suffix('.db')

if fname.exists():
    fname.unlink()

conn = sqlite3.connect(fname)
c = conn.cursor()

# Put some data into the DB
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
conn.commit()
conn.close()

with open(fname) as fo:
    contents = fo.read().strip()
    print(type(contents))
    print(contents)
