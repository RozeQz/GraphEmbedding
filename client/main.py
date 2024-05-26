import sys

from PyQt5 import QtWidgets
from gui.main_window import MainWindow


def main() -> None:

    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
