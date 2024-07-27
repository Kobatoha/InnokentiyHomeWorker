from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtCore import QRect, Qt


def create_line_edits(parent):
    line_edit = QLineEdit(parent)
    line_edit.setGeometry(QRect(280, 10, 61, 20))
    line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
    line_edit.setReadOnly(True)
    line_edit.setObjectName('lineEdit')
    line_edit.setText('1000')

    line_edit_2 = QLineEdit(parent)
    line_edit_2.setGeometry(QRect(280, 30, 61, 20))
    line_edit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
    line_edit_2.setReadOnly(True)
    line_edit_2.setObjectName('line_edit_2')
    line_edit_2.setText('25')

    line_edit_3 = QLineEdit(parent)
    line_edit_3.setGeometry(QRect(280, 50, 61, 20))
    line_edit_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
    line_edit_3.setReadOnly(True)
    line_edit_3.setObjectName('line_edit_3')
    line_edit_3.setText('25')

    line_edit_4 = QLineEdit(parent)
    line_edit_4.setGeometry(QRect(280, 70, 61, 21))
    line_edit_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
    line_edit_4.setReadOnly(True)
    line_edit_4.setObjectName('lineEdit_4')
    line_edit_4.setText('25')

    line_edit_5 = QLineEdit(parent)
    line_edit_5.setGeometry(QRect(280, 90, 61, 21))
    line_edit_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
    line_edit_5.setReadOnly(True)
    line_edit_5.setObjectName('lineEdit_5')
    line_edit_5.setText('25')
