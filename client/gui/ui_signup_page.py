# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_signup_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignUpPage(object):
    def setupUi(self, SignUpPage):
        SignUpPage.setObjectName("SignUpPage")
        SignUpPage.resize(642, 457)
        self.verticalLayout = QtWidgets.QVBoxLayout(SignUpPage)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_8 = QtWidgets.QLabel(SignUpPage)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_status = QtWidgets.QLabel(SignUpPage)
        self.lbl_status.setMaximumSize(QtCore.QSize(500, 16777215))
        self.lbl_status.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_status.setWordWrap(True)
        self.lbl_status.setObjectName("lbl_status")
        self.horizontalLayout_3.addWidget(self.lbl_status)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(8)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(SignUpPage)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(SignUpPage)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(SignUpPage)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(SignUpPage)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(SignUpPage)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(SignUpPage)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(SignUpPage)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lbl_fixed_group = QtWidgets.QLabel(SignUpPage)
        self.lbl_fixed_group.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_fixed_group.setObjectName("lbl_fixed_group")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.lbl_fixed_group)
        self.edt_group = QtWidgets.QLineEdit(SignUpPage)
        self.edt_group.setObjectName("edt_group")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.edt_group)
        self.cbx_role = QtWidgets.QComboBox(SignUpPage)
        self.cbx_role.setObjectName("cbx_role")
        self.cbx_role.addItem("")
        self.cbx_role.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.cbx_role)
        self.edt_password = QtWidgets.QLineEdit(SignUpPage)
        self.edt_password.setToolTip("")
        self.edt_password.setPlaceholderText("")
        self.edt_password.setObjectName("edt_password")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.edt_password)
        self.edt_login = QtWidgets.QLineEdit(SignUpPage)
        self.edt_login.setObjectName("edt_login")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.edt_login)
        self.edt_email = QtWidgets.QLineEdit(SignUpPage)
        self.edt_email.setObjectName("edt_email")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.edt_email)
        self.edt_midname = QtWidgets.QLineEdit(SignUpPage)
        self.edt_midname.setObjectName("edt_midname")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.edt_midname)
        self.edt_name = QtWidgets.QLineEdit(SignUpPage)
        self.edt_name.setObjectName("edt_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.edt_name)
        self.edt_surname = QtWidgets.QLineEdit(SignUpPage)
        self.edt_surname.setObjectName("edt_surname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edt_surname)
        self.horizontalLayout_2.addLayout(self.formLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.btn_signup = QtWidgets.QPushButton(SignUpPage)
        self.btn_signup.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_signup.setObjectName("btn_signup")
        self.horizontalLayout.addWidget(self.btn_signup)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.label_9 = QtWidgets.QLabel(SignUpPage)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.lbl_login = QtWidgets.QLabel(SignUpPage)
        self.lbl_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lbl_login.setObjectName("lbl_login")
        self.horizontalLayout_4.addWidget(self.lbl_login)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem11)

        self.retranslateUi(SignUpPage)
        QtCore.QMetaObject.connectSlotsByName(SignUpPage)

    def retranslateUi(self, SignUpPage):
        _translate = QtCore.QCoreApplication.translate
        SignUpPage.setWindowTitle(_translate("SignUpPage", "Form"))
        self.label_8.setText(_translate("SignUpPage", "Регистрация"))
        self.lbl_status.setText(_translate("SignUpPage", "TextLabel"))
        self.label.setText(_translate("SignUpPage", "Фамилия:"))
        self.label_2.setText(_translate("SignUpPage", "Имя:"))
        self.label_3.setText(_translate("SignUpPage", "Отчество:"))
        self.label_4.setText(_translate("SignUpPage", "Email:"))
        self.label_5.setText(_translate("SignUpPage", "Логин:"))
        self.label_6.setText(_translate("SignUpPage", "Пароль:"))
        self.label_7.setText(_translate("SignUpPage", "Роль:"))
        self.lbl_fixed_group.setText(_translate("SignUpPage", "Группа:"))
        self.edt_group.setPlaceholderText(_translate("SignUpPage", "ИУ6-71Б"))
        self.cbx_role.setItemText(0, _translate("SignUpPage", "Студент"))
        self.cbx_role.setItemText(1, _translate("SignUpPage", "Преподаватель"))
        self.edt_login.setPlaceholderText(_translate("SignUpPage", "ivan"))
        self.edt_email.setPlaceholderText(_translate("SignUpPage", "ivan@gmail.ru"))
        self.edt_midname.setPlaceholderText(_translate("SignUpPage", "Иванович (необязательное поле)"))
        self.edt_name.setPlaceholderText(_translate("SignUpPage", "Иван"))
        self.edt_surname.setPlaceholderText(_translate("SignUpPage", "Иванов"))
        self.btn_signup.setText(_translate("SignUpPage", "Зарегистрироваться"))
        self.label_9.setText(_translate("SignUpPage", "Уже есть аккаунт?"))
        self.lbl_login.setText(_translate("SignUpPage", "Войти"))
