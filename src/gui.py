from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from process_data import accountBotTest
import threading

SIZE = 36


class Twitter(QWidget):
    def __init__(self):
        super().__init__()
        self.f = QtGui.QFont()
        self.f.setPixelSize(SIZE)

        label = QLabel("Enter an account to be analysed:", self)
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.bot_chance = QLabel()
        self.fake_news_chance = QLabel(self)
        self.positivity = QLabel(self)
        self.label2 = QLabel(self)
        self.input = QLineEdit(self)
        self.submit = QPushButton("Analyse", self)
        self.loading = QLabel(self)
        self.loading.resize(100, 100)
        self.loading_gif = QtGui.QMovie("../img/loading.gif")

        self.setWindowTitle("Twitter account checker")
        self.loading.setAlignment(QtCore.Qt.AlignCenter)
        self.loading.setMovie(self.loading_gif)
        self.loading.hide()

        self.submit.clicked.connect(self.analyse)
        self.loading.resize(150, 150)
        self.loading_gif.setScaledSize(QtCore.QSize(150, 150))

        self.vlayout = QVBoxLayout(self)
        self.vlayout.setAlignment(QtCore.Qt.AlignTop)
        self.vlayout.setSpacing(20)
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.input)
        hlayout.addWidget(self.submit)
        hlayout2 = QHBoxLayout()
        hlayout2.setAlignment(QtCore.Qt.AlignLeft)
        hlayout2.addWidget(self.label2)
        hlayout2.addWidget(self.positivity)

        self.label3 = QLabel("Bot Probability:")
        hlayout3 = QHBoxLayout()
        hlayout3.addWidget(self.label3)
        hlayout3.addWidget(self.bot_chance)
        hlayout3.setAlignment(QtCore.Qt.AlignLeft)

        self.label4 = QLabel("Fake News Probability:")
        hlayout4 = QHBoxLayout()
        hlayout4.addWidget(self.label4)
        hlayout4.addWidget(self.fake_news_chance)
        hlayout4.setAlignment(QtCore.Qt.AlignLeft)
        self.label4.hide()
        self.fake_news_chance.hide()

        self.vlayout.addWidget(label)
        self.vlayout.addLayout(hlayout)
        self.vlayout.addLayout(hlayout3)
        self.vlayout.addLayout(hlayout4)
        self.vlayout.addLayout(hlayout2)
        self.label2.hide()
        self.positivity.hide()
        self.setFont(self.f)
        self.resize(1200, 500)
        self.label2.setText("Positivity Rating:")
        self.loading.move(self.width() // 2 - 75, int(self.height() * 2 / 3) - 60)
        self.label3.hide()
        self.bot_chance.hide()
        self.show()

    def get_probabilities(self, search):
        from random import randint

        try:
            font_style = "font-size: 36px"
            sentiment, bot, fakeness = accountBotTest(search)
            bot = min(bot, 99)
            self.bot_chance.setText("{:.1f}".format(bot) + "%")
            self.positivity.setText(sentiment)
            if bot < 50:
                self.bot_chance.setStyleSheet(
                    f"color: rgb({bot/50*255}, 255, 0); {font_style}"
                )
            else:
                self.bot_chance.setStyleSheet(
                    f"color: rgb(255, {(100-bot)/50*255}, 0); {font_style}"
                )

            self.fake_news_chance.setText("{:.1f}".format(fakeness) + "%")
            if fakeness < 50:
<<<<<<< HEAD
                self.fake_news_chance.setStyleSheet(
                    f"color: rgb({bot/50*255}, 255, 0); {font_style}"
                )
            else:
                self.fake_news_chance.setStyleSheet(
                    f"color: rgb(255, {(100-bot)/50*255}, 0); {font_style}"
                )
=======
                self.fake_news_chance.setStyleSheet(f"color: rgb({bot/50*255}, 255, 0); {font_style}")
            else:
                self.fake_news_chance.setStyleSheet(f"color: rgb(255, {(100-bot)/50*255}, 0); {font_style}")

>>>>>>> 0bf6ff5474bce6257b2c92f35062159b4ee5172b

            font_style = "font-size: 36px"

            if sentiment == "Very Negative":
                self.positivity.setStyleSheet("color: rgb(255, 0, 0);" + font_style)
            elif sentiment == "Slightly Negative":
                self.positivity.setStyleSheet("color: rgb(255, 60, 0);" + font_style)
            elif sentiment == "Slightly Positive":
                self.positivity.setStyleSheet("color: rgb(111, 200, 0);" + font_style)
            elif sentiment == "Very Positive":
                self.positivity.setStyleSheet("color: rgb(0, 255, 0);" + font_style)
            else:
                self.positivity.setStyleSheet("color: rgb(255, 255, 0);" + font_style)

        except BaseException as e:
            print(e)
            self.bot_chance.setText("Error: User does not exist!")

        self.loading_gif.stop()
        self.loading.hide()

        self.fake_news_chance.setText(str(randint(0, 100)))
        self.bot_chance.show()
        self.fake_news_chance.show()
        self.label2.show()
        self.positivity.show()
        self.label3.show()
        self.bot_chance.show()
        self.label4.show()

    def analyse(self):
        self.fake_news_chance.hide()
        self.label4.hide()
        self.bot_chance.hide()
        self.label2.hide()
        self.label3.hide()
        self.bot_chance.hide()
        self.loading.show()
        self.positivity.hide()
        self.loading_gif.start()
        search = self.input.text()
        thread = threading.Thread(target=self.get_probabilities, args=[search])
        thread.start()
