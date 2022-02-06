import sys
from PyQt5.QtWidgets import QApplication
from gui import Twitter

app = QApplication(sys.argv)
window = Twitter()
sys.exit(app.exec_())
