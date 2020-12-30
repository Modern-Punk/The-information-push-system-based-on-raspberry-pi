#coding:utf-8
import sys
reload(sys)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtCore import QThread ,pyqtSignal 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QMovie
from baiduservice import Baidu_Asr
from tuling_service import Tuling_Chat
from recoder import record
from python_bug import baidusearch
from recoder import play_audio
from creat_database import create_database_fun
from insert_database import insert_keyword
from decrease_database import freq_time
from insert_user import new_user
from password_confirm import needpassword
from get_email import get_email
from send_email import Mail
import time
import datetime
import sqlite3
import json
sys.setdefaultencoding('utf8')

asr_client = Baidu_Asr('22783449', 'ulC5G0y6OKKUzq1qXwnceieU', 'D3wvoa3C3LaBFlf9DHlhO53C8oyX9fZa',
                       '/home/pi/Desktop/SRTP2/input.wave')
tuling_client = Tuling_Chat('020f3b022ef54789bb968c370b88718d', '630185')


class register_form(QDialog):
    def __init__(self,size,parent=None):
        super(register_form, self).__init__(parent)
        usrName = QLabel("UserName")
        passWd = QLabel("PassWord")
        email =QLabel("Email")
        self.userNameLineEdit = QLineEdit()
        self.passWdLineEdit = QLineEdit()
        self.passWdLineEdit.setEchoMode(QLineEdit.Password)
        self.emailLineEdit = QLineEdit()
        

        gridLayout = QGridLayout()
        gridLayout.addWidget(usrName, 0, 0, 1, 1)
        gridLayout.addWidget(passWd, 1, 0, 1, 1)
        gridLayout.addWidget(email, 2,0,1,1)
        gridLayout.addWidget(self.userNameLineEdit,0,1,1,3)
        gridLayout.addWidget(self.passWdLineEdit,1,1,1,3)
        gridLayout.addWidget(self.emailLineEdit,2,1,1,3)
		
        self.okPushBtn = QPushButton("确定")
        self.cancelPushBtn = QPushButton("取消")
        btnLayout = QHBoxLayout()
        btnLayout.setSpacing(60)
        btnLayout.addWidget(self.okPushBtn)
        btnLayout.addWidget(self.cancelPushBtn)

        dlgLayout = QVBoxLayout()
        dlgLayout.setContentsMargins(40,40,40,40)
        dlgLayout.addLayout(gridLayout)
        dlgLayout.addStretch(40)
        dlgLayout.addLayout(btnLayout)
        self.setLayout(dlgLayout)
        
       
        
        self.setWindowTitle("注册界面")
        self.resize(200,200)
#推送界面
class advert_form(QDialog):
	def __init__(self,size,parent=None):
		super(advert_form, self).__init__(parent)
		
		
		
		
		self.sp_day=QtWidgets.QSpinBox()
		self.label = QtWidgets.QLabel("天")
		self.label.setObjectName("label")
		
		self.sp_hour=QtWidgets.QSpinBox()
		self.label_2 = QtWidgets.QLabel("时")
		self.label_2.setObjectName("label2")
		
		self.sp_min=QtWidgets.QSpinBox()
		self.label_3 = QtWidgets.QLabel("分")
		self.label_3.setObjectName("label_3")
		
		self.label_4 = QtWidgets.QLabel("推送时间间隔：")
		self.label_4.setObjectName("label_4")
		
		self.like=QtWidgets.QSpinBox()
		self.label_5 = QtWidgets.QLabel("次")
		self.label_5.setObjectName("label_5")
		
		self.label_6 = QtWidgets.QLabel("喜爱阈值：")
		self.label_6.setObjectName("label_6")
		
		self.decrease=QtWidgets.QSpinBox()
		self.label_7 = QtWidgets.QLabel("天/次")
		self.label_7.setObjectName("label_7")
		
		self.label_8 = QtWidgets.QLabel("削减阈值：")
		self.label_8.setObjectName("label_8")
		
		self.pushButton = QPushButton("确定")
		self.pushButton.setObjectName("pushButton")
		
		self.pushButton2 = QPushButton("取消")
		self.pushButton2.setObjectName("pushButton2")
		
		gridLayout = QGridLayout()
		gridLayout.setSpacing(10)
		gridLayout.addWidget(self.label_4,1,0)
		gridLayout.addWidget(self.sp_day,1,1)
		gridLayout.addWidget(self.label,1,2)
		gridLayout.addWidget(self.sp_hour,1,3)
		gridLayout.addWidget(self.label_2,1,4)
		gridLayout.addWidget(self.sp_min,1,5)
		gridLayout.addWidget(self.label_3,1,6)
		gridLayout.addWidget(self.label_6,2,0)
		gridLayout.addWidget(self.like,2,1)
		gridLayout.addWidget(self.label_5,2,2)
		gridLayout.addWidget(self.label_8,3,0)
		gridLayout.addWidget(self.decrease,3,1)
		gridLayout.addWidget(self.label_7,3,2)
		gridLayout.addWidget(self.pushButton,4,1)
		gridLayout.addWidget(self.pushButton2,4,4)
		self.setLayout(gridLayout)
		
		self.setWindowTitle("推送设置界面")
		self.resize(int((size.width())*0.4),size.height()*0.8)
		
		

#爬虫界面
class python_bug_form(QDialog):
	def __init__(self, size, parent=None):
		super(python_bug_form, self).__init__(parent)
		
		self.keywords=None
		
		self.textEdit = QtWidgets.QTextEdit()
		self.textEdit.setObjectName("textEdit")

		self.label = QtWidgets.QLabel("爬取结果")
		self.label.setObjectName("label")

		self.label_2 = QLabel("附带链接")
		self.label_2.setObjectName("label_2")

		self.lineEdit_2 = QLineEdit()
		self.lineEdit_2.setObjectName("lineEdit_2")

		self.pushButton_3 = QPushButton("一键访问")
		self.pushButton_3.setObjectName("pushButton_3")

		self.radioButton = QRadioButton("语音播报")
		self.radioButton.setObjectName("radioButton")

		self.pushButton_4 = QPushButton("邮件发送")
		self.pushButton_4.setObjectName("pushButton_4")

		self.pushButton_5 = QPushButton("存入数据库")
		self.pushButton_5.setObjectName("pushButton_5")

		self.pushButton_6 = QPushButton("数据分析")
		self.pushButton_6.setObjectName("pushButton_6")
		
		self.pushButton = QPushButton("语音输入")
		self.pushButton.setObjectName("pushButton")

		self.lineEdit = QLineEdit()
		self.lineEdit.setObjectName("lineEdit")
		
		self.pushButton_2 = QPushButton("确定")
		self.pushButton_2.setObjectName("pushButton_2")

		self.label_3 = QLabel('')
		self.label_3.setObjectName("label_3")
		self.movie=QMovie("/home/pi/Desktop/SRTP2/timg.gif")
		self.label_3.setMovie(self.movie)

		self.label_4 = QLabel("网络爬虫")
		self.label_4.setObjectName("label_4")

		
		gridLayout = QGridLayout()
		gridLayout.setSpacing(10)
		gridLayout.addWidget(self.label_4,1,6-1,2,2)
		gridLayout.addWidget(self.label_3,1,0,1,1)
		gridLayout.addWidget(self.pushButton,3,1-1,1,2)
		gridLayout.addWidget(self.lineEdit,3,3-1,1,7)
		gridLayout.addWidget(self.pushButton_2,3,10-1,1,1)
		gridLayout.addWidget(self.label,4,0,1,2)
		gridLayout.addWidget(self.textEdit,5,0,6,6)
		gridLayout.addWidget(self.radioButton,5,7-1,1,2)
		gridLayout.addWidget(self.label_2,6,7-1,1,2)
		gridLayout.addWidget(self.lineEdit_2,7,7-1,1,3)
		gridLayout.addWidget(self.pushButton_3,7,9,1,1)
		gridLayout.addWidget(self.pushButton_5,8,7-1,1,4)
		gridLayout.addWidget(self.pushButton_4,9,7-1,1,4)
		gridLayout.addWidget(self.pushButton_6,10,7-1,1,4)
		self.setLayout(gridLayout)
		
		self.setWindowTitle("爬虫界面")
		self.movie.start()#gif
		self.resize(int((size.width())*0.75),size.height()*0.9)
		
	def set_asr_display(self,data): #显示输入的功能
		self.lineEdit.setText(data)
		
	def str_display(self,data):
		self.textEdit.setText(data)
		asr_client.tts_word(data)
		self.init_audio_thread()
	
	def list_display(self,data):
		info=""
		info_2="百度百科未搜索到相关内容，为您推送以下内容："
		i=1
		for data_com in data:
			info=info+data_com[0]+"\n"+data_com[1]+"\n"+"--------------------"+"\n"
		self.textEdit.setPlainText(info)
		for data_com in data:
			info_2=info_2+str(i)+data_com[0]
			i=i+1
		asr_client.tts_word(info_2)
		self.init_audio_thread()
		
	def init_audio_thread(self):
		self.audio=Audio_Thread()
		self.audio.start()
		
		
#login
class userForm(QDialog):
    def __init__(self, parent = None):
        super(userForm, self).__init__(parent)
        usrName = QLabel("UserName")
        passWd = QLabel("PassWord")
        self.userNameLineEdit = QLineEdit()
        self.passWdLineEdit = QLineEdit()
        self.passWdLineEdit.setEchoMode(QLineEdit.Password)

        gridLayout = QGridLayout()
        gridLayout.addWidget(usrName, 0, 0, 1, 1)
        gridLayout.addWidget(passWd, 1, 0, 1, 1)
        gridLayout.addWidget(self.userNameLineEdit,0,1,1,3)
        gridLayout.addWidget(self.passWdLineEdit,1,1,1,3)

        self.okPushBtn = QPushButton("确定")
        self.cancelPushBtn = QPushButton("取消")
        btnLayout = QHBoxLayout()
        btnLayout.setSpacing(60)
        btnLayout.addWidget(self.okPushBtn)
        btnLayout.addWidget(self.cancelPushBtn)

        dlgLayout = QVBoxLayout()
        dlgLayout.setContentsMargins(40,40,40,40)
        dlgLayout.addLayout(gridLayout)
        dlgLayout.addStretch(40)
        dlgLayout.addLayout(btnLayout)
        self.setLayout(dlgLayout)
        
       
        
        self.setWindowTitle("登录界面")
        self.resize(200,200)
        
        #self.pushButton.clicked['bool'].connect(self.gui_conversation)
        
        
	
	
	
#改动：后台线程
class BackendThread(QThread): #用于主界面
	update_data_1 = pyqtSignal(str)
	update_data_2 = pyqtSignal(str)
	def run(self):
		record()
		result_record = asr_client.get_asr_result()	
		self.update_data_1.emit(result_record) #该self指针是指向自己的类
		result_tuling = tuling_client.talk(result_record)
		self.update_data_2.emit(result_tuling)
		
class Bug_ASR_BackendThread(QThread):#爬虫界面中用于语音输入的后台线程
	update_data_1 = pyqtSignal(str)
	def run(self):
		record()
		result_record = asr_client.get_asr_result()	
		print(result_record)
		self.update_data_1.emit(result_record)

class Bug_BackendThread(QThread):
	update_data_1 = pyqtSignal(str)
	update_data_2 = pyqtSignal(list)
	keyword = None
	def run(self):
		print("后台运行ing")
		if self.keyword:
			info=baidusearch(self.keyword)
			print(info)
			if type(info)==list:
				print("列表")
				self.update_data_2.emit(info)
			else :
				print("数据")
				self.update_data_1.emit(info)
		else:
			print("Error")
		
class Audio_Thread(QThread):
	def run(self):
		play_audio()

class new_threshold(QThread):
	def __init__(self, time_spacing,like,decrease_threshold,parent = None):
		super(new_threshold,self).__init__(parent)
		with open('/home/pi/Desktop/SRTP2/set_advert.txt','r') as f:
			a=f.read()
			self.time_spacing=int(a.split()[0])
			time_spacing.append(self.time_spacing)
			self.like=int(a.split()[1])
			like.append(self.like)
			self.decrease_threshold=int(a.split()[2])
			decrease_threshold.append(self.decrease_threshold)
			self.a=None
			
	def str_display(self,data):
		asr_client.tts_word(data)
		self.c=Audio_Thread()
		self.c.start()
		
	def list_display(self,data):
		info_2="百度百科未搜索到相关内容，为您推送以下内容："
		i=1
		for data_com in data:
			info_2=info_2+str(i)+data_com[0]
			i=i+1
		asr_client.tts_word(info_2)
		self.c=Audio_Thread()
		self.c.start()

	def run(self):
		while True:
			print("checking is running")
			time.sleep(10)
			with open('/home/pi/Desktop/SRTP2/set_advert.txt','r') as f:
				a=f.read()
				self.time_spacing=int(a.split()[0])
				print(self.time_spacing)
				self.like=int(a.split()[1])
				print(self.like)
				self.decrease_threshold=int(a.split()[2])
				print(self.decrease_threshold)
			set_delta=datetime.timedelta(minutes=self.time_spacing)#生成时间差
			set_seconds=set_delta.total_seconds()
			print("settime:{}".format(set_seconds))
			now_time=datetime.datetime.now(tz=None)
			conn = sqlite3.connect('srtp.db')
			c = conn.cursor()
			print ("Opened database successfully")

			cursor = c.execute("SELECT keyword,freq,time from key_freq")
			for row in cursor:
				str = json.dumps(row[0], ensure_ascii=False)
				print(json.loads(str))
				print (row[1])
				print(row[2])
				past_time=row[2]
				past_time=datetime.datetime.strptime(past_time,"%Y-%m-%d-%H-%M")
				delta=now_time-past_time
				seconds=delta.total_seconds()
				print("time:{}".format(seconds))			
				if seconds >= set_seconds and int(row[1])>=self.like:#超过设定的时间阈值且关键字频次大于了喜爱的阈值
					print("running_advert")
					self.a=Bug_BackendThread()
					self.a.keyword=json.loads(str)
					self.a.update_data_1.connect(self.str_display)#str_display
					self.a.update_data_2.connect(self.list_display)
					self.a.start()
					print(past_time)
					freq_time(row[2],4,conn)#重要，需要手动修改
				decrease=(24*60*60)/self.decrease_threshold
				if seconds >= decrease:#几天削减一次频次
					freq_time(row[2],1,conn)
				print("-----------")
					
				
					

			print ("Operation done successfully")
			conn.close()
			
			"""
				file=open("/home/pi/Desktop/SRTP2/set_advert.txt")
				while True:
					text=file.readline()
					if not text:
						break
					self.time_spacing=
			"""
				
			
	
#结束

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		#创建数据库
		create_database_fun()
		
		#登录子窗口
		self.logForm=None
		#爬虫子窗口
		self.bug_dialog=None
		#智能推送子窗口
		self.advert_dialog=None
		#智能推送属性
		self.time_spacing=[]
		self.like_threshold=[]
		self.decrease_threshold=[]
		
		self.advert=new_threshold(self.time_spacing,self.like_threshold,self.decrease_threshold)
		self.advert.start()
		#注册和登录
		self.register_dialog=None
		self.__id=None
		self.__password=None
		self.__email=None
		self.log_flag=0
		#邮件发送
		self.mail = Mail()
		
		#改动：大小和中心
		self.screen = QDesktopWidget().screenGeometry()
		self.center_size(MainWindow)
		#结束
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.frame = QtWidgets.QFrame(self.centralwidget)
		
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame.setObjectName("frame")
		self.widget = QtWidgets.QWidget(self.frame)
		self.widget.setGeometry(QtCore.QRect(30, 20, 400, 32))
		self.widget.setObjectName("widget")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setSpacing(3)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.pushButton = QtWidgets.QPushButton(self.widget)
		self.pushButton.setObjectName("pushButton")
		self.horizontalLayout.addWidget(self.pushButton)
		self.label = QtWidgets.QLabel(self.widget)
		self.label.setObjectName("label")
		self.horizontalLayout.addWidget(self.label)
		self.me_says = QtWidgets.QLineEdit(self.widget)
		self.me_says.setObjectName("me_says")
		self.horizontalLayout.addWidget(self.me_says)
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(40, 250, 131, 20))
		self.label_2.setObjectName("label_2")
		
		
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(290, 100, 231, 20))
		self.label_3.setObjectName("label_3")
		
		self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_2.setObjectName("pushButton_2")
		
		self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_3.setObjectName("pushButton_3")
		
		self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_4.setObjectName("pushButton_4")
		
		self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_5.setObjectName("pushButton_5")
		
		self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_6.setObjectName("pushButton_6")
		
		self.robot_says = QtWidgets.QTextEdit(self.centralwidget)
		self.robot_says.setGeometry(QtCore.QRect(240, 240, 271, 121))
		self.robot_says.setObjectName("robot_says")
		
		self.pushButton_7=QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_7.setObjectName("pushButton_7")
		
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 671, 22))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
        
		self.retranslateUi(MainWindow)
		
        
        
        
        
		# 改动:按键的信号与槽连接声明
		self.pushButton.clicked['bool'].connect(self.gui_conversation)#开启对话线程
		self.pushButton_2.clicked['bool'].connect(self.show_log_dialog)#开启登录界面
		self.pushButton_3.clicked['bool'].connect(self.show_bug_dialog)#开启爬虫界面
		self.pushButton_4.clicked['bool'].connect(self.show_advert_dialog)#开启推送界面
		self.pushButton_7.clicked['bool'].connect(self.show_register_dialog)#开启注册界面
		
		
		
		# 结束
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		
	#改动：QMainWindow移至中心,改变大小
	def center_size(self, MainWindow):
		MainWindow.resize(self.screen.width(),self.screen.height())
		size=self.geometry()
		self.move((self.screen.width()-size.width())/2,(self.screen.height()-size.height())/2)
		print(size.width()/2)
		print(size.height()/2)
	#结束
	
	
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.pushButton.setText(_translate("MainWindow", "录音"))
		self.label.setText(_translate("MainWindow", "语音输入"))
		self.label_2.setText(_translate("MainWindow", "语音机器人输出"))
		self.label_3.setText(_translate("MainWindow", "智能语音推送系统"))
		self.pushButton_2.setText(_translate("MainWindow", "登录"))
		self.pushButton_3.setText(_translate("MainWindow", "网络爬虫"))
		self.pushButton_4.setText(_translate("MainWindow", "智能推送"))
		self.pushButton_5.setText(_translate("MainWindow","帮助"))
		self.pushButton_6.setText(_translate("MainWindow","关于我们"))
		self.pushButton_7.setText(_translate("MainWindow","注册"))
		#各个控件的方位
		size=self.geometry()
		self.label_3.setGeometry(QtCore.QRect(int(size.width()*0.5)-131/2, 100, 131, 20))
		self.label_2.setGeometry(QtCore.QRect(int(size.width()*0.5)-131/2, int(size.height()*0.38), 131, 20))
		#self.label.setWordWrap(True)
		#self.label.setAlignment(QtCore.Qt.AlignTop)
		self.frame.setGeometry(QtCore.QRect(int(size.width()*0.5)-460/2, 160, 460, 61))#frame
		self.robot_says.setGeometry(QtCore.QRect(int(size.width()*0.5)-300/2, int(size.height()*0.35)+40, 300,121))
		self.pushButton_2.setGeometry(QtCore.QRect(int(size.width()*0.18)-100/2, int(size.height()*0.2), 100, 75))
		self.pushButton_3.setGeometry(QtCore.QRect(int(size.width()*0.18)-100/2, int(size.height()*0.4), 100, 75))
		self.pushButton_4.setGeometry(QtCore.QRect(int(size.width()*0.18)-100/2, int(size.height()*0.6), 100, 75))
		self.pushButton_5.setGeometry(QtCore.QRect(int(size.width()*0.80)-100/2, int(size.height()*0.2), 100, 75))
		self.pushButton_6.setGeometry(QtCore.QRect(int(size.width()*0.80)-100/2, int(size.height()*0.4), 100, 75))
		self.pushButton_7.setGeometry(QtCore.QRect(int(size.width()*0.18)-100/2, int(size.height()*0.8), 100, 75))
		
	
	def paintEvent(self,event):
		painter=QPainter(self)
		pixmap=QPixmap("/home/pi/Desktop/SRTP2/timg.jpg")
		painter.drawPixmap(self.rect(),pixmap)
		
		
		
		
        
	#改动：后台线程初始化
	def initUI(self):#主界面的语音交互
		self.backend=BackendThread()
		self.backend.update_data_1.connect(self.handleDisplay_me)
		self.backend.update_data_2.connect(self.handleDisplay_robot)
		self.backend.start()
		
	def init_bug_asr_thread(self):
		self.bug_backend=Bug_ASR_BackendThread()
		self.bug_backend.update_data_1.connect(self.bug_dialog.set_asr_display)
		self.bug_backend.start()
		
	def init_bug_thread(self):
		self.bug_backend_2=Bug_BackendThread()
		data=self.bug_dialog.lineEdit.text()#过滤掉噪声
		self.bug_dialog.keywords=data
		if "。" in data:
			data=data.replace("。",'')
			self.bug_dialog.keywords=data
			print(self.bug_dialog.keywords)
		if "搜索" in data: 
			data=data.replace("搜索",'')
			self.bug_dialog.keywords=data
			print(self.bug_dialog.keywords)
		if "查找" in data:
			data=data.replace("查找",'')
			self.bug_dialog.keywords=data
			print(self.bug_dialog.keywords)
		if "查查" in data:
			data=data.replace("查查",'')
			self.bug_dialog.keywords=data
			print(self.bug_dialog.keywords)
		if "检索" in data:
			data=data.replace("检索",'')
			self.bug_dialog.keywords=data
			print(self.bug_dialog.keywords)
		self.bug_backend_2.keyword=self.bug_dialog.keywords
		self.bug_backend_2.update_data_1.connect(self.bug_dialog.str_display)
		self.bug_backend_2.update_data_2.connect(self.bug_dialog.list_display)
		self.bug_backend_2.start()
	
	def init_audio_thread(self):
		self.audio=Audio_Thread()
		self.audio.start()
		
	#结束
	
	
	#改动：槽与显示控件的处理
	def gui_conversation(self):
		self.initUI()
		
	def handleDisplay_robot(self,data):
		self.robot_says.setText(data)
		asr_client.tts_word(data)
		self.init_audio_thread()
		
	
	def handleDisplay_me(self,data):
		self.me_says.setText(data)
		
	
	#结束
	
	#登录对话框运行
	#logForm成员变量的声明在前面
	def show_log_dialog(self):
		self.logForm = userForm()
		self.logForm.okPushBtn.clicked['bool'].connect(self.log_ok_clicked)
		self.logForm.cancelPushBtn.clicked['bool'].connect(self.log_cancel_clicked)
        
		self.logForm.show()
		self.logForm.exec_()
	#结束
	
	#ok
	def log_ok_clicked(self):
		if self.logForm:
			user_id=self.logForm.userNameLineEdit.text().strip()
			user_passwd=self.logForm.passWdLineEdit.text().strip()
			#print(needpassword(user_id)[0].strip())
		if needpassword(user_id).strip() == '["'+user_passwd+'"]':		
			self.__id=user_id
			self.__password=user_passwd
			self.log_flag=1
			self.__email=get_email(self.__id)[2:-2]
			print(self.__email)
			QMessageBox.warning(self,"提示","登录成功",QMessageBox.No|QMessageBox.Yes,QMessageBox.Yes)
			print("登录成功")
		else:
			QMessageBox.warning(self,"提示","登录失败",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
			self.log_flag=0
			print("error")
				
		#print(user_id)
		#print(user_passwd)
		self.logForm.close()
		self.logForm=None
		
	#cancel
	def log_cancel_clicked(self):
		self.logForm.close()
		self.logForm=None
	#结束
	
	
	#爬虫对话框运行
	
	def visit_url(self):
		url=self.bug_dialog.lineEdit_2.text()
		print(url)
		QtGui.QDesktopServices.openUrl(QtCore.QUrl(url))
		
	def insert_data(self):
		text=self.bug_dialog.lineEdit.text()
		dt=datetime.datetime.now(tz=None)
		now_time=dt.strftime("%Y-%m-%d-%H-%M")
		insert_keyword(text,now_time)#插入数据库
	
	def email_sending(self):
		text=self.bug_dialog.textEdit.toPlainText()
		#print(self.email__)
		if self.__email and text:
			#QMessageBox.warning(self,"提示","发送成功",QMessageBox.No|QMessageBox.Yes,QMessageBox.Yes)
			print("发送成功")
			self.mail.email_name=self.__email
			self.mail.content=text
			self.mail.send()
		else:
			if self.__email is None:
				QMessageBox.warning(self,"邮件发送失败","尚未登录",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
			if text is None:
				QMessageBox.warning(self,"邮件发送失败","发送内容为空",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
			#print("邮件发送失败")
		
	def show_bug_dialog(self):
		self.bug_dialog = python_bug_form(self.geometry())
		self.bug_dialog.pushButton.clicked['bool'].connect(self.init_bug_asr_thread)#开启爬虫界面中的语音输入线程
		self.bug_dialog.pushButton_2.clicked['bool'].connect(self.init_bug_thread)#开启爬虫线程
		self.bug_dialog.pushButton_2.clicked['bool'].connect(self.insert_data)#插入数据
		self.bug_dialog.pushButton_3.clicked['bool'].connect(self.visit_url)#访问网址
		self.bug_dialog.pushButton_4.clicked['bool'].connect(self.email_sending)#邮件发送
		self.bug_dialog.show()
		self.bug_dialog.exec_()
	
	#智能推送对话框运行
	def show_advert_dialog(self):
		self.advert_dialog =advert_form(self.geometry())
		self.new_setting_data()#从txt文件中更新信息
		self.advert_dialog.pushButton.clicked['bool'].connect(self.send_setting_data)
		self.advert_dialog.pushButton2.clicked['bool'].connect(self.cancel_butt)
		self.advert_dialog.show()
		self.advert_dialog.exec_()
		
	def send_setting_data(self):
		self.time_spacing[0]=(self.advert_dialog.sp_day.value())*24*60+(self.advert_dialog.sp_hour.value())*60+self.advert_dialog.sp_min.value()
		self.like_threshold[0]=self.advert_dialog.like.value()
		self.decrease_threshold[0]=self.advert_dialog.decrease.value()
		with open("/home/pi/Desktop/SRTP2/set_advert.txt","w") as f:
			f.write(str(self.time_spacing[0])+" "+str(self.like_threshold[0])+" "+str(self.decrease_threshold[0]))
		self.advert_dialog.close()
		self.advert_dialog=None
		
	def new_setting_data(self):
		with open('/home/pi/Desktop/SRTP2/set_advert.txt','r') as f:
			a=f.read()
			b=int(a.split()[0])
			day=b/(24*60)
			hour=(b-day*24*60)/60
			minu=b-day*24*60-hour*60
			self.advert_dialog.sp_day.setValue(day)
			self.advert_dialog.sp_hour.setValue(hour)
			self.advert_dialog.sp_min.setValue(minu)
			self.advert_dialog.like.setValue(int(a.split()[1]))
			self.advert_dialog.decrease.setValue(int(a.split()[2]))

	def cancel_butt(self):
		self.advert_dialog.close()
		self.advert_dialog=None
		
	#注册对话框运行
	def show_register_dialog(self):
		self.register_dialog=register_form(self.geometry())
		self.register_dialog.okPushBtn.clicked['bool'].connect(self.get_reginfo)
		self.register_dialog.show()
		self.register_dialog.exec_()
		
	def get_reginfo(self):
		reg_id=self.register_dialog.userNameLineEdit.text()
		reg_pswd=self.register_dialog.passWdLineEdit.text()
		reg_email=self.register_dialog.emailLineEdit.text()
		new_user(reg_id,reg_pswd,reg_email)
		QMessageBox.warning(self,"提示","注册成功",QMessageBox.No|QMessageBox.Yes,QMessageBox.Yes)
		self.register_dialog.close()
		self.register_dialog=None
		
	def cancel_reg(self):
		self.register_dialog.close()
		self.register_dialog=None
		
