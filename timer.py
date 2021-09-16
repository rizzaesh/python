from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# Creating a window

class Page(QWidget):
	"""docstring for Page"""
	def __init__(self, parent = None):
		super(Page, self).__init__(parent)

		my_label = QLabel("text dddddddddddddddddddddddddd")
		layout = QVBoxLayout()

		layout.addWidget(my_label)
		layout.addStretch()
		MainLayout = QGridLayout()
		MainLayout.addLayout(layout, 0, 1)

		self.setLayout(MainLayout)
		self.setWindowTitle("a0")
		# self.setFixedSize(400, 200)
# if __name__ == '__main__':
# 	import sys

# 	app = QApplication(sys.argv)

# 	window = Page()
# 	window.show()
# 	sys.exit(app.exec_())
