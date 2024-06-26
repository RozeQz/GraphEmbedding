# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_test_start_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TestStartPage(object):
    def setupUi(self, TestStartPage):
        TestStartPage.setObjectName("TestStartPage")
        TestStartPage.resize(754, 481)
        self.verticalLayout = QtWidgets.QVBoxLayout(TestStartPage)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.lbl_warning = QtWidgets.QLabel(TestStartPage)
        self.lbl_warning.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_warning.setObjectName("lbl_warning")
        self.verticalLayout.addWidget(self.lbl_warning)
        self.lbl_test_info = QtWidgets.QLabel(TestStartPage)
        self.lbl_test_info.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_test_info.setObjectName("lbl_test_info")
        self.verticalLayout.addWidget(self.lbl_test_info)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_start = QtWidgets.QPushButton(TestStartPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        self.btn_start.setMinimumSize(QtCore.QSize(160, 40))
        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout.addWidget(self.btn_start)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)

        self.retranslateUi(TestStartPage)
        QtCore.QMetaObject.connectSlotsByName(TestStartPage)

    def retranslateUi(self, TestStartPage):
        _translate = QtCore.QCoreApplication.translate
        TestStartPage.setWindowTitle(_translate("TestStartPage", "Form"))
        self.lbl_warning.setText(_translate("TestStartPage", "<html><head/><body><p>Внимание!</p><p>Перед прохождением тестирования, ознакомьтесь с информацией ниже.</p></body></html>"))
        self.lbl_test_info.setText(_translate("TestStartPage", "<html><head/><body><p>Во время тестирования нельзя перемещаться между вопросами - сначала нужно ответить на текущий вопрос.</p><p>На все тестирование Вам будет дано 30 минут.</p><p>После ответа на все вопросы или по завершению таймера, тестирование будет завершено.</p><p>После завершения тестирования можно будет ознакомиться с результатами сразу же, либо на странице профиля.</p><p>Все результаты будут видны Вашему преподавателю.</p></body></html>"))
        self.btn_start.setText(_translate("TestStartPage", "Начать тестирование"))
