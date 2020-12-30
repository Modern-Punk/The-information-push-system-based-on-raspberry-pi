#coding:utf-8
import sqlite3
import json

def new_user(user_id,user_password,user_email):
	conn = sqlite3.connect('srtp.db')
	c = conn.cursor()
	conn.text_factory = str
	flag=0
	cursor = c.execute("SELECT id,password from user")#查询关键词和对应的频次
	for row in cursor:
		str1 = json.dumps(row[0], ensure_ascii=False)
		#print(json.loads(str1))
		if(user_id==row[0]):
			flag=1
			break
	print("-----------")
	if (flag==0):
		c.execute("INSERT INTO user (id,password,email) VALUES(?,?,?)",(user_id,user_password,user_email))
	elif(flag==1):
		c.execute("update user set password=? ,email=? where id=?",(user_password,user_email,user_id))#更新频次+1

	conn.commit()
	print ("Records created successfully")
	conn.close()
	
