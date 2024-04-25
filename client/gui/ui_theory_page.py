# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_theory_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TheoryPage(object):
    def setupUi(self, TheoryPage):
        TheoryPage.setObjectName("TheoryPage")
        TheoryPage.resize(685, 590)
        self.horizontalLayout = QtWidgets.QHBoxLayout(TheoryPage)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_read = QtWidgets.QPushButton(TheoryPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_read.sizePolicy().hasHeightForWidth())
        self.btn_read.setSizePolicy(sizePolicy)
        self.btn_read.setMaximumSize(QtCore.QSize(350, 16777215))
        self.btn_read.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_read.setObjectName("btn_read")
        self.verticalLayout_2.addWidget(self.btn_read)
        spacerItem2 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_topics = QtWidgets.QLabel(TheoryPage)
        self.lbl_topics.setObjectName("lbl_topics")
        self.verticalLayout_3.addWidget(self.lbl_topics)
        self.lbl_topic_1 = QtWidgets.QLabel(TheoryPage)
        self.lbl_topic_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lbl_topic_1.setObjectName("lbl_topic_1")
        self.verticalLayout_3.addWidget(self.lbl_topic_1)
        self.lbl_topic_2 = QtWidgets.QLabel(TheoryPage)
        self.lbl_topic_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lbl_topic_2.setObjectName("lbl_topic_2")
        self.verticalLayout_3.addWidget(self.lbl_topic_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)

        self.retranslateUi(TheoryPage)
        QtCore.QMetaObject.connectSlotsByName(TheoryPage)

    def retranslateUi(self, TheoryPage):
        _translate = QtCore.QCoreApplication.translate
        TheoryPage.setWindowTitle(_translate("TheoryPage", "Form"))
        self.btn_read.setText(_translate("TheoryPage", "Отметить как прочитанное"))
        self.lbl_topics.setText(_translate("TheoryPage", "Темы:"))
        self.lbl_topic_1.setText(_translate("TheoryPage", "<html><head/><body><p>1. Термины и определения</p></body></html>"))
        self.lbl_topic_2.setText(_translate("TheoryPage", "<html><head/><body><p>2. Второй топик</p></body></html>"))