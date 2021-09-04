# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QMainWindow
from PyQt5.QtWidgets import QMessageBox
import jdatetime
import os
from PyQt5.QtCore import QTimer, QTime, Qt
import subprocess
# from untitledback import Ui_MainWindow
class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(913, 534)
        MainWindow.setStyleSheet(
                    '''*{
                background-image: url(./qq.jpg);
                    }''')

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        layout = QVBoxLayout()
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 191, 61))
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet('''*{
            color: 'black';
            font-family: 'Arial';
            font-weight: 900;
            font-size: 22px;
            border-radius: 12px;
            background: transparent;
            background-color: rgba(100, 100, 100, 0);


        }''')
        self.timer = QTimer(self)
        layout.addWidget(self.label_9)

        self.timer.timeout.connect(self.timerr)
        self.timer.start(1000)
        # self.add_on_5()
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 300, 191, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(
        '''*{
            color: 'black';
            font-family: 'Arial';
            font-weight: 900;
            font-size: 22px;
            border-radius: 12px;
            background: transparent;
            background-color: rgba(100, 100, 100, 0.4);

        }
        *:hover{
            color: 'black';
            font-family: 'Arial';
            font-weight: 900;
            font-size: 22px;
            border-radius: 12px;
            background: transparent;
            background-color: rgba(100, 100, 100, 0.9);
        }''')
        self.pushButton_hist = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_hist.setGeometry(QtCore.QRect(700,360,191,40))
        self.pushButton_hist.setObjectName("pushButton_hist")
        self.pushButton_hist.setStyleSheet(
        '''*{
            color: 'black';
            font-family: 'Arial';
            font-weight: 900;
            font-size: 22px;
            border-radius: 12px;
            background: transparent;
            background-color: rgba(100, 100, 100, 0.4);

        }
        *:hover{
            color: 'black';
            font-family: 'Arial';
            font-weight: 900;
            font-size: 22px;
            border-radius: 12px;
            background: transparent;
            background-color: rgba(100, 100, 100, 0.9);
        }''')
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10,70,110,30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet(
        '''*{
            color: 'black';
            font-family: 'Arial';
            font-weight: 200;
            font-size: 12px;
            border-radius: 12px;
            background: transparent;
            background-color: rgba(100, 100, 100, 0.4);

        }
        *:hover{
            color: 'black';
            font-family: 'Arial';
            font-weight: 400;
            font-size: 14px;
            border-radius: 12px;
            background: transparent;
            background-color: rgba(100, 100, 100, 0.9);
        }''')
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 255, 191, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet(
        '''*{
            color: 'black';
            font-family: 'Arial';
            font-size: 22px;
            border-radius: 12px;
            font-weight: 900;
            background: transparent;
            background-color: rgba(100, 100, 100, 0.4);

        }
        *:hover{
            color: 'black';
            font-family: 'Arial';
            font-size: 22px;
            border-radius: 12px;
            font-weight: 900;
            background: transparent;
            background-color: rgba(100, 100, 100, 0.9);
        }''')
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(700, 180, 191, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet(
        '''*{
            color: 'black';
            font-family: 'Arial';
            font-size: 22px;
            border-radius: 12px;
            font-weight: 900;
            background: transparent;
            background-color: rgba(100, 100, 100, 0.4);

        }
        *:hover{
            color: 'black';
            font-family: 'Arial';
            font-size: 22px;
            font-weight: 900;
            border-radius: 12px;
            background: transparent;
            background-color: rgba(100, 100, 100, 0.9);
        }''')
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(700, 100, 191, 61))
        self.label.setObjectName("label")
        self.label.setStyleSheet(
                    '''*{
                color: 'black';
                height: 60px;
                font-family: 'Arial';
                font-size: 32px;
                font-weight: 500;
                border-radius: 12px;
                margin: 2px 2px;
                padding: 6px;
                background: transparent;
                background-color: rgba(100, 100, 100, 0.3); 
                    }''')
        # self.labeldate = QtWidgets.QLabel(self.centralwidget)
        # self.labeldate.setGeometry(QtCore.QRect(100, 100, 191, 161))
        # self.labeldate.setObjectName("labeldate")
        # self.labeldate.setStyleSheet(
        #             '''*{
        #         color: 'black';
        #         height: 60px;
        #         font-family: 'Arial';
        #         font-size: 32px;
        #         border-radius: 12px;
        #         margin: 2px 2px;
        #         padding: 6px;
        #         background: transparent; 
        #             }''')
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 0, 261, 121))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet(
                    '''*{
                color: 'black';
                height: 60px;
                font-family: 'Arial';
                font-size: 32px;
                border-radius: 12px;
                margin: 2px 2px;
                padding: 1px;
                background: transparent; 
                    }''')
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10,470,70,40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet(
        '''*{
            color: 'black';
            font-family: 'Arial';
            font-size: 12px;
            border-radius: 12px;
            font-weight: 200;
            background: transparent;
            background-color: rgba(250, 100, 100, 0.7);

        }
        *:hover{
            color: 'black';
            font-family: 'Arial';
            font-size: 12px;
            font-weight: 300;
            border-radius: 12px;
            background: transparent;
            background-color: rgba(250, 100, 100, 0.9);
        }''')
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 913, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def add_on(self):
        os.startfile("./add_user\\add_user.exe")
    def add_on_2(self):
        os.startfile("./search\\search.exe")
    def add_on_3(self):
        os.startfile("./upset\\upset.exe")
    def timerr(self):
        time = jdatetime.datetime.now()
        self.label_9.setText(f'{time.hour} : {time.minute} : {time.second}')

    def add_on_4(self):
        # self.pushButton.hide()
        name, done1 = QtWidgets.QInputDialog.getText(
            self, 'Input Dialog', 'کد عبور خود را وارد کنید')
        if name == '9904':     
            MainWindow.setWindowTitle("مدرسه دکتر علی شریعتی-خوش آمدید آقای باخدا")
            self.pushButton.setText("اضافه کردن ")
            self.pushButton.clicked.connect(self.add_on)
            self.pushButton_2.setText("جست و جو ")
            self.pushButton_2.clicked.connect(self.add_on_2)
            self.pushButton_5.hide()
        else:
            pass
    def add_on_5(self):
        os.startfile("./hist\\hist.exe")
    def onClicked(self, item):

        QMessageBox.information(self, "ارتباط", "برای اطلاعات بیشتر با 09036349122 تماس بگیرید.")
    def add_on_inactive(self, item):
  
        QMessageBox.information(self," ", "متاسفانه اجازه‌ی ورود ندارید.")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "مدرسه دکتر علی شریعتی-ورود به عنوان میهمان"))
        self.pushButton.setText(_translate("MainWindow", "اضافه کردن"))
        self.pushButton.clicked.connect(self.add_on_inactive)
        self.pushButton_2.setText(_translate("MainWindow", "جست و جو "))
        self.pushButton_2.clicked.connect(self.add_on_inactive)
        self.pushButton_3.setText(_translate("MainWindow", "حضور و غیاب"))
        self.pushButton_3.clicked.connect(self.add_on_3)
        self.pushButton_5.setText(_translate("MainWindow","ورود به عنوان ادمین"))
        self.pushButton_5.clicked.connect(self.add_on_4)
        self.pushButton_hist.setText(_translate("MainWindow","تاریخچه"))
        self.pushButton_hist.clicked.connect(self.add_on_5)
        self.label.setText(_translate("MainWindow", 'شریعتی'))
        self.label_2.setText(_translate("MainWindow", "                 به نام خدا"))
        self.pushButton_4.setText(_translate("MainWindow","ارتباط با ما"))
        self.pushButton_4.clicked.connect(self.onClicked)
        # self.labeldate.setText(_translate("MainWindow",""))


    # def time(self):

        # time = datetime.datetime.now()
        # self.labeldate.setText(f"تاریخ امروز: {time.day}/{time.month}")
if __name__ == "__main__":
    import sys
    import json
    # with open('name.json','r') as nameofschools:
    # 	nameofschools = json.load(nameofschools)

    # nameofschool = nameofschools["name"]
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # ui.time()
    MainWindow.show()

    sys.exit(app.exec_())
