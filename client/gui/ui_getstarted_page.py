# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_getstarted_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GetStartedPage(object):
    def setupUi(self, GetStartedPage):
        GetStartedPage.setObjectName("GetStartedPage")
        GetStartedPage.resize(651, 458)
        self.verticalLayout = QtWidgets.QVBoxLayout(GetStartedPage)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.lbl_intro = QtWidgets.QLabel(GetStartedPage)
        self.lbl_intro.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_intro.setWordWrap(True)
        self.lbl_intro.setObjectName("lbl_intro")
        self.horizontalLayout_3.addWidget(self.lbl_intro)
        spacerItem2 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.btn_login = QtWidgets.QPushButton(GetStartedPage)
        self.btn_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout_2.addWidget(self.btn_login)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.lbl_no_acc = QtWidgets.QLabel(GetStartedPage)
        self.lbl_no_acc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_no_acc.setWordWrap(True)
        self.lbl_no_acc.setObjectName("lbl_no_acc")
        self.horizontalLayout.addWidget(self.lbl_no_acc)
        self.lbl_signup = QtWidgets.QLabel(GetStartedPage)
        self.lbl_signup.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lbl_signup.setWordWrap(False)
        self.lbl_signup.setObjectName("lbl_signup")
        self.horizontalLayout.addWidget(self.lbl_signup)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)

        self.retranslateUi(GetStartedPage)
        QtCore.QMetaObject.connectSlotsByName(GetStartedPage)

    def retranslateUi(self, GetStartedPage):
        _translate = QtCore.QCoreApplication.translate
        GetStartedPage.setWindowTitle(_translate("GetStartedPage", "Form"))
        self.lbl_intro.setText(_translate("GetStartedPage", "<html><head/><body><p>Чтобы получить доступ к страницам раздела <span style=\" color:#0c8ce8;\">&quot;Обучения&quot;</span>, а также к странице<span style=\" color:#0c8ce8;\">&quot;Профиль&quot;</span>, войдите в аккаунт или создайте его.</p></body></html>"))
        self.btn_login.setText(_translate("GetStartedPage", "Войти"))
        self.lbl_no_acc.setText(_translate("GetStartedPage", "<html><head/><body><p>Нет аккаунта?</p></body></html>"))
        self.lbl_signup.setText(_translate("GetStartedPage", "<html><head/><body><p>Зарегистрируйтесь бесплатно.</p></body></html>"))
