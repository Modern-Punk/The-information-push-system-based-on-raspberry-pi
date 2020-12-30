#coding:utf-8


import sqlite3
import json

conn = sqlite3.connect('srtp.db')
c = conn.cursor()
print ("Opened database successfully")

cursor = c.execute("SELECT keyword,freq,time from key_freq")
for row in cursor:
   str = json.dumps(row[0], ensure_ascii=False)
   #freq=json.dumps(row[1], ensure_ascii=False)
   print(json.loads(str))
   #print ("keyword = ",row[0])
   print (row[1])
   print(row[2])
   print("-----------")

print ("Operation done successfully")
conn.close()
