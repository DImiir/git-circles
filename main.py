import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from random import randint
from PyQt6.QtGui import QPainter, QColor
from style_for import Ui_MainWindow


class Painting_circles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_btn.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw_circle()
            self.qp.end()

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self):
        radius = randint(1, 600)
        self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        self.qp.drawEllipse(int(randint(1, 800) - radius / 2), int(randint(1, 600) - radius / 2), radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Painting_circles()
    ex.show()
    sys.exit(app.exec())
