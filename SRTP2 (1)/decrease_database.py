#coding:utf-8
import sqlite3
import json
def freq_time(ti,decrease,conn):#关键词推送
	#conn=sqlite3.connect('srtp.db')
	c=conn.cursor()
	conn.text_factory = str
	flag = 0#用于检测传入时间是否存在
	find_ti = c.execute("select keyword,time from key_freq")
	for row in find_ti:
		str1 = json.dumps(row[1], ensure_ascii=False)
		#print(json.loads(str1))
		if(ti==row[1]):
			flag=1
	if(flag==1):
		cursor = c.execute("SELECT freq from key_freq where time = '%s'"%ti)
		for row in cursor:
			freq1=row[0]#freq1=传入时间所对应的频次
		c.execute("update key_freq set freq=? where time = ?",(freq1-decrease,ti))
	else:
		print("查询时间不存在")
	c.execute("delete from key_freq where freq <= 0")
	conn.commit()
	#conn.close()

#freq_time("2020-12-14-19-46",4)
