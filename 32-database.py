import sqlite3
import re
conn=sqlite3.connect('50.3-newdata.sqlite')
cur=conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''
CREATE TABLE Users (email TEXT, count INTEGER)''')

hand=open('82-mbox.txt')
for line in hand:
    if not line.startswith('From: '): continue
    email=line.split()[1]

    cur.execute('SELECT count FROM Users WHERE email=?',(email,))
    row=cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Users (email,count) VALUES (?,1)',(email,))
    else:
        cur.execute('UPDATE Users SET count=count+1 WHERE email=?',(email,))
    conn.commit()

    sqlstr='SELECT email, count FROM Users ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(row[0],row[1])
    