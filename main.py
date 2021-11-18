from PyQt5.QtGui import QPainter, QPen

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
import random
import sys
from ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.draw)
        self.draw_flag = False

    def draw(self):
        self.draw_flag = True
        self.update()

    def paintEvent(self, event):
        if self.draw_flag:
            painter = QPainter(self)
            self.drawCircle(painter)
            painter.end()

            self.draw_flag = False

    def drawCircle(self, painter):
        painter.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
        pos_x = random.randrange(200, 600)
        pos_y = random.randrange(100, 400)
        d = random.randrange(100, 300)
        painter.drawEllipse(pos_x, pos_y, d, d)


App = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(App.exec())
