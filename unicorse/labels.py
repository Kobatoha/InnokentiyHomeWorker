from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QRect, Qt


def create_labels(parent):
    font = QFont()
    font.setPointSize(10)
    font.setBold(False)
    font.setFamily("Segoe UI")

    horses = QLabel('Horses', parent)
    horses.setGeometry(QRect(140, 160, 130, 20))
    horses.setFont(font)
    horses.setObjectName('horses_label')

    childbirth = QLabel('Жеребята', parent)
    childbirth.setGeometry(QRect(140, 180, 130, 20))
    childbirth.setFont(font)
    childbirth.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft)
    childbirth.setObjectName('childbirth')

    get_mating = QLabel('Случки get', parent)
    get_mating.setGeometry(QRect(140, 200, 130, 20))
    get_mating.setFont(font)
    get_mating.setObjectName('get_mating')

    post_mating = QLabel('Случки post', parent)
    post_mating.setGeometry(QRect(140, 220, 130, 20))
    post_mating.setFont(font)
    post_mating.setObjectName('post_mating')

    stable = QLabel('Стойла', parent)
    stable.setGeometry(QRect(140, 240, 130, 20))
    stable.setFont(font)
    stable.setObjectName('stable')

    competitions = QLabel('Соревнования', parent)
    competitions.setGeometry(QRect(140, 260, 130, 20))
    competitions.setFont(font)
    competitions.setObjectName('competitions')
