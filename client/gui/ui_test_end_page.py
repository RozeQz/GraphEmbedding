# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_test_end_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TestEndPage(object):
    def setupUi(self, TestEndPage):
        TestEndPage.setObjectName("TestEndPage")
        TestEndPage.resize(400, 290)
        self.horizontalLayout = QtWidgets.QHBoxLayout(TestEndPage)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.vbox_results = QtWidgets.QVBoxLayout()
        self.vbox_results.setSpacing(30)
        self.vbox_results.setObjectName("vbox_results")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vbox_results.addItem(spacerItem1)
        self.lbl_test_end = QtWidgets.QLabel(TestEndPage)
        self.lbl_test_end.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_test_end.setObjectName("lbl_test_end")
        self.vbox_results.addWidget(self.lbl_test_end)
        self.fbox_results = QtWidgets.QFormLayout()
        self.fbox_results.setHorizontalSpacing(10)
        self.fbox_results.setObjectName("fbox_results")
        self.lbl_fixed = QtWidgets.QLabel(TestEndPage)
        self.lbl_fixed.setObjectName("lbl_fixed")
        self.fbox_results.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_fixed)
        self.lbl_fixed_2 = QtWidgets.QLabel(TestEndPage)
        self.lbl_fixed_2.setObjectName("lbl_fixed_2")
        self.fbox_results.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_fixed_2)
        self.lbl_result = QtWidgets.QLabel(TestEndPage)
        self.lbl_result.setObjectName("lbl_result")
        self.fbox_results.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lbl_result)
        self.lbl_time = QtWidgets.QLabel(TestEndPage)
        self.lbl_time.setObjectName("lbl_time")
        self.fbox_results.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lbl_time)
        self.vbox_results.addLayout(self.fbox_results)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btn_restart = QtWidgets.QPushButton(TestEndPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_restart.sizePolicy().hasHeightForWidth())
        self.btn_restart.setSizePolicy(sizePolicy)
        self.btn_restart.setMinimumSize(QtCore.QSize(200, 0))
        self.btn_restart.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_restart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_restart.setObjectName("btn_restart")
        self.horizontalLayout_2.addWidget(self.btn_restart)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.vbox_results.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vbox_results.addItem(spacerItem4)
        self.horizontalLayout.addLayout(self.vbox_results)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)

        self.retranslateUi(TestEndPage)
        QtCore.QMetaObject.connectSlotsByName(TestEndPage)

    def retranslateUi(self, TestEndPage):
        _translate = QtCore.QCoreApplication.translate
        TestEndPage.setWindowTitle(_translate("TestEndPage", "Form"))
        self.lbl_test_end.setText(_translate("TestEndPage", "Тестирование завершено!"))
        self.lbl_fixed.setText(_translate("TestEndPage", "Ваш результат:"))
        self.lbl_fixed_2.setText(_translate("TestEndPage", "Время тестирования:"))
        self.lbl_result.setText(_translate("TestEndPage", "TextLabel"))
        self.lbl_time.setText(_translate("TestEndPage", "TextLabel"))
        self.btn_restart.setText(_translate("TestEndPage", "Вернуться на\n"
"начальную страницу"))
