from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.web_view = QWebEngineView()
        self.setCentralWidget(self.web_view)

        self.web_view.load(QUrl('http://10.0.0.6:8000/home/'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
