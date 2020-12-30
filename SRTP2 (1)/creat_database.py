import sqlite3
encoding='utf-8'
def create_database_fun():
	try:
		conn = sqlite3.connect('srtp.db')
		print ("Opened database successfully")
		c = conn.cursor()
		c.execute('''CREATE TABLE key_freq
			   (keyword  CHAR(10) NOT NULL,
			   freq    INT,
			   time CHAR(10));''')
		print ("Table created successfully")
		conn.commit()
		conn.close()
	except sqlite3.OperationalError :
		print("exists")
		
	
