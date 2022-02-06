import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout
import threading


class Twitter(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("Account:", self)
        self.bot_chance = QLabel(self)
        self.fake_news_chance = QLabel(self)
        self.input = QLineEdit(self)
        self.submit = QPushButton("Analyse", self)
        self.loading = QLabel(self)
        self.loading.resize(100, 100)
        self.loading_gif = QtGui.QMovie("../loading.gif")

        self.setWindowTitle("Twitter account checker")
        self.loading.setAlignment(QtCore.Qt.AlignCenter)
        self.loading.setMovie(self.loading_gif)

        self.submit.clicked.connect(self.analyse)
        self.submit.clicked.connect(self.loading_gif.start)
        self.submit.clicked.connect(self.analyse)

        self.vlayout = QVBoxLayout(self)
        hlayout = QHBoxLayout()
        hlayout.addWidget(label)
        hlayout.addWidget(self.input)
        self.vlayout.addLayout(hlayout)
        self.vlayout.addWidget(self.submit)
        self.vlayout.addWidget(self.loading)
        self.vlayout.addWidget(self.bot_chance)
        self.vlayout.addWidget(self.fake_news_chance)

        self.resize(300, 100)
        self.show()

    def get_probabilities(self, search):
        from random import randint
        from time import sleep

        sleep(2)
        self.loading_gif.stop()
        self.loading.hide()
        self.bot_chance.setText("Bot Probability: " + str(randint(0, 100)))
        self.fake_news_chance.setText("Fake News Probability: " + str(randint(0, 100)))
        self.bot_chance.show()
        self.fake_news_chance.show()

    def analyse(self):
        self.fake_news_chance.hide()
        self.bot_chance.hide()
        self.loading.show()
        self.loading_gif.start()
        search = self.input.text()
        thread = threading.Thread(target=self.get_probabilities, args=[search])
        thread.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Twitter()
    sys.exit(app.exec_())
