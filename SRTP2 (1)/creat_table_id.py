import sqlite3
encoding='utf-8'
conn = sqlite3.connect('srtp_id.db')
print ("Opened database successfully")
c = conn.cursor()
c.execute('''CREATE TABLE user
       (id  CHAR(20) NOT NULL,
       password    char(20) not null,
       email CHAR(20) not null);''')

print ("Table created successfully")
conn.commit()
conn.close()
