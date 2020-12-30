#coding:utf-8


def needpassword(user_id):
	import sqlite3
	import json
	conn=sqlite3.connect("srtp.db")
	c=conn.cursor()
	
	#判断输入的用户名是否已经在数据库中
	flag=0
	cursor=c.execute("select id,password from user")#
	for row in cursor:
		id_sql=json.dumps(row[0], ensure_ascii=False)#row[0]为id列
		if user_id==json.loads(id_sql):
			flag=1
			break
	
	if flag==1:#查询用户名所对应的密码
		cursor=c.execute("select password from user where id='%s'"%user_id)
		for row in cursor:
			str1 = json.dumps(row, ensure_ascii=False)
	elif flag==0:
		str1="wrong id"
	return str1
    
#password=needpassword("2018112285")
#print(password)
