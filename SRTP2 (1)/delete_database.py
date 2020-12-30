#coding:utf-8
import sqlite3

conn = sqlite3.connect('srtp.db')
c = conn.cursor()
print ("Opened database successfully")

c.execute("delete from user;")#改user为key_freq可
  
print ("Operation done successfully")
conn.commit()
conn.close()
