# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QCompleter, QButtonGroup, QDialog
import sys
from PyQt5.QtCore import Qt
from window import Ui_MainWindow
import xlrd
import xlwt
from pprint import pprint  # pprint的输出形式为一行输出一个结果，下一个结果换行输出。实质上pprint输出的结果更为完整
import json
import pandas as pd
import os
from os import startfile
import csv
dataBase = []


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_all_able(False)
        self.set_box_able(False)
        self.pushButton_next.clicked.connect(self.glossNext)
        self.pushButton_prev.clicked.connect(self.glossprev)
        self.pushButton_toIndex.clicked.connect(self.toIndex)
        self.pushButton_load.clicked.connect(self.load)
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_video.clicked.connect(self.openVideo)

        self.radioButton_1.clicked.connect(self.set_change_able)
        self.radioButton_2.clicked.connect(self.set_change_able)
        self.radioButton_3.clicked.connect(self.set_change_able)

        self.checkBox_L_1.clicked.connect(self.set_L_1_able)
        self.checkBox_L_2.clicked.connect(self.set_L_2_able)
        self.checkBox_L_3.clicked.connect(self.set_L_3_able)
        self.checkBox_L_4.clicked.connect(self.set_L_4_able)

        self.checkBox_R_1.clicked.connect(self.set_R_1_able)
        self.checkBox_R_2.clicked.connect(self.set_R_2_able)
        self.checkBox_R_3.clicked.connect(self.set_R_3_able)
        self.checkBox_R_4.clicked.connect(self.set_R_4_able)

    def set_box_able(self, con:bool):
        self.checkBox_L_1.setEnabled(con)
        self.checkBox_L_2.setEnabled(con)
        self.checkBox_L_3.setEnabled(con)
        self.checkBox_L_4.setEnabled(con)

        self.checkBox_R_1.setEnabled(con)
        self.checkBox_R_2.setEnabled(con)
        self.checkBox_R_3.setEnabled(con)
        self.checkBox_R_4.setEnabled(con)

    def set_all_able(self, con: bool):
        self.lineEdit_pattern_index_L_1.setEnabled(con)
        self.lineEdit_pattern_index_L_2.setEnabled(con)
        self.lineEdit_pattern_index_L_3.setEnabled(con)
        self.lineEdit_pattern_index_L_4.setEnabled(con)

        self.lineEdit_pattern_index_R_1.setEnabled(con)
        self.lineEdit_pattern_index_R_2.setEnabled(con)
        self.lineEdit_pattern_index_R_3.setEnabled(con)
        self.lineEdit_pattern_index_R_4.setEnabled(con)

        self.lineEdit_pattern_end_L_1.setEnabled(con)
        self.lineEdit_pattern_end_L_2.setEnabled(con)
        self.lineEdit_pattern_end_L_3.setEnabled(con)
        self.lineEdit_pattern_end_L_4.setEnabled(con)

        self.lineEdit_pattern_end_R_1.setEnabled(con)
        self.lineEdit_pattern_end_R_2.setEnabled(con)
        self.lineEdit_pattern_end_R_3.setEnabled(con)
        self.lineEdit_pattern_end_R_4.setEnabled(con)

        self.lineEdit_pattern_fade_out_L_1.setEnabled(con)
        self.lineEdit_pattern_fade_out_L_2.setEnabled(con)
        self.lineEdit_pattern_fade_out_L_3.setEnabled(con)
        self.lineEdit_pattern_fade_out_L_4.setEnabled(con)

        self.lineEdit_pattern_fade_out_R_1.setEnabled(con)
        self.lineEdit_pattern_fade_out_R_2.setEnabled(con)
        self.lineEdit_pattern_fade_out_R_3.setEnabled(con)
        self.lineEdit_pattern_fade_out_R_4.setEnabled(con)

        self.lineEdit_pattern_fade_in_L_1.setEnabled(con)
        self.lineEdit_pattern_fade_in_L_2.setEnabled(con)
        self.lineEdit_pattern_fade_in_L_3.setEnabled(con)
        self.lineEdit_pattern_fade_in_L_4.setEnabled(con)

        self.lineEdit_pattern_fade_in_R_1.setEnabled(con)
        self.lineEdit_pattern_fade_in_R_2.setEnabled(con)
        self.lineEdit_pattern_fade_in_R_3.setEnabled(con)
        self.lineEdit_pattern_fade_in_R_4.setEnabled(con)

        self.lineEdit_pattern_start_L_1.setEnabled(con)
        self.lineEdit_pattern_start_L_2.setEnabled(con)
        self.lineEdit_pattern_start_L_3.setEnabled(con)
        self.lineEdit_pattern_start_L_4.setEnabled(con)

        self.lineEdit_pattern_start_R_1.setEnabled(con)
        self.lineEdit_pattern_start_R_2.setEnabled(con)
        self.lineEdit_pattern_start_R_3.setEnabled(con)
        self.lineEdit_pattern_start_R_4.setEnabled(con)



    def set_changeBox_able_R(self):
        if self.checkBox_R_1.isChecked():
            self.checkBox_R_1.setEnabled(1)
        else:
            self.checkBox_R_2.setChecked(0)
            self.checkBox_R_2.setEnabled(0)

        if self.checkBox_R_2.isChecked():
            self.checkBox_R_2.setEnabled(1)
        else:
            self.checkBox_R_3.setChecked(0)
            self.checkBox_R_3.setEnabled(0)

        if self.checkBox_R_3.isChecked():
            self.checkBox_R_3.setEnabled(1)
        else:
            self.checkBox_R_4.setChecked(0)
            self.checkBox_R_4.setEnabled(0)

    def set_change_able(self):
        if self.radioButton_1.isChecked():
            self.checkBox_L_1.setEnabled(1)
            self.checkBox_R_1.setEnabled(1)
            # self.set_L_1_able_all(1)
            # self.set_R_1_able_all(1)
            # self.set_all_able(True)
        else:
            self.set_box_able(False)
            self.set_all_able(False)

    def load(self):
        qmessagebox = QMessageBox()

        if self.lineEdit_operater.text() == '':
            qmessagebox.warning(self, '警告', '请输入操作员姓名')
            return

        if self.lineEdit_date.text() == '':
            qmessagebox.warning(self, '警告', '请输入日期')
            return

        filePathLoad = os.path.dirname(os.path.realpath(sys.executable))
        # print(1)
        file = 'D:\pattern\动作修复 词目标注工具\词目动作原语模板标注工具 关键字段表格.xls'  # 文件路径
        try:
            wb = xlrd.open_workbook(filename=file)  # 用方法打开该文件路径下的文件
        except:
            qmessagebox.warning(self, '警告', '文件打开失败，请检查姓名、日期、表格是否被占用')
            return
        ws = wb.sheet_by_name("Sheet1")  # 打开该表格里的表单
        # print(1)
        for r in range(ws.nrows):  # 遍历行
            col = []
            for l in range(ws.ncols):  # 遍历列
                col.append(ws.cell(r, l).value)  # 将单元格中的值加入到列表中(r,l)相当于坐标系，cell（）为单元格，value为单元格的值
            dataBase.append(col)
        pprint(dataBase[0])
        self.label_load_con.setText('已导入')

    def save(self):
        qmessagebox = QMessageBox()

        prices = {
            'ACME': 45.23,
            'AAPL': 612.78,
            'IBM': 205.55,
            'HPQ': 37.20,
            'FB': 10.75
        }

        # with open('D:\pattern\动作修复 词目标注工具\output.json', 'w') as f:
            # json.dump(prices, f)
        workbook = xlwt.Workbook(encoding='utf-8')
        ws = workbook.add_sheet("Sheet1")
        rows = len(dataBase)
        lines = len(dataBase[0])
        for i in range(rows):
            for j in range(lines):
                ws.write(i, j, dataBase[i][j])
        try:
            workbook.save('D:\pattern\动作修复 词目标注工具\词目动作原语模板标注工具 关键字段表格.xls')
        except:
            qmessagebox.warning(self, '警告', '文件保存失败请检查姓名、日期、表格是否被占用')
            return
        self.load()
        qmessagebox.about(self, '保存文件', '保存成功')

    def glossNext(self):
        return

    def glossprev(self):
        return

    def toIndex(self):
        return

    def checkCon(self):
        qmessagebox = QMessageBox()
        if self.radioButton_1.isChecked() + self.radioButton_2.isChecked() + self.radioButton_3.isChecked() == 0:
            qmessagebox.warning(self, '警告', '请至少选择一项处理意见')
            return 0
        return 1

    def openVideo(self):
        class Video(object):
            def __init__(self, path):
                self.path = path

            def play(self):
                from os import startfile
                startfile(self.path, "open")

        class Movie_MP4(Video):
            type = 'MP4'  # 此处以MP4格式为例


        movie = Movie_MP4(r'D:\pattern\video\1_1_阿昌族.mp4')
        movie.play()

    def set_link_able_L(self):
        if self.checkBox_L_1.isChecked():
            self.checkBox_L_2.setEnabled(1)
            # self.set_L_2_able_all(1)
        else:
            self.checkBox_L_2.setChecked(0)
            self.checkBox_L_2.setEnabled(0)
            self.set_L_2_able_all(0)
        if self.checkBox_L_2.isChecked():
            # self.set_L_3_able_all(1)
            self.checkBox_L_3.setEnabled(1)
        else:
            self.checkBox_L_3.setChecked(0)
            self.checkBox_L_3.setEnabled(0)
            self.set_L_3_able_all(0)

        if self.checkBox_L_3.isChecked():
            self.checkBox_L_4.setEnabled(1)
            # self.set_L_4_able_all(1)
        else:
            self.checkBox_L_4.setChecked(0)
            self.checkBox_L_4.setEnabled(0)
            self.set_L_4_able_all(0)

    def set_L_1_able_all(self, con: bool):
        self.lineEdit_pattern_index_L_1.setEnabled(con)
        self.lineEdit_pattern_fade_in_L_1.setEnabled(con)
        self.lineEdit_pattern_end_L_1.setEnabled(con)
        self.lineEdit_pattern_fade_out_L_1.setEnabled(con)
        self.lineEdit_pattern_start_L_1.setEnabled(con)

    def set_L_1_able(self):
        if self.checkBox_L_1.isChecked():
            self.set_L_1_able_all(True)
        else:
            self.set_L_1_able_all(False)
        self.set_link_able_L()

    def set_L_2_able_all(self, con: bool):
        self.lineEdit_pattern_index_L_2.setEnabled(con)
        self.lineEdit_pattern_fade_in_L_2.setEnabled(con)
        self.lineEdit_pattern_end_L_2.setEnabled(con)
        self.lineEdit_pattern_fade_out_L_2.setEnabled(con)
        self.lineEdit_pattern_start_L_2.setEnabled(con)

    def set_L_2_able(self):
        if self.checkBox_L_2.isChecked():
            self.set_L_2_able_all(True)
        else:
            self.set_L_2_able_all(False)
        self.set_link_able_L()

    def set_L_3_able_all(self, con: bool):
        self.lineEdit_pattern_index_L_3.setEnabled(con)
        self.lineEdit_pattern_fade_in_L_3.setEnabled(con)
        self.lineEdit_pattern_end_L_3.setEnabled(con)
        self.lineEdit_pattern_fade_out_L_3.setEnabled(con)
        self.lineEdit_pattern_start_L_3.setEnabled(con)

    def set_L_3_able(self):
        if self.checkBox_L_3.isChecked():
            self.set_L_3_able_all(True)
        else:
            self.set_L_3_able_all(False)
        self.set_link_able_L()

    def set_L_4_able_all(self, con: bool):
        self.lineEdit_pattern_index_L_4.setEnabled(con)
        self.lineEdit_pattern_fade_in_L_4.setEnabled(con)
        self.lineEdit_pattern_end_L_4.setEnabled(con)
        self.lineEdit_pattern_fade_out_L_4.setEnabled(con)
        self.lineEdit_pattern_start_L_4.setEnabled(con)

    def set_L_4_able(self):
        if self.checkBox_L_4.isChecked():
            self.set_L_4_able_all(True)
        else:
            self.set_L_4_able_all(False)

        self.set_link_able_L()

    def set_link_able_R(self):
        if self.checkBox_R_1.isChecked():
            self.checkBox_R_2.setEnabled(1)
            # self.set_R_2_able_all(1)
        else:
            self.checkBox_R_2.setChecked(0)
            self.checkBox_R_2.setEnabled(0)
            self.set_R_2_able_all(0)
        if self.checkBox_R_2.isChecked():
            # self.set_R_3_able_all(1)
            self.checkBox_R_3.setEnabled(1)
        else:
            self.checkBox_R_3.setChecked(0)
            self.checkBox_R_3.setEnabled(0)
            self.set_R_3_able_all(0)

        if self.checkBox_R_3.isChecked():
            self.checkBox_R_4.setEnabled(1)
            # self.set_R_4_able_all(1)
        else:
            self.checkBox_R_4.setChecked(0)
            self.checkBox_R_4.setEnabled(0)
            self.set_R_4_able_all(0)

    def set_R_1_able_all(self, con: bool):
        self.lineEdit_pattern_index_R_1.setEnabled(con)
        self.lineEdit_pattern_fade_in_R_1.setEnabled(con)
        self.lineEdit_pattern_end_R_1.setEnabled(con)
        self.lineEdit_pattern_fade_out_R_1.setEnabled(con)
        self.lineEdit_pattern_start_R_1.setEnabled(con)

    def set_R_1_able(self):
        if self.checkBox_R_1.isChecked():
            self.set_R_1_able_all(True)
        else:

            self.set_R_1_able_all(False)

        self.set_link_able_R()

    def set_R_2_able_all(self, con: bool):
        self.lineEdit_pattern_index_R_2.setEnabled(con)
        self.lineEdit_pattern_fade_in_R_2.setEnabled(con)
        self.lineEdit_pattern_end_R_2.setEnabled(con)
        self.lineEdit_pattern_fade_out_R_2.setEnabled(con)
        self.lineEdit_pattern_start_R_2.setEnabled(con)

    def set_R_2_able(self):
        if self.checkBox_R_2.isChecked():
            self.set_R_2_able_all(True)
        else:
            self.set_R_2_able_all(False)

        self.set_link_able_R()

    def set_R_3_able_all(self, con: bool):
        self.lineEdit_pattern_index_R_3.setEnabled(con)
        self.lineEdit_pattern_fade_in_R_3.setEnabled(con)
        self.lineEdit_pattern_end_R_3.setEnabled(con)
        self.lineEdit_pattern_fade_out_R_3.setEnabled(con)
        self.lineEdit_pattern_start_R_3.setEnabled(con)

    def set_R_3_able(self):
        if self.checkBox_R_3.isChecked():
            self.set_R_3_able_all(True)
        else:
            self.set_R_3_able_all(False)

        self.set_link_able_R()

    def set_R_4_able_all(self, con: bool):
        self.lineEdit_pattern_index_R_4.setEnabled(con)
        self.lineEdit_pattern_fade_in_R_4.setEnabled(con)
        self.lineEdit_pattern_end_R_4.setEnabled(con)
        self.lineEdit_pattern_fade_out_R_4.setEnabled(con)
        self.lineEdit_pattern_start_R_4.setEnabled(con)

    def set_R_4_able(self):
        if self.checkBox_R_4.isChecked():
            self.set_R_4_able_all(True)
        else:
            self.set_R_4_able_all(False)

        self.set_link_able_R()

if __name__ == '__main__':
    # dataBase_csv = csv.reader(open(r'D:\UI\word_box\data\data_w_rep.csv', 'r'))
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()

    sys.exit(app.exec_())
