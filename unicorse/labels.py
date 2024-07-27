from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QRect, Qt


def create_labels(parent):
    label = QLabel('Жеребята', parent)
    label.setGeometry(QRect(140, 10, 131, 16))
    font = QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(10)
    font.setBold(True)
    label.setFont(font)
    label.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft)
    label.setObjectName('label')

    label_2 = QLabel('Случки in', parent)
    label_2.setGeometry(QRect(140, 30, 131, 16))
    font.setPointSize(10)
    font.setBold(True)
    label_2.setFont(font)
    label_2.setObjectName('label_2')

    label_3 = QLabel('Случки out', parent)
    label_3.setGeometry(QRect(140, 50, 131, 16))
    font.setPointSize(10)
    font.setBold(True)
    label_3.setFont(font)
    label_3.setObjectName('label_3')

    label_4 = QLabel('Стойла', parent)
    label_4.setGeometry(QRect(140, 70, 131, 16))
    font.setPointSize(10)
    font.setBold(True)
    label_4.setFont(font)
    label_4.setObjectName('label_4')

    label_5 = QLabel('Соревнования', parent)
    label_5.setGeometry(QRect(140, 90, 131, 16))
    font.setPointSize(10)
    font.setBold(True)
    label_5.setFont(font)
    label_5.setObjectName('label_5')
