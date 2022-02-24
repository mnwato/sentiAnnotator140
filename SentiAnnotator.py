import os
import sys
import pandas as pd
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5 import QtCore, QtWidgets
from textblob import TextBlob as tb

from guipy import Ui_SentiAnotator140

global i
i = 0

happy_emoji = ":-) :) ;) :o) :] :c) :> =] 8) =) :} :^) :-D :D 8-D 8D x-D X-D =-D =D =-3 =3 :-)) :'-) :') >:P :-P :P X-P x-p :-p :p =p :-b :b >:) >;) >:-) <3".split()

sad_emoji = ">:[ :-( :(  :-c :c :-<  :< :-[ :[ :{ ;( :@ >:( :'-( :'( >:/ :-/ :-.  =/ :L =L :S >.<".split()

# text = df['tweet']
# df = df.drop(columns=['id','username','date','time','replies_count','retweets_count','likes_count','language','sentiment','tweet'])
# df = df.drop(columns=['Signal','handySentiment','tweet'])
# df['Signal'] = None
# df['handySentiment'] = None
# df['tweet'] = text

class MainWindow(QDialog):
	def __init__(self):
		super(MainWindow, self).__init__()


		self.ui = Ui_SentiAnotator140()
		self.ui.setupUi(self)

		

		self.ui.tweetNumber.setValidator(QRegExpValidator(QRegExp(r"\d*\.\d+|\d+")))

		self.ui.displayButton.clicked.connect(self.displayButton_func)
		self.ui.previousButton.clicked.connect(self.previousButton_func)
		self.ui.nextButton.clicked.connect(self.nextButton_func)
		self.ui.buyLabel.clicked.connect(self.buyLabel_func)
		self.ui.sellLabel.clicked.connect(self.sellLabel_func)
		self.ui.label1.clicked.connect(self.label1_func)
		self.ui.label2.clicked.connect(self.label2_func)
		self.ui.label3.clicked.connect(self.label3_func)
		self.ui.label4.clicked.connect(self.label4_func)
		self.ui.label5.clicked.connect(self.label5_func)
		self.ui.finishButton.clicked.connect(self.finishButton_func)
		self.ui.enter.clicked.connect(self.enter_func)
		self.ui.Resetbutton.clicked.connect(self.Resetbutton_func)

		# self.ui.lineEdit.setText('./btc_emoticons.csv')
		# self.ui.lineEdit.setText('./forLabeling.csv')
		self.ui.lineEdit.setText('./nasdaq_emoticons.csv')
		# self.ui.lineEdit.setText('./Stock_Data.csv')




	def enter_func(self):
		global df

		if self.ui.lineEdit.text() != '':
			address = str(self.ui.lineEdit.text())
			address = address.replace(''''\'''', '/')
			try:
				# if address[-3:] == 'csv':
				if os.path.exists(address):
					df = pd.read_csv(address)
					df['handySentiment'] = df['handySentiment'].astype(str)


					self.ui.displayButton.setEnabled(True)
					self.ui.previousButton.setEnabled(True)
					self.ui.nextButton.setEnabled(True)
					self.ui.buyLabel.setEnabled(True)
					self.ui.sellLabel.setEnabled(True)
					self.ui.label1.setEnabled(True)
					self.ui.label2.setEnabled(True)
					self.ui.label3.setEnabled(True)
					self.ui.label4.setEnabled(True)
					self.ui.label5.setEnabled(True)
					self.ui.finishButton.setEnabled(True)
					self.ui.Resetbutton.setEnabled(True)

					self.ui.enter.setEnabled(False)
					self.ui.lineEdit.setEnabled(False)
			except:
				pass

		else:
			pass


	def keyPressEvent(self, event):

		if event.key() == QtCore.Qt.Key_Escape:
			print('last list was {}'.format(i))
			try:
				df.to_csv(self.ui.lineEdit.text(), index=False)
				sys.exit()
			except:
				sys.exit()

		if event.key() == QtCore.Qt.Key_1:
			df['handySentiment'].at[i] = 1
			self.ui.handySentiment.setText(str(df['handySentiment'].at[i]))

		if event.key() == QtCore.Qt.Key_2:
			df['handySentiment'].at[i] = 3
			self.ui.handySentiment.setText(str(df['handySentiment'].at[i]))

		if event.key() == QtCore.Qt.Key_3:
			df['handySentiment'].at[i] = 5
			self.ui.handySentiment.setText(str(df['handySentiment'].at[i]))

		if event.key() == QtCore.Qt.Key_4:
			df['Signal'].at[i] = 'None'
			self.ui.signalLabel.setText('None')
			df['handySentiment'].at[i] = 'None'
			self.ui.handySentiment.setText('None')

	def displayButton_func(self):
		global i, df
		if self.ui.tweetNumber.text() != '':
			i = int(self.ui.tweetNumber.text())
		else:
			i = 0
		self.ui.handySentiment.setText(str(df['handySentiment'].at[i]))
		self.ui.signalLabel.setText(str(df['Signal'].at[i]))
		self.ui.text.setText(df['tweet'].at[i])
		auto_sentiment = (tb(df['tweet'].at[i])).sentiment.polarity   ##### TextBlob #####
		if auto_sentiment>0:
			self.ui.autoLabel.setText(f"<font color='green'>{str(round(auto_sentiment, 1))}</font>")
		else:
			self.ui.autoLabel.setText(f"<font color='red'>{str(round(auto_sentiment, 1))}</font>")


		for emoji in happy_emoji:
			if emoji in df['tweet'].at[i]:
				print(emoji)
				self.ui.emoticon.setStyleSheet("background-color: green")
				pass
				

		for emoji in sad_emoji:
			if emoji in df['tweet'].at[i]:
				print(emoji)
				self.ui.emoticon.setStyleSheet("background-color: red")
				pass


	def previousButton_func(self):
		self.ui.emoticon.setStyleSheet("")

		global i, df
		if i > 0:
			i = i - 1
		else:
			i = 0
		self.ui.handySentiment.setText(str(df['handySentiment'].at[i]))
		self.ui.signalLabel.setText(str(df['Signal'].at[i]))
		self.ui.text.setText(df['tweet'].at[i])
		self.ui.tweetNumber.setText(str(i))
		auto_sentiment = (tb(df['tweet'].at[i])).sentiment.polarity   ##### TextBlob #####
		if auto_sentiment>0:
			self.ui.autoLabel.setText(f"<font color='green'>{str(round(auto_sentiment, 1))}</font>")
		else:
			self.ui.autoLabel.setText(f"<font color='red'>{str(round(auto_sentiment, 1))}</font>")


		for emoji in happy_emoji:
			if emoji in df['tweet'].at[i]:
				print(emoji)
				self.ui.emoticon.setStyleSheet("background-color: green")
				pass
				

		for emoji in sad_emoji:
			if emoji in df['tweet'].at[i]:
				print(emoji)
				self.ui.emoticon.setStyleSheet("background-color: red")
				pass


	def nextButton_func(self):
		self.ui.emoticon.setStyleSheet("")

		global i, df
		if i < len(df)-1:
			i = i + 1
		else:
			i = len(df)-1
		self.ui.handySentiment.setText(str(df['handySentiment'].at[i]))
		self.ui.signalLabel.setText(str(df['Signal'].at[i]))
		self.ui.text.setText(df['tweet'].at[i])
		self.ui.tweetNumber.setText(str(i))
		auto_sentiment = (tb(df['tweet'].at[i])).sentiment.polarity   ##### TextBlob #####
		if auto_sentiment>0:
			self.ui.autoLabel.setText(f"<font color='green'>{str(round(auto_sentiment, 1))}</font>")
		else:
			self.ui.autoLabel.setText(f"<font color='red'>{str(round(auto_sentiment, 1))}</font>")


		for emoji in happy_emoji:
			if emoji in df['tweet'].at[i]:
				print(emoji)
				self.ui.emoticon.setStyleSheet("background-color: green")
				pass
				

		for emoji in sad_emoji:
			if emoji in df['tweet'].at[i]:
				print(emoji)
				self.ui.emoticon.setStyleSheet("background-color: red")
				pass


	def buyLabel_func(self):
		df['Signal'].at[i] = 'Buy'
		self.ui.signalLabel.setText(str(df['Signal'].at[i]))

	def sellLabel_func(self):
		df['Signal'].at[i] = 'Sell'
		self.ui.signalLabel.setText(str(df['Signal'].at[i]))

	def label1_func(self):
		df['handySentiment'].at[i] = 1
		self.ui.handySentiment.setText(str(df['handySentiment'].at[i]))

	def label2_func(self):
		df['handySentiment'].at[i] = 2
		self.ui.handySentiment.setText(str(df['handySentiment'].at[i]))

	def label3_func(self):
		df['handySentiment'].at[i] = 3
		self.ui.handySentiment.setText(str(df['handySentiment'].at[i]))

	def label4_func(self):
		df['handySentiment'].at[i] = 4
		self.ui.handySentiment.setText(str(df['handySentiment'].at[i]))

	def label5_func(self):
		df['handySentiment'].at[i] = 5
		self.ui.handySentiment.setText(str(df['handySentiment'].at[i]))

	def finishButton_func(self):
		print('last list was {}'.format(i))
		df.to_csv(self.ui.lineEdit.text(), index=False)
		sys.exit()

	def Resetbutton_func(self):
		df['Signal'].at[i] = 'None'
		self.ui.signalLabel.setText('None')
		df['handySentiment'].at[i] = 'None'
		self.ui.handySentiment.setText('None')

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)  # enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)  # use highdpi icons

# main
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setWindowTitle("SentiAnotator140")
widget.setMinimumSize(550, 320)
widget.setMaximumSize(550, 320)
widget.show()
try:
	print('last list was {}'.format(i))
	sys.exit(app.exec_())

except:
	pass