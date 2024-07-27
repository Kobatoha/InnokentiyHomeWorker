from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtCore import QRect, Qt


def create_line_edits(parent):
    horses_edit = QLineEdit(parent)
    horses_edit.setGeometry(QRect(280, 160, 60, 20))
    horses_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
    horses_edit.setReadOnly(True)
    horses_edit.setObjectName('horses_edit')
    horses_edit.setText('1000')

    childbirth_edit = QLineEdit(parent)
    childbirth_edit.setGeometry(QRect(280, 180, 60, 20))
    childbirth_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
    childbirth_edit.setReadOnly(True)
    childbirth_edit.setObjectName('childbirth_edit')
    childbirth_edit.setText('75')

    get_mating_edit = QLineEdit(parent)
    get_mating_edit.setGeometry(QRect(280, 200, 60, 20))
    get_mating_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
    get_mating_edit.setReadOnly(True)
    get_mating_edit.setObjectName('get_mating_edit')
    get_mating_edit.setText('30')

    post_mating_edit = QLineEdit(parent)
    post_mating_edit.setGeometry(QRect(280, 220, 60, 20))
    post_mating_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
    post_mating_edit.setReadOnly(True)
    post_mating_edit.setObjectName('post_mating_edit')
    post_mating_edit.setText('33')

    stable_edit = QLineEdit(parent)
    stable_edit.setGeometry(QRect(280, 240, 60, 20))
    stable_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
    stable_edit.setReadOnly(True)
    stable_edit.setObjectName('stable_edit')
    stable_edit.setText('1')

    competition_edit = QLineEdit(parent)
    competition_edit.setGeometry(QRect(280, 260, 60, 20))
    competition_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
    competition_edit.setReadOnly(True)
    competition_edit.setObjectName('competition_edit')
    competition_edit.setText('25')
