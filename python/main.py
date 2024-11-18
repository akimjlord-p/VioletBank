import sys
from PyQt6.QtWidgets import QApplication
from ui.MainWindow import MainWindow
from core.db_func import initiate_db, is_db_empty


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    if is_db_empty():
        initiate_db()
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

