import sqlite3

conn=sqlite3.connect('srtp.db')
c=conn.cursor()

c.execute("drop table id_password")

conn.commit()
conn.close()
