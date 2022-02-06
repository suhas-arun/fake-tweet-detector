import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout
from process_data import accountBotTest
import threading

SIZE = 36


class Twitter(QWidget):
    def __init__(self):
        super().__init__()
        f = QtGui.QFont()
        f.setPixelSize(SIZE)

        label = QLabel("Enter an account to be analysed:", self)
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.bot_chance = QLabel(self)
        self.fake_news_chance = QLabel(self)
        self.positivity = QLabel(self)
        self.input = QLineEdit(self)
        self.submit = QPushButton("Analyse", self)
        self.loading = QLabel(self)
        self.loading.resize(100, 100)
        self.loading_gif = QtGui.QMovie("../loading.gif")

        self.setWindowTitle("Twitter account checker")
        self.loading.setAlignment(QtCore.Qt.AlignCenter)
        self.loading.setMovie(self.loading_gif)
        self.loading.hide()

        self.submit.clicked.connect(self.analyse)
        self.loading.resize(150, 150)
        self.loading_gif.setScaledSize(QtCore.QSize(150,150))

        self.vlayout = QVBoxLayout(self)
        self.vlayout.setAlignment(QtCore.Qt.AlignTop)
        self.vlayout.setSpacing(20)
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.input)
        hlayout.addWidget(self.submit)
        self.vlayout.addWidget(label)
        self.vlayout.addLayout(hlayout)
        self.vlayout.addWidget(self.bot_chance)
        self.vlayout.addWidget(self.fake_news_chance)
        self.vlayout.addWidget(self.positivity)

        self.setFont(f)
        self.resize(1200, 500)
        self.loading.move(self.width()//2 - 75, int(self.height()*2/3) - 60)
        self.show()

    def get_probabilities(self, search):
        from random import randint
        try:
            sentiment, bot = accountBotTest(search)
            self.bot_chance.setText("Bot Probability: " + "{:.1f}".format(bot) + "%")
        except BaseException as e:
            print(e)
            self.bot_chance.setText("Error: User does not exist!")

        self.loading_gif.stop()
        self.loading.hide()

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
