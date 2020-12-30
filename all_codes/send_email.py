#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

class Mail:
    def __init__(self):
        # 第三方 SMTP 服务

        self.mail_host="smtp.qq.com"       #设置服务器:这个是qq邮箱服务器，直接复制就可以
        self.mail_pass="pnxjzfvlmjftddje"           #刚才我们获取的授权码
        self.sender = '3089488231@qq.com'      #你的邮箱地址 
        #self.email_name=self.sender
        self.email_name=None
        #self.receivers = ['3089488231@qq.com']  # 收件人的邮箱地址，可设置为你的QQ邮箱或者其他邮箱，可多个
        self.receivers=[]
        self.content=None
		
    def send(self):
		if self.content and self.email_name:
			self.receivers.append(self.email_name)# 收件人的邮箱地址
			message = MIMEText(self.content, 'plain', 'utf-8')

			message['From'] = Header("您的智能推送系统", 'utf-8')  
			message['To'] =  Header("主人", 'utf-8')
			
			subject = '推送消息'  #发送的主题，可自由填写
			message['Subject'] = Header(subject, 'utf-8') 
			try:
				smtpObj = smtplib.SMTP_SSL(self.mail_host, 465) 
				smtpObj.login(self.sender,self.mail_pass)  
				smtpObj.sendmail(self.sender, self.receivers, message.as_string())
				smtpObj.quit()
				print('邮件发送成功')
			except smtplib.SMTPException as e:
				print(e)
				print('send_email邮件发送失败')
		else:
			print("error")

"""
if  __name__ == '__main__':
    mail = Mail()
    mail.send()

"""
