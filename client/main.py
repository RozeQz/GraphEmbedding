import argparse
import sys

from PyQt5 import QtWidgets, QtGui, uic
from gui.main_window import MainWindow


def main() -> None:

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--algorithm', type=str,
                        dest='algorithm',
                        help="Name of algoritm to use: gamma, pq, annealing")
    parser.add_argument('-g', '--gui', action='store_true')
    # parser.add_argument(type=str, dest='filename',
    #                     help="File containing graph")
    args = parser.parse_args()

    if args.gui:
        app = QtWidgets.QApplication([])
        application = MainWindow()
        # application = uic.loadUi("gui/ui_main_window.ui")
        application.show()

        sys.exit(app.exec())


if __name__ == '__main__':
    main()
