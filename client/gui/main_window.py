from PyQt5.QtGui import QFont, QFontDatabase, QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow

from gui.ui_main_window import Ui_MainWindow

from gui.test_page import TestPage
from gui.profile_page import ProfilePage
from gui.main_page import MainPage


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.resizeEvent = self.on_resize

        # Путь к ассетам
        path = "client/gui/resources/"

        # Отображение картинок
        icon = QIcon()
        icon.addPixmap(QPixmap(path + "img/logo_black.svg"),
                       QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.ui.lbl_logo.setPixmap(QPixmap(path + "img/logo_white.svg"))
        self.ui.lbl_arrow.setPixmap(QPixmap(path + "img/arrow.svg"))

        # Работа со шрифтом
        font_id = QFontDatabase.addApplicationFont(
            path + "fonts/OpenSans-Regular.ttf")
        if font_id < 0:
            print('Font not loaded')
        families = QFontDatabase.applicationFontFamilies(font_id)
        font = QFont(families[0])
        self.ui.lbl_profile.setFont(font)

        # Создание страниц для отображения в stacked widget
        self.main_page = MainPage(self)
        self.profile_page = ProfilePage(self)
        self.test_page = TestPage(self)

        # Инициализация первой страницы
        self.ui.stackedWidget.addWidget(self.main_page)
        self.ui.stackedWidget.setCurrentWidget(self.main_page)

        # Привязка стиля (qss)
        with open(path + "styles/main.qss", 'r', encoding="utf-8") as file:
            self.setStyleSheet(file.read())

        with open(path + "styles/profile.qss", 'r', encoding="utf-8") as file:
            self.profile_page.setStyleSheet(file.read())
            self.test_page.setStyleSheet(file.read())

        with open(path + "styles/main.qss", 'r', encoding="utf-8") as file:
            self.main_page.setStyleSheet(file.read())

        # Добавление страниц
        self.ui.stackedWidget.addWidget(self.test_page)
        self.ui.stackedWidget.addWidget(self.profile_page)

        # Обработка нажатия на кнопок
        self.ui.lbl_graph_emb.mouseReleaseEvent = self.show_graph_emb_page
        self.ui.lbl_testing.mouseReleaseEvent = self.show_testing_page
        self.ui.lbl_exit.mouseReleaseEvent = self.close
        self.ui.lbl_logo.mouseReleaseEvent = self.show_main_page
        self.ui.lbl_profile.mouseReleaseEvent = self.show_profile_page

    def show_testing_page(self, event):
        event.accept()
        self.ui.stackedWidget.setCurrentWidget(self.test_page)

    def show_profile_page(self, event):
        event.accept()
        self.ui.stackedWidget.setCurrentWidget(self.profile_page)

    def show_main_page(self, event):
        event.accept()
        self.ui.stackedWidget.setCurrentWidget(self.main_page)

    def show_graph_emb_page(self, event):
        event.accept()
        self.ui.stackedWidget.setCurrentWidget(self.graph_emb_page)

    def on_resize(self, event):
        event.accept()
        # print(self.main_page.size())
