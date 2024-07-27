import sys
from PyQt6.QtWidgets import QApplication
from ui import MyApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
