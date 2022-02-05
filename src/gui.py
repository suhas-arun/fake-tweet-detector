import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout


def get_probabilities(_):
    """PLACEHOLDER!"""
    from random import randint
    from time import sleep
    sleep(30)
    return randint(0, 20), randint(0, 20)


class Twitter(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("Account:", self)
        self.bot_chance = QLabel(self)
        self.fake_news_chance = QLabel(self)
        self.input = QLineEdit(self)
        self.submit = QPushButton("Analyse", self)
        self.setWindowTitle("Twitter account checker")

        self.submit.clicked.connect(self.analyse)

        self.vlayout = QVBoxLayout(self)
        hlayout = QHBoxLayout(self)
        hlayout.addWidget(label)
        hlayout.addWidget(self.input)
        self.vlayout.addLayout(hlayout)
        self.vlayout.addWidget(self.submit)
        self.vlayout.addWidget(self.bot_chance)
        self.vlayout.addWidget(self.fake_news_chance)

        self.resize(300, 100)
        self.show()

    def analyse(self):
        search = self.input.text()
        bot_chance, fake_news_chance = get_probabilities(search)
        bot_chance = QLabel("Bot Chance: " + str(bot_chance), self)
        fake_news_chance = QLabel("Fake News Chance: " + str(fake_news_chance), self)
        self.vlayout.addWidget(bot_chance)
        self.vlayout.addWidget(fake_news_chance)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Twitter()
    sys.exit(app.exec_())
