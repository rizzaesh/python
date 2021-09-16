import sys

from PyQt5.QtWidgets import (QWidget,
	QApplication,QHBoxLayout,QVBoxLayout,QGridLayout,
	QPushButton,QLabel,QLineEdit)
from PyQt5.QtCore import QTimer
# from timer import Page
from playsound import playsound 


class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()
		self.cunter = 0
		self.p = 0

	def init_ui(self):
		self.label = QLabel("set timer")
		self.name = QLineEdit()
		self.name.returnPressed.connect(self.stop)
		self.setNameButtom = QPushButton("push name")

		# OkButtom = QPushButton("Ok!")
		self.setNameButtom.clicked.connect(self.stop)
		self.setNameButtom.hide()
		# CancelButtom = QPushButton("Cancel!") 

		h = QVBoxLayout()
		# h.addStretch()
		h.addWidget(self.label)
		h.addWidget(self.name)
		
		v = QVBoxLayout()
		v.addStretch()
		v.addLayout(h)
		v.addWidget(self.setNameButtom)

		self.setLayout(v)
		self.setWindowTitle("Horizontal layout")
		self.show()
	def OK(self):
		self.cunter += 1
		self.label.setText(f"{self.cunter}")
		# self.setNameButtom.setText(f"{self.cunter}")
		if self.cunter == self.p:
			self.timer.stop()
			self.cunter = 0
			playsound('./1121.wav')

	def stop(self):
		if self.name.text() != "":
			self.p = int(self.name.text())
		else: self.p = int(10)
		self.timer = QTimer()
		self.timer.timeout.connect(self.OK)
		self.timer.start(1000)



if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec_())

