from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QRect, QSize
from functions import *


def create_buttons(parent):
    driver_brave = QPushButton('', parent)
    driver_brave.setGeometry(QRect(250, 10, 40, 40))
    driver_brave.setAutoFillBackground(False)
    driver_brave.setIcon(QIcon('images/icons8-brave-48.png'))
    driver_brave.setIconSize(QSize(30, 30))
    driver_brave.setObjectName('driver_brave')
    driver_brave.clicked.connect(handle_driver_brave)

    driver_chrome = QPushButton('', parent)
    driver_chrome.setGeometry(QRect(300, 10, 40, 40))
    driver_chrome.setIcon(QIcon('images/icons8-chrome-48.png'))
    driver_chrome.setIconSize(QSize(30, 30))
    driver_chrome.clicked.connect(handle_driver_chrome)

    female_andalus = QPushButton('andalusian', parent)
    female_andalus.setGeometry(QRect(10, 10, 100, 40))
    female_andalus.setIcon(QIcon('images/reproduction_v1713961017.png'))
    female_andalus.setIconSize(QSize(30, 30))
    female_andalus.setObjectName('female_andalus')
    female_andalus.clicked.connect(handle_female_andalus)

    male_andalus = QPushButton('andalusian', parent)
    male_andalus.setGeometry(QRect(10, 60, 100, 40))
    male_andalus.setIcon(QIcon('images/male_v1713961017.png'))
    male_andalus.setIconSize(QSize(30, 30))
    male_andalus.setObjectName('male_andalus')
    male_andalus.clicked.connect(handle_male_andalus)

    unicorn_andalus = QPushButton('andalusian', parent)
    unicorn_andalus.setGeometry(QRect(10, 110, 100, 40))
    unicorn_andalus.setIcon(QIcon('images/corne_v1713961018.png'))
    unicorn_andalus.setIconSize(QSize(30, 30))
    unicorn_andalus.setObjectName('unicorn_andalus')
    unicorn_andalus.clicked.connect(handle_unicorn_andalus)

    competitions_andalus = QPushButton('andalusian', parent)
    competitions_andalus.setGeometry(QRect(10, 160, 100, 40))
    competitions_andalus.setIcon(QIcon('images/specialisation-classique_v1713961017.png'))
    competitions_andalus.setIconSize(QSize(30, 30))
    competitions_andalus.setObjectName('competitions_andalus')
    competitions_andalus.clicked.connect(handle_competitions_andalus)

    blup_andalus = QPushButton('andalusian', parent)
    blup_andalus.setGeometry(QRect(10, 210, 100, 40))
    blup_andalus.setIcon(QIcon('images/trophee_v1713961017.png'))
    blup_andalus.setIconSize(QSize(30, 30))
    blup_andalus.setObjectName('blup_andalus')
    blup_andalus.clicked.connect(handle_blup_andalus)

    female_marshadore = QPushButton('marsha', parent)
    female_marshadore.setGeometry(QRect(10, 260, 100, 40))
    female_marshadore.setIcon(QIcon('images/reproduction_v1713961017.png'))
    female_marshadore.setIconSize(QSize(30, 30))
    female_marshadore.setObjectName('female_marshadore')
    female_marshadore.clicked.connect(handle_female_marshadore)

    male_marshadore = QPushButton('marsha', parent)
    male_marshadore.setGeometry(QRect(10, 310, 100, 40))
    male_marshadore.setIcon(QIcon('images/male_v1713961017.png'))
    male_marshadore.setIconSize(QSize(30, 30))
    male_marshadore.setObjectName('male_marshadore')
    male_marshadore.clicked.connect(handle_male_marshadore)