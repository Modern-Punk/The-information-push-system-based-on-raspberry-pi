#coding:utf-8
import sqlite3
import json

def insert_keyword(x,ti):
	conn = sqlite3.connect('srtp.db')#连接数据库
	c = conn.cursor()
	conn.text_factory = str
	flag=0#flag=1表示需要插入的关键词已经在数据库中存在
	freq1=0
	cursor = c.execute("SELECT keyword,freq from key_freq")#查询关键词和对应的频次
	for row in cursor:
		str1 = json.dumps(row[0], ensure_ascii=False)
		print(json.loads(str1))
		if(x==row[0]):
			flag=1
			freq1=row[1]#freq1=现在关键词对应的频次
			break
	print("-----------")

	if(flag==1):
		c.execute("update key_freq set freq=?,time=? where keyword=?",(freq1+1,ti,x))#更新频次+1
		#c.execute("update key_freq set time=? where keyword=?",(ti,x))
	elif(flag==0):
		c.execute("INSERT INTO key_freq (keyword,freq,time) VALUES(?,?,?)",(x,1,ti))#插入新数据
	conn.commit()
	print ("Records created successfully")
	conn.close()
	

