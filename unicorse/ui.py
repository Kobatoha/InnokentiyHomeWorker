from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMainWindow, QProgressBar, QLineEdit, QLabel, QMenuBar
from PyQt6.QtGui import QIcon, QPixmap, QFont
from PyQt6.QtCore import QRect, QSize, Qt
from buttons import create_buttons
from labels import create_labels
from line_edits import create_line_edits


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.driver = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Unicorse')
        self.resize(350, 410)

        with open('css/style.css', 'r') as f:
            self.setStyleSheet(f.read())

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        create_buttons(central_widget, MyApp)

        create_labels(central_widget)

        create_line_edits(central_widget)

        progress_bar = QProgressBar(self)
        progress_bar.setGeometry(QRect(150, 120, 181, 16))
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        progress_bar.setFont(font)
        progress_bar.setProperty("value", 22)
        progress_bar.setObjectName("progress_bar")

