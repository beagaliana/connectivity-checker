from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
import pycurl, validators
from datetime import datetime
import os

class MainPage(QDialog):
	def __init__(self):
		super(MainPage, self).__init__()
		loadUi('WCCT.ui', self)
		#functions
		self.Connect2.clicked.connect(self.check)
		self.Connect2.clicked.connect(self.write2history)
		self.Add.clicked.connect(self.AddInList)
		self.Delete.clicked.connect(self.removeItem)
		self.History.clicked.connect(self.history)
		
		f = open("URLs.txt", "r")
		urls=f.readlines()
		for line in urls:
			words = line.split("\n")
			self.List.addItems(words)
		f.close()

	def AddInList(self):
		url=self.textwebsite.toPlainText()
		self.List.addItem(url)
		f = open("URLs.txt", "a")
		f.write(url+"\n")
		f.close()
	
	def history(self):
		from HistoryPage import HistoryPage
		classHistory=HistoryPage()
		classHistory.exec_()
	
        def delete_history(self):
            if os.path.exists("history.txt"):
                os.remove("history.txt")

        def write2history(self):
                dt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                url=self.List.currentText()
                f = open("history.txt", "a")
                result=self.url_exists()
                f.write(url + ", " + dt + "" + str(result) + "\n")
                f.close()
	
	def removeItem(self):
		index=self.List.currentIndex()
		url=self.List.currentText()
		self.List.removeItem(index)
		with open("URLs.txt", "r+") as f:
			d = f.readlines()
			f.seek(0)
			for i in d:
				if i.strip("\n") != url:
					f.write(i)
			f.truncate()


	def check(self):
	
		#print("WEB CONNECTIVITY CHECKER TOOL")
		if (self.url_exists()):
			self.Status.setText("CONNECTION SUCCESSFUL: website up.")
			#print("CONNECTION SUCCESSFUL: website up.")
		else:
			self.Status.setText("CONNECTION FAILED: website down.")
			#print("CONNECTION FAILED: website down.")


	def url_exists(self):
		"""
	Check if the given URL really exists
	
	"""
		host = self.List.currentText()		
		url="http://"+host
		if validators.url(url):
			c = pycurl.Curl()
			c.setopt(pycurl.NOBODY, True)
			c.setopt(pycurl.FOLLOWLOCATION, False)
			c.setopt(pycurl.CONNECTTIMEOUT, 10)
			c.setopt(pycurl.TIMEOUT, 10)
			c.setopt(pycurl.COOKIEFILE, '')
			c.setopt(pycurl.URL, url)
			try:
				c.perform()
				response_code = c.getinfo(pycurl.RESPONSE_CODE)
				c.close()
				return True if response_code < 400 else False
			except pycurl.error as err:
				errno = err
			except pycurl.error as err1:
				errstr = err1
				raise OSError('An error occurred: {}'.format(errstr))
		else:
			raise ValueError('"{}" is not a valid url'.format(url))

		



if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	ui = MainPage()
	ui.show()
	sys.exit(app.exec_())
