from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi

class HistoryPage(QDialog):
	def __init__(self):
		super(HistoryPage, self).__init__()
		loadUi('/Users/soufianetai/Desktop/AGH/Python/GUI/HistoryGUI.ui', self)
		#functions
		f = open("/Users/soufianetai/Desktop/AGH/Python/GUI/history.txt", "r")
		urls=f.read()
		self.History.setPlainText(urls)
		
		
	
