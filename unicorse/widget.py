import sys
from PyQt6.QtCore import QSize, Qt, QRect
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lowadi")
        self.setBaseSize(QSize(300, 300))  # Установка размера основного окна

        button1 = QPushButton()
        button1.setFixedSize(QSize(35, 35))  # Установка размера кнопки
        button1.setGeometry(QRect(5, 5, 25, 25))
        button1.setIcon(
            QIcon(r'C:\Users\user\PycharmProjects\InnokentiyHomeWorker\unicorse\images\reproduction_v1713961017.png'))

        button2 = QPushButton()
        button2.setFixedSize(QSize(35, 35))  # Установка размера кнопки
        button2.setIcon(
            QIcon(r'C:\Users\user\PycharmProjects\InnokentiyHomeWorker\unicorse\images\male_v1713961017.png'))

        button3 = QPushButton()
        button3.setFixedSize(QSize(35, 35))  # Установка размера кнопки
        button3.setIcon(
            QIcon(r'C:\Users\user\PycharmProjects\InnokentiyHomeWorker\unicorse\images\selle-classique-3x_v1713961018.png'))

        # Создание вертикального лейаута
        layout = QVBoxLayout()
        # layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Центрирование кнопок
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        # Создание контейнера и установка лейаута
        container = QWidget()
        # container.setLayout(layout)

        self.setCentralWidget(container)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
