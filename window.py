# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 40, 160, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_gloss = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_gloss.setFont(font)
        self.label_gloss.setObjectName("label_gloss")
        self.horizontalLayout.addWidget(self.label_gloss)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(230, 40, 167, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_gloss_index = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_gloss_index.setFont(font)
        self.label_gloss_index.setObjectName("label_gloss_index")
        self.horizontalLayout_2.addWidget(self.label_gloss_index)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(410, 40, 201, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_operater = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_operater.sizePolicy().hasHeightForWidth())
        self.lineEdit_operater.setSizePolicy(sizePolicy)
        self.lineEdit_operater.setObjectName("lineEdit_operater")
        self.horizontalLayout_3.addWidget(self.lineEdit_operater)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(620, 40, 181, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_date = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_date.sizePolicy().hasHeightForWidth())
        self.lineEdit_date.setSizePolicy(sizePolicy)
        self.lineEdit_date.setObjectName("lineEdit_date")
        self.horizontalLayout_4.addWidget(self.lineEdit_date)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 100, 101, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 150, 1181, 261))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(21)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_pattern_fade_in_L_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_fade_in_L_2.setFont(font)
        self.lineEdit_pattern_fade_in_L_2.setObjectName("lineEdit_pattern_fade_in_L_2")
        self.gridLayout.addWidget(self.lineEdit_pattern_fade_in_L_2, 2, 3, 1, 1)
        self.lineEdit_pattern_fade_out_L_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_fade_out_L_4.setFont(font)
        self.lineEdit_pattern_fade_out_L_4.setObjectName("lineEdit_pattern_fade_out_L_4")
        self.gridLayout.addWidget(self.lineEdit_pattern_fade_out_L_4, 4, 6, 1, 1)
        self.lineEdit_pattern_start_L_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_start_L_1.setFont(font)
        self.lineEdit_pattern_start_L_1.setObjectName("lineEdit_pattern_start_L_1")
        self.gridLayout.addWidget(self.lineEdit_pattern_start_L_1, 1, 4, 1, 1)
        self.lineEdit_pattern_fade_out_L_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_fade_out_L_3.setFont(font)
        self.lineEdit_pattern_fade_out_L_3.setObjectName("lineEdit_pattern_fade_out_L_3")
        self.gridLayout.addWidget(self.lineEdit_pattern_fade_out_L_3, 3, 6, 1, 1)
        self.lineEdit_pattern_start_L_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_start_L_2.setFont(font)
        self.lineEdit_pattern_start_L_2.setObjectName("lineEdit_pattern_start_L_2")
        self.gridLayout.addWidget(self.lineEdit_pattern_start_L_2, 2, 4, 1, 1)
        self.lineEdit_pattern_fade_in_L_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_fade_in_L_3.setFont(font)
        self.lineEdit_pattern_fade_in_L_3.setObjectName("lineEdit_pattern_fade_in_L_3")
        self.gridLayout.addWidget(self.lineEdit_pattern_fade_in_L_3, 3, 3, 1, 1)
        self.lineEdit_pattern_fade_out_L_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_fade_out_L_1.setFont(font)
        self.lineEdit_pattern_fade_out_L_1.setObjectName("lineEdit_pattern_fade_out_L_1")
        self.gridLayout.addWidget(self.lineEdit_pattern_fade_out_L_1, 1, 6, 1, 1)
        self.lineEdit_pattern_start_L_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_start_L_4.setFont(font)
        self.lineEdit_pattern_start_L_4.setObjectName("lineEdit_pattern_start_L_4")
        self.gridLayout.addWidget(self.lineEdit_pattern_start_L_4, 4, 4, 1, 1)
        self.lineEdit_pattern_start_L_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_start_L_3.setFont(font)
        self.lineEdit_pattern_start_L_3.setObjectName("lineEdit_pattern_start_L_3")
        self.gridLayout.addWidget(self.lineEdit_pattern_start_L_3, 3, 4, 1, 1)
        self.lineEdit_pattern_end_L_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_end_L_3.setFont(font)
        self.lineEdit_pattern_end_L_3.setObjectName("lineEdit_pattern_end_L_3")
        self.gridLayout.addWidget(self.lineEdit_pattern_end_L_3, 3, 5, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 4, 1, 1)
        self.lineEdit_pattern_index_L_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_index_L_3.setFont(font)
        self.lineEdit_pattern_index_L_3.setObjectName("lineEdit_pattern_index_L_3")
        self.gridLayout.addWidget(self.lineEdit_pattern_index_L_3, 3, 2, 1, 1)
        self.lineEdit_pattern_end_L_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_end_L_2.setFont(font)
        self.lineEdit_pattern_end_L_2.setObjectName("lineEdit_pattern_end_L_2")
        self.gridLayout.addWidget(self.lineEdit_pattern_end_L_2, 2, 5, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 6, 1, 1)
        self.lineEdit_pattern_fade_in_L_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_fade_in_L_1.setFont(font)
        self.lineEdit_pattern_fade_in_L_1.setObjectName("lineEdit_pattern_fade_in_L_1")
        self.gridLayout.addWidget(self.lineEdit_pattern_fade_in_L_1, 1, 3, 1, 1)
        self.lineEdit_pattern_index_L_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_index_L_4.setFont(font)
        self.lineEdit_pattern_index_L_4.setObjectName("lineEdit_pattern_index_L_4")
        self.gridLayout.addWidget(self.lineEdit_pattern_index_L_4, 4, 2, 1, 1)
        self.lineEdit_pattern_index_L_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_index_L_2.setFont(font)
        self.lineEdit_pattern_index_L_2.setObjectName("lineEdit_pattern_index_L_2")
        self.gridLayout.addWidget(self.lineEdit_pattern_index_L_2, 2, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 5, 1, 1)
        self.lineEdit_pattern_end_L_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_end_L_1.setFont(font)
        self.lineEdit_pattern_end_L_1.setObjectName("lineEdit_pattern_end_L_1")
        self.gridLayout.addWidget(self.lineEdit_pattern_end_L_1, 1, 5, 1, 1)
        self.lineEdit_pattern_end_L_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_end_L_4.setFont(font)
        self.lineEdit_pattern_end_L_4.setObjectName("lineEdit_pattern_end_L_4")
        self.gridLayout.addWidget(self.lineEdit_pattern_end_L_4, 4, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(0, 4))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 23))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)
        self.lineEdit_pattern_fade_in_L_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_fade_in_L_4.setFont(font)
        self.lineEdit_pattern_fade_in_L_4.setObjectName("lineEdit_pattern_fade_in_L_4")
        self.gridLayout.addWidget(self.lineEdit_pattern_fade_in_L_4, 4, 3, 1, 1)
        self.lineEdit_pattern_index_L_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_index_L_1.setFont(font)
        self.lineEdit_pattern_index_L_1.setObjectName("lineEdit_pattern_index_L_1")
        self.gridLayout.addWidget(self.lineEdit_pattern_index_L_1, 1, 2, 1, 1)
        self.lineEdit_pattern_fade_out_L_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_fade_out_L_2.setFont(font)
        self.lineEdit_pattern_fade_out_L_2.setObjectName("lineEdit_pattern_fade_out_L_2")
        self.gridLayout.addWidget(self.lineEdit_pattern_fade_out_L_2, 2, 6, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 2, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 3, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 1, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 4, 0, 1, 1)
        self.checkBox_L_1 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_L_1.setText("")
        self.checkBox_L_1.setObjectName("checkBox_L_1")
        self.gridLayout.addWidget(self.checkBox_L_1, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 2)
        self.checkBox_L_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_L_2.setText("")
        self.checkBox_L_2.setObjectName("checkBox_L_2")
        self.gridLayout.addWidget(self.checkBox_L_2, 2, 1, 1, 1)
        self.checkBox_L_3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_L_3.setText("")
        self.checkBox_L_3.setObjectName("checkBox_L_3")
        self.gridLayout.addWidget(self.checkBox_L_3, 3, 1, 1, 1)
        self.checkBox_L_4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_L_4.setText("")
        self.checkBox_L_4.setObjectName("checkBox_L_4")
        self.gridLayout.addWidget(self.checkBox_L_4, 4, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(70, 420, 1181, 261))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setVerticalSpacing(21)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_pattern_fade_out_R_4 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_fade_out_R_4.setFont(font)
        self.lineEdit_pattern_fade_out_R_4.setObjectName("lineEdit_pattern_fade_out_R_4")
        self.gridLayout_2.addWidget(self.lineEdit_pattern_fade_out_R_4, 4, 6, 1, 1)
        self.lineEdit_pattern_end_R_4 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_end_R_4.setFont(font)
        self.lineEdit_pattern_end_R_4.setObjectName("lineEdit_pattern_end_R_4")
        self.gridLayout_2.addWidget(self.lineEdit_pattern_end_R_4, 4, 5, 1, 1)
        self.lineEdit_pattern_fade_in_R_1 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_fade_in_R_1.setFont(font)
        self.lineEdit_pattern_fade_in_R_1.setObjectName("lineEdit_pattern_fade_in_R_1")
        self.gridLayout_2.addWidget(self.lineEdit_pattern_fade_in_R_1, 1, 3, 1, 1)
        self.lineEdit_pattern_start_R_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_start_R_2.setFont(font)
        self.lineEdit_pattern_start_R_2.setObjectName("lineEdit_pattern_start_R_2")
        self.gridLayout_2.addWidget(self.lineEdit_pattern_start_R_2, 2, 4, 1, 1)
        self.lineEdit_pattern_end_R_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_end_R_3.setFont(font)
        self.lineEdit_pattern_end_R_3.setObjectName("lineEdit_pattern_end_R_3")
        self.gridLayout_2.addWidget(self.lineEdit_pattern_end_R_3, 3, 5, 1, 1)
        self.lineEdit_pattern_index_R_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_index_R_3.setFont(font)
        self.lineEdit_pattern_index_R_3.setObjectName("lineEdit_pattern_index_R_3")
        self.gridLayout_2.addWidget(self.lineEdit_pattern_index_R_3, 3, 2, 1, 1)
        self.lineEdit_pattern_start_R_1 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_start_R_1.setFont(font)
        self.lineEdit_pattern_start_R_1.setObjectName("lineEdit_pattern_start_R_1")
        self.gridLayout_2.addWidget(self.lineEdit_pattern_start_R_1, 1, 4, 1, 1)
        self.lineEdit_pattern_fade_out_R_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_fade_out_R_3.setFont(font)
        self.lineEdit_pattern_fade_out_R_3.setObjectName("lineEdit_pattern_fade_out_R_3")
        self.gridLayout_2.addWidget(self.lineEdit_pattern_fade_out_R_3, 3, 6, 1, 1)
        self.lineEdit_pattern_fade_out_R_1 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_fade_out_R_1.setFont(font)
        self.lineEdit_pattern_fade_out_R_1.setObjectName("lineEdit_pattern_fade_out_R_1")
        self.gridLayout_2.addWidget(self.lineEdit_pattern_fade_out_R_1, 1, 6, 1, 1)
        self.lineEdit_pattern_fade_in_R_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_fade_in_R_3.setFont(font)
        self.lineEdit_pattern_fade_in_R_3.setObjectName("lineEdit_pattern_fade_in_R_3")
        self.gridLayout_2.addWidget(self.lineEdit_pattern_fade_in_R_3, 3, 3, 1, 1)
        self.lineEdit_pattern_start_R_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_start_R_3.setFont(font)
        self.lineEdit_pattern_start_R_3.setObjectName("lineEdit_pattern_start_R_3")
        self.gridLayout_2.addWidget(self.lineEdit_pattern_start_R_3, 3, 4, 1, 1)
        self.lineEdit_pattern_start_R_4 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_start_R_4.setFont(font)
        self.lineEdit_pattern_start_R_4.setObjectName("lineEdit_pattern_start_R_4")
        self.gridLayout_2.addWidget(self.lineEdit_pattern_start_R_4, 4, 4, 1, 1)
        self.lineEdit_pattern_fade_in_R_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_fade_in_R_2.setFont(font)
        self.lineEdit_pattern_fade_in_R_2.setObjectName("lineEdit_pattern_fade_in_R_2")
        self.gridLayout_2.addWidget(self.lineEdit_pattern_fade_in_R_2, 2, 3, 1, 1)
        self.lineEdit_pattern_end_R_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_end_R_2.setFont(font)
        self.lineEdit_pattern_end_R_2.setObjectName("lineEdit_pattern_end_R_2")
        self.gridLayout_2.addWidget(self.lineEdit_pattern_end_R_2, 2, 5, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 0, 5, 1, 1)
        self.lineEdit_pattern_index_R_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_index_R_2.setFont(font)
        self.lineEdit_pattern_index_R_2.setObjectName("lineEdit_pattern_index_R_2")
        self.gridLayout_2.addWidget(self.lineEdit_pattern_index_R_2, 2, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(0, 4))
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 23))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 0, 2, 1, 1)
        self.lineEdit_pattern_fade_out_R_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_fade_out_R_2.setFont(font)
        self.lineEdit_pattern_fade_out_R_2.setObjectName("lineEdit_pattern_fade_out_R_2")
        self.gridLayout_2.addWidget(self.lineEdit_pattern_fade_out_R_2, 2, 6, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 0, 3, 1, 1)
        self.lineEdit_pattern_index_R_4 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_index_R_4.setFont(font)
        self.lineEdit_pattern_index_R_4.setObjectName("lineEdit_pattern_index_R_4")
        self.gridLayout_2.addWidget(self.lineEdit_pattern_index_R_4, 4, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 0, 4, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 6, 1, 1)
        self.lineEdit_pattern_fade_in_R_4 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_fade_in_R_4.setFont(font)
        self.lineEdit_pattern_fade_in_R_4.setObjectName("lineEdit_pattern_fade_in_R_4")
        self.gridLayout_2.addWidget(self.lineEdit_pattern_fade_in_R_4, 4, 3, 1, 1)
        self.lineEdit_pattern_index_R_1 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_index_R_1.setFont(font)
        self.lineEdit_pattern_index_R_1.setObjectName("lineEdit_pattern_index_R_1")
        self.gridLayout_2.addWidget(self.lineEdit_pattern_index_R_1, 1, 2, 1, 1)
        self.lineEdit_pattern_end_R_1 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pattern_end_R_1.setFont(font)
        self.lineEdit_pattern_end_R_1.setObjectName("lineEdit_pattern_end_R_1")
        self.gridLayout_2.addWidget(self.lineEdit_pattern_end_R_1, 1, 5, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 2, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 1, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 4, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 3, 0, 1, 1)
        self.checkBox_R_1 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_R_1.setText("")
        self.checkBox_R_1.setObjectName("checkBox_R_1")
        self.gridLayout_2.addWidget(self.checkBox_R_1, 1, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 0, 0, 1, 2)
        self.checkBox_R_2 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_R_2.setText("")
        self.checkBox_R_2.setObjectName("checkBox_R_2")
        self.gridLayout_2.addWidget(self.checkBox_R_2, 2, 1, 1, 1)
        self.checkBox_R_3 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_R_3.setText("")
        self.checkBox_R_3.setObjectName("checkBox_R_3")
        self.gridLayout_2.addWidget(self.checkBox_R_3, 3, 1, 1, 1)
        self.checkBox_R_4 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_R_4.setText("")
        self.checkBox_R_4.setObjectName("checkBox_R_4")
        self.gridLayout_2.addWidget(self.checkBox_R_4, 4, 1, 1, 1)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(950, 30, 383, 80))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButton_1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setObjectName("radioButton_1")
        self.horizontalLayout_5.addWidget(self.radioButton_1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_5.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_5.addWidget(self.radioButton_3)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(70, 700, 731, 51))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(40)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_save = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_6.addWidget(self.pushButton_save)
        self.pushButton_prev = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_prev.setObjectName("pushButton_prev")
        self.horizontalLayout_6.addWidget(self.pushButton_prev)
        self.pushButton_next = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_next.setObjectName("pushButton_next")
        self.horizontalLayout_6.addWidget(self.pushButton_next)
        self.pushButton_video = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_video.setObjectName("pushButton_video")
        self.horizontalLayout_6.addWidget(self.pushButton_video)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(930, 710, 366, 41))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_18 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_7.addWidget(self.label_18)
        self.label_index_cur = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_index_cur.setObjectName("label_index_cur")
        self.horizontalLayout_7.addWidget(self.label_index_cur)
        self.lineEdit_to_index = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_to_index.sizePolicy().hasHeightForWidth())
        self.lineEdit_to_index.setSizePolicy(sizePolicy)
        self.lineEdit_to_index.setObjectName("lineEdit_to_index")
        self.horizontalLayout_7.addWidget(self.lineEdit_to_index)
        self.pushButton_toIndex = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.pushButton_toIndex.setObjectName("pushButton_toIndex")
        self.horizontalLayout_7.addWidget(self.pushButton_toIndex)
        self.pushButton_load = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_load.setGeometry(QtCore.QRect(825, 30, 112, 34))
        self.pushButton_load.setObjectName("pushButton_load")
        self.label_load_con = QtWidgets.QLabel(self.centralwidget)
        self.label_load_con.setGeometry(QtCore.QRect(850, 80, 81, 18))
        self.label_load_con.setObjectName("label_load_con")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "词目："))
        self.label_gloss.setText(_translate("MainWindow", "爱国"))
        self.label_2.setText(_translate("MainWindow", "词目序号："))
        self.label_gloss_index.setText(_translate("MainWindow", "101"))
        self.label_3.setText(_translate("MainWindow", "标记员："))
        self.lineEdit_operater.setText(_translate("MainWindow", "张三"))
        self.label_4.setText(_translate("MainWindow", "日期："))
        self.lineEdit_date.setText(_translate("MainWindow", "3.14"))
        self.label_5.setText(_translate("MainWindow", "动作标记"))
        self.label_9.setText(_translate("MainWindow", "start"))
        self.label_11.setText(_translate("MainWindow", "fade_out"))
        self.label_10.setText(_translate("MainWindow", "end"))
        self.label_8.setText(_translate("MainWindow", "fade_in"))
        self.label_7.setText(_translate("MainWindow", "模板号"))
        self.label_20.setText(_translate("MainWindow", "动作2"))
        self.label_21.setText(_translate("MainWindow", "动作3"))
        self.label_19.setText(_translate("MainWindow", "动作1"))
        self.label_22.setText(_translate("MainWindow", "动作4"))
        self.label_6.setText(_translate("MainWindow", "左手   "))
        self.label_16.setText(_translate("MainWindow", "end"))
        self.label_14.setText(_translate("MainWindow", "模板号"))
        self.label_15.setText(_translate("MainWindow", "fade_in"))
        self.label_12.setText(_translate("MainWindow", "start"))
        self.label_13.setText(_translate("MainWindow", "fade_out"))
        self.label_24.setText(_translate("MainWindow", "动作2"))
        self.label_23.setText(_translate("MainWindow", "动作1"))
        self.label_26.setText(_translate("MainWindow", "动作4"))
        self.label_25.setText(_translate("MainWindow", "动作3"))
        self.label_17.setText(_translate("MainWindow", "右手   "))
        self.radioButton_1.setText(_translate("MainWindow", "需修改"))
        self.radioButton_2.setText(_translate("MainWindow", "无需修改"))
        self.radioButton_3.setText(_translate("MainWindow", "不确定"))
        self.pushButton_save.setText(_translate("MainWindow", "保存"))
        self.pushButton_prev.setText(_translate("MainWindow", "上一个"))
        self.pushButton_next.setText(_translate("MainWindow", "下一个"))
        self.pushButton_video.setText(_translate("MainWindow", "打开视频"))
        self.label_18.setText(_translate("MainWindow", "当前词目："))
        self.label_index_cur.setText(_translate("MainWindow", "NULL"))
        self.pushButton_toIndex.setText(_translate("MainWindow", "转到"))
        self.pushButton_load.setText(_translate("MainWindow", "导入数据"))
        self.label_load_con.setText(_translate("MainWindow", "未导入"))
