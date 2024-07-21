import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QToolBar, QAction, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon

class SimpleBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        self.back_button = QAction(QIcon('back.png'), "Atrás", self)
        self.back_button.triggered.connect(self.browser.back)

        self.forward_button = QAction(QIcon('forward.png'), "Adelante", self)
        self.forward_button.triggered.connect(self.browser.forward)

        self.reload_button = QAction(QIcon('reload.png'), "Recargar", self)
        self.reload_button.triggered.connect(self.browser.reload)

        self.toolbar = QToolBar()
        self.toolbar.setStyleSheet("""
            QToolBar {
                background: #333;
                padding: 5px;
            }
            QLineEdit {
                background: #555;
                color: white;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton, QAction {
                color: white;
                background: #444;
                border-radius: 5px;
                padding: 5px;
            }
        """)

        self.toolbar.addAction(self.back_button)
        self.toolbar.addAction(self.forward_button)
        self.toolbar.addAction(self.reload_button)
        self.toolbar.addWidget(self.url_bar)

        self.addToolBar(self.toolbar)

        layout = QVBoxLayout()
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.browser.urlChanged.connect(self.update_url_bar)

        self.setWindowTitle("MarWeb")
        self.showMaximized()

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))

    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleBrowser()
    sys.exit(app.exec_())
