# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1920, 1080)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/logo_black.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(26)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.fr_menu = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fr_menu.sizePolicy().hasHeightForWidth())
        self.fr_menu.setSizePolicy(sizePolicy)
        self.fr_menu.setMinimumSize(QtCore.QSize(0, 0))
        self.fr_menu.setMaximumSize(QtCore.QSize(360, 16777215))
        self.fr_menu.setStyleSheet("QFrame {\n"
"    background-color: rgb(44, 48, 57);\n"
"}")
        self.fr_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_menu.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fr_menu.setLineWidth(0)
        self.fr_menu.setObjectName("fr_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fr_menu)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_logo = QtWidgets.QLabel(self.fr_menu)
        self.lbl_logo.setMaximumSize(QtCore.QSize(16777215, 200))
        self.lbl_logo.setStyleSheet("")
        self.lbl_logo.setText("")
        self.lbl_logo.setPixmap(QtGui.QPixmap("../assets/logo_white.svg"))
        self.lbl_logo.setScaledContents(False)
        self.lbl_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_logo.setObjectName("lbl_logo")
        self.verticalLayout_3.addWidget(self.lbl_logo)
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_profile = QtWidgets.QLabel(self.fr_menu)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_profile.setFont(font)
        self.lbl_profile.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    text-align: left;\n"
"    margin-left: 32;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: rgb(12, 140, 233);\n"
"}")
        self.lbl_profile.setObjectName("lbl_profile")
        self.verticalLayout.addWidget(self.lbl_profile)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_edu = QtWidgets.QLabel(self.fr_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_edu.sizePolicy().hasHeightForWidth())
        self.lbl_edu.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(26)
        font.setKerning(True)
        self.lbl_edu.setFont(font)
        self.lbl_edu.setStyleSheet("color: rgb(158, 172, 183);\n"
"text-align: left;\n"
"margin-left: 32;")
        self.lbl_edu.setObjectName("lbl_edu")
        self.horizontalLayout_3.addWidget(self.lbl_edu)
        self.lbl_arrow = QtWidgets.QLabel(self.fr_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_arrow.sizePolicy().hasHeightForWidth())
        self.lbl_arrow.setSizePolicy(sizePolicy)
        self.lbl_arrow.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_arrow.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lbl_arrow.setText("")
        self.lbl_arrow.setPixmap(QtGui.QPixmap("../assets/arrow.svg"))
        self.lbl_arrow.setObjectName("lbl_arrow")
        self.horizontalLayout_3.addWidget(self.lbl_arrow)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.lbl_testing = QtWidgets.QLabel(self.fr_menu)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(26)
        self.lbl_testing.setFont(font)
        self.lbl_testing.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    text-align: left;\n"
"    margin-left: 52;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: rgb(12, 140, 233);\n"
"}")
        self.lbl_testing.setObjectName("lbl_testing")
        self.verticalLayout_2.addWidget(self.lbl_testing)
        self.lbl_tasks = QtWidgets.QLabel(self.fr_menu)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(26)
        self.lbl_tasks.setFont(font)
        self.lbl_tasks.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    text-align: left;\n"
"    margin-left: 52;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: rgb(12, 140, 233);\n"
"}")
        self.lbl_tasks.setObjectName("lbl_tasks")
        self.verticalLayout_2.addWidget(self.lbl_tasks)
        self.lbl_theory = QtWidgets.QLabel(self.fr_menu)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(26)
        self.lbl_theory.setFont(font)
        self.lbl_theory.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    text-align: left;\n"
"    margin-left: 52;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: rgb(12, 140, 233);\n"
"}\n"
"")
        self.lbl_theory.setObjectName("lbl_theory")
        self.verticalLayout_2.addWidget(self.lbl_theory)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.lbl_graph_emb = QtWidgets.QLabel(self.fr_menu)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(26)
        self.lbl_graph_emb.setFont(font)
        self.lbl_graph_emb.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    text-align: left;\n"
"    margin-left: 32;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: rgb(12, 140, 233);\n"
"}")
        self.lbl_graph_emb.setObjectName("lbl_graph_emb")
        self.verticalLayout.addWidget(self.lbl_graph_emb)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem1)
        self.lbl_exit = QtWidgets.QLabel(self.fr_menu)
        self.lbl_exit.setMaximumSize(QtCore.QSize(16777215, 160))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_exit.setFont(font)
        self.lbl_exit.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    text-align: left;\n"
"    margin-left: 32;\n"
"    margin-top: 30;\n"
"    margin-bottom: 50;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: rgb(12, 140, 233);\n"
"}")
        self.lbl_exit.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lbl_exit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.lbl_exit.setObjectName("lbl_exit")
        self.verticalLayout_3.addWidget(self.lbl_exit)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 1)
        self.verticalLayout_3.setStretch(4, 1)
        self.horizontalLayout_4.addWidget(self.fr_menu)
        self.fr_main = QtWidgets.QFrame(self.centralwidget)
        self.fr_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_main.setObjectName("fr_main")
        self.horizontalLayout_4.addWidget(self.fr_main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PlanarEd"))
        self.lbl_profile.setText(_translate("MainWindow", "Профиль"))
        self.lbl_edu.setText(_translate("MainWindow", "Обучение"))
        self.lbl_testing.setText(_translate("MainWindow", "Тестирование"))
        self.lbl_tasks.setText(_translate("MainWindow", "Задания"))
        self.lbl_theory.setText(_translate("MainWindow", "Теория"))
        self.lbl_graph_emb.setText(_translate("MainWindow", "Укладка графа"))
        self.lbl_exit.setText(_translate("MainWindow", "Выйти"))
