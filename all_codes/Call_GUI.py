#coding:utf-8

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QDesktopWidget
from GUI import Ui_MainWindow
from recoder import record_corr


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        


if __name__ == "__main__":
	record_corr() #为了修复界面的数据流和record的数据流冲突
	app = QApplication(sys.argv)
	win = MyMainWindow()
	win.show()
	sys.exit(app.exec_())


