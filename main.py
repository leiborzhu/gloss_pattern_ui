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
import time
from pprint import pprint  # pprint的输出形式为一行输出一个结果，下一个结果换行输出。实质上pprint输出的结果更为完整
import json
import pandas as pd
import os
from os import startfile
import csv
from Dialog import Ui_Dialog
from Dialog_hint import Ui_Dialog_hint
from Dialog_check import Ui_Dialog_proof

dataBase = []
key_label = []
data_dict_oneLine = {}
dataGroup = []
saveCon = 0
index_cur = 0
indexDict = {}
from Alise import *

rootPath = os.path.dirname(os.path.realpath(sys.executable))
rem_tmp = []


class ProofWindow(QDialog, Ui_Dialog_proof):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.WindowMinimizeButtonHint)
        self.setupUi(self)

        self.pushButton_proof_yes.clicked.connect(self.yes)

        self.errBox = [errHandAlise, errRetarAlise, errPerformAlise, errRestAlise]
        for i in range(len(self.errBox)):
            if dataGroup[index_cur][self.errBox[i]] != '' and dataGroup[index_cur][self.errBox[i]]:
               exec('self.radioButton_res_' + str(i + 1) + '.setChecked(1)')
        if dataGroup[index_cur][videoConAlise] != '':
            if int(dataGroup[index_cur][videoConAlise]) == 1:
                self.radioButton_res_0.setChecked(True)
        self.textEdit_proof.setText(dataGroup[index_cur]['proofremark'])

        self.radioButton_res_0.clicked.connect(self.exclude)
        self.radioButton_res_1.clicked.connect(self.cancelCorrect)
        self.radioButton_res_2.clicked.connect(self.cancelCorrect)
        self.radioButton_res_3.clicked.connect(self.cancelCorrect)
        self.radioButton_res_4.clicked.connect(self.cancelCorrect)

    def yes(self):
        qmessagebox = QMessageBox()
        checkBox = [
            self.radioButton_res_0.isChecked(),
            self.radioButton_res_1.isChecked(),
            self.radioButton_res_2.isChecked(),
            self.radioButton_res_3.isChecked(),
            self.radioButton_res_4.isChecked()
        ]
        if sum(checkBox) == 0:
            qmessagebox.warning(self, '警告', '请至少选择一个评价')
            return
        if self.radioButton_res_0.isChecked():
            dataGroup[index_cur][videoConAlise] = 1
        else:
            dataGroup[index_cur][videoConAlise] = 2

        if self.radioButton_res_4.isChecked() and self.textEdit_proof.toPlainText() == '':
            qmessagebox.warning(self, '警告', '请写明相关理由')
            return

        for i in range(len(checkBox) - 1):
            if checkBox[i + 1]:
                dataGroup[index_cur][self.errBox[i]] = 1
            else:
                dataGroup[index_cur][self.errBox[i]] = 0
        if self.radioButton_res_4.isChecked():
            dataGroup[index_cur]['proofremark'] = self.textEdit_proof.toPlainText()
        else:
            dataGroup[index_cur]['proofremark'] = ''
            self.textEdit_proof.setText('')

        qmessagebox.warning(self, '警告', '设置成功，请注意保存')
        self.close()

    def cancelCorrect(self):
        self.radioButton_res_0.setChecked(False)

    def exclude(self):
        if self.radioButton_res_0.isChecked():
            self.radioButton_res_1.setChecked(False)
            self.radioButton_res_2.setChecked(False)
            self.radioButton_res_3.setChecked(False)
            self.radioButton_res_4.setChecked(False)

    def showDialog(self):
        self.show()


class HintWindow(QDialog, Ui_Dialog_hint):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.WindowMinimizeButtonHint)
        self.setupUi(self)

        self.pushButton_back.clicked.connect(self.back)
        self.textEdit_hint.setText(dataGroup[index_cur][describeAlise])

    def back(self):
        self.close()

    def showDialog(self):
        self.show()


class DialogWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.WindowMinimizeButtonHint)
        self.setupUi(self)

        self.pushButton_yes.clicked.connect(self.yes)
        self.pushButton_no.clicked.connect(self.no)
        self.textEdit.setText(rem_tmp)

    def yes(self):
        global rem_tmp
        rem_tmp = self.textEdit.toPlainText()
        self.close()

    def no(self):
        global rem_tmp
        rem_tmp = dataGroup[index_cur][remarkAlise]
        self.close()

    def showDialog(self):
        self.show()


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.WindowMinimizeButtonHint)
        self.setFixedSize(1366, 768)
        self.setupUi(self)
        self.set_all_able(False)
        self.set_box_able(False)
        self.pushButton_next.clicked.connect(self.glossNext)
        self.pushButton_prev.clicked.connect(self.glossprev)
        self.pushButton_toIndex.clicked.connect(self.toIndex)
        self.pushButton_load.clicked.connect(self.load)
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_video_res.clicked.connect(self.open_video_res)
        self.pushButton_video_after.clicked.connect(self.open_video_after)
        self.pushButton_readme.clicked.connect(self.readme)
        self.pushButton_output.clicked.connect(self.output)
        self.pushButton_hint.clicked.connect(self.hint)

        self.radioButton_1.clicked.connect(self.set_change_able)
        self.radioButton_2.clicked.connect(self.set_change_able)
        self.radioButton_3.clicked.connect(self.set_change_able)

        for strHand in ['L', 'R']:
            for index in range(1, 5):
                exec('self.checkBox_' + strHand + '_' + str(index) + '.clicked.connect(self.set_' + strHand + '_' + str(index) + '_able)')
        '''
        self.checkBox_L_1.clicked.connect(self.set_box_able_line(strHand: str, index: int):)
        ...................
        '''

        self.checkBox_checkMode.clicked.connect(self.changeMode)

        boxGroup = ['start', 'index', 'end', 'fade_out', 'fade_in']
        for strHand in ['L', 'R']:
            for index in range(1, 5):
                for strBox in boxGroup:
                    exec('self.lineEdit_pattern_' + strBox + '_' + strHand + '_' + str(index) + \
                         '.textChanged.connect(self.saveCondiChange)')
        '''
        self.lineEdit_pattern_start_L_1.textChanged.connect(self.saveCondiChange)
        .....................
        '''

    def set_box_able(self, con: bool):
        self.checkBox_L_1.setEnabled(con)
        self.checkBox_L_2.setEnabled(con)
        self.checkBox_L_3.setEnabled(con)
        self.checkBox_L_4.setEnabled(con)

        self.checkBox_R_1.setEnabled(con)
        self.checkBox_R_2.setEnabled(con)
        self.checkBox_R_3.setEnabled(con)
        self.checkBox_R_4.setEnabled(con)

    def set_box_check(self, con: bool):
        self.checkBox_L_1.setChecked(con)
        self.checkBox_L_2.setChecked(con)
        self.checkBox_L_3.setChecked(con)
        self.checkBox_L_4.setChecked(con)

        self.checkBox_R_1.setChecked(con)
        self.checkBox_R_2.setChecked(con)
        self.checkBox_R_3.setChecked(con)
        self.checkBox_R_4.setChecked(con)

    def set_all_able(self, con: bool):
        # self.set_L_1_able_all(con)
        self.set_box_able_all(con, 'L', 1)
        self.set_box_able_all(con, 'L', 2)
        self.set_box_able_all(con, 'L', 3)
        self.set_box_able_all(con, 'L', 4)

        self.set_box_able_all(con, 'R', 1)
        self.set_box_able_all(con, 'R', 2)
        self.set_box_able_all(con, 'R', 3)
        self.set_box_able_all(con, 'R', 4)

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

    # 选择是否修改时改变状态
    def set_change_able(self):
        if self.checkBox_checkMode.isChecked():
            self.checkBox_L_1.setEnabled(True)
            self.checkBox_R_1.setEnabled(True)
            if self.radioButton_1.isChecked():
                self.set_link_able_R()
                self.set_link_able_L()
                for strHand in ['L', 'R']:
                    for index in range(1, 5):
                        if eval('self.checkBox_' + strHand + '_' + str(index) + '.isChecked()'):
                            exec('self.set_box_able_all(True, strHand, index)')
                '''
                if self.checkBox_L_1.isChecked():
                    set_box_able_all(True, strHand, index)
                ...................
                '''
            else:
                self.set_box_able(False)
                self.set_all_able(False)

        else:
            if self.radioButton_1.isChecked():
                self.checkBox_L_1.setEnabled(1)
                self.checkBox_R_1.setEnabled(1)
                self.set_link_able_R()
                self.set_link_able_L()
                for strHand in ['L', 'R']:
                    for index in range(1, 5):
                        if eval('self.checkBox_' + strHand + '_' + str(index) + '.isChecked()'):
                            exec('self.set_box_able_all(True, strHand, index)')
                '''
                if self.checkBox_L_1.isChecked():
                    set_box_able_all(True, strHand, index)
                    .........................
                '''
            else:
                self.set_box_able(False)
                self.set_all_able(False)

        global saveCon
        saveCon = 0
        self.label_save_condi.setText('未保存')
    # 更新界面，数据状态
    def refresh(self, index_cur):

        global saveCon
        global rem_tmp
        saveCon = 0
        self.label_save_condi.setText('未保存')
        lineCur = dataGroup[index_cur]

        self.label_gloss.setText(str(lineCur[glossAlise]))
        self.label_gloss_index.setText(str(int(lineCur[indexAlise])))
        rem_tmp = lineCur[remarkAlise]

        # 根据数据更新界面
        def contUpdate():
            lineCur = dataGroup[index_cur]
            alsGroup = ['patterAlise', 'startAlise', 'endAlise', 'fadeInAlise', 'fadeOutAlise']
            boxGroup = ['index', 'start', 'end', 'fade_in', 'fade_out']
            for strHand in ['L', 'R']:
                for index in range(1, 5):

                    checkLine = 'str(lineCur[patterAlise_' + strHand + '_' + str(index) + ']) != ""'
                    if eval(checkLine):
                        exec('self.checkBox_' + strHand + '_' + str(index) + '.setChecked(1)')
                        exec('self.checkBox_' + strHand + '_' + str(index) + '.setEnabled(1)')
                        for i in range(len(alsGroup)):
                            line = 'self.lineEdit_pattern_' + boxGroup[i] + '_' + strHand + '_' + str(index) + \
                                   '.setText(str(int(lineCur[' + alsGroup[i] + '_' + strHand + '_' + str(index) + '])))'
                            exec(line)
                    else:
                        exec('self.checkBox_' + strHand + '_' + str(index) + '.setChecked(0)')
                        self.clearBox(strHand, index)
                    exec('self.set_' + strHand + '_' + str(index) + '_able()')
            '''
            if str(lineCur[patterAlise_L_1]) != '':
                self.checkBox_L_1.setChecked(1)
                self.checkBox_L_1.setEnabled(1)
                self.lineEdit_pattern_index_L_1.setText(str(int(lineCur[patterAlise_L_1])))
                self.lineEdit_pattern_start_L_1.setText(str(int(lineCur[startAlise_L_1])))
                self.lineEdit_pattern_end_L_1.setText(str(int(lineCur[endAlise_L_1])))
                self.lineEdit_pattern_fade_in_L_1.setText(str(int(lineCur[fadeInAlise_L_1])))
                self.lineEdit_pattern_fade_out_L_1.setText(str(int(lineCur[fadeOutAlise_L_1])))
            else:
                self.checkBox_L_1.setChecked(0)
                self.clearBox('L', 1)

            self.set_L_1_able()
            ..................
            '''
        def updateInputCon():
            if str(lineCur[isCorrectAlise]) != '':
                if int(lineCur[isCorrectAlise] == 1):
                    contUpdate()
                    self.radioButton_1.setChecked(1)
                    self.checkBox_R_1.setEnabled(1)
                    self.checkBox_L_1.setEnabled(1)

                elif int(lineCur[isCorrectAlise] == 2):
                    self.radioButton_2.setChecked(1)
                    self.clearAll()

                else:
                    self.radioButton_3.setChecked(1)
                    self.clearAll()

            else:
                self.radioButton_3.setChecked(1)
                self.clearAll()

        if self.checkBox_checkMode.isChecked():
            contUpdate()
            if lineCur[isProofALise] == '':
                self.radioButton_3.setChecked(1)
            else:
                if int(lineCur[isProofALise]) == 1:
                    self.radioButton_1.setChecked(1)
                elif int(lineCur[isProofALise]) == 2:
                    self.radioButton_2.setChecked(1)
                else:
                    self.radioButton_3.setChecked(1)
            self.set_change_able()
        else:
            updateInputCon()


    def load(self):
        qmessagebox = QMessageBox()

        if self.label_load_con.text() == '已导入':
            qmessagebox.warning(self, '警告', '文件已导入')
            return

        if self.lineEdit_operater.text() == '':
            qmessagebox.warning(self, '警告', '请输入操作员姓名')
            return

        if self.lineEdit_reader.text() == '':
            qmessagebox.warning(self, '警告', '请输入校对员姓名')
            return

        # print(os.path.dirname(os.path.realpath(sys.executable)))
        filePathLoad = os.path.dirname(os.path.realpath(sys.executable))
        opName = self.lineEdit_operater.text().strip()
        reName = self.lineEdit_reader.text().strip()
        file = os.path.join(rootPath,
                            '词目动作原语模板分类标注工具_' + opName + '_' + reName + '.xls')
        # file = 'D:\pattern\动作修复 词目标注工具\词目动作原语模板标注工具 关键字段表格.xls'  # 文件路径
        try:
            wb = xlrd.open_workbook(filename=file)  # 用方法打开该文件路径下的文件
        except:
            qmessagebox.warning(self, '警告', '文件打开失败，请检查姓名、表格是否被占用')
            return
        ws = wb.sheet_by_name("Sheet1")  # 打开该表格里的表单

        for r in range(ws.nrows):  # 遍历行
            col = []
            for l in range(ws.ncols):  # 遍历列
                col.append(ws.cell(r, l).value)  # 将单元格中的值加入到列表中(r,l)相当于坐标系，cell（）为单元格，value为单元格的值
            dataBase.append(col)

        self.label_load_con.setText('已导入')

        for i in dataBase[0]:
            key_label.append(i)
            data_dict_oneLine[str(i)] = ''

        # print(data_dict_oneLine)
        for i in range(1, len(dataBase)):
            data_dict_line_tmp = data_dict_oneLine.copy()
            for j in range(len(key_label)):
                data_dict_line_tmp[key_label[j]] = dataBase[i][j]
            dataGroup.append(data_dict_line_tmp)
            indexDict[str(int(dataGroup[i - 1][indexAlise]))] = i - 1

        index_cur = 0
        self.refresh(index_cur)

        def buttom_check():
            self.pushButton_save.setEnabled(1)
            self.pushButton_prev.setEnabled(1)
            self.pushButton_next.setEnabled(1)
            self.pushButton_video_res.setEnabled(1)
            self.pushButton_video_after.setEnabled(1)
            self.pushButton_output.setEnabled(1)
            self.pushButton_toIndex.setEnabled(1)
            self.pushButton_readme.setEnabled(1)
            self.pushButton_hint.setEnabled(1)

            self.radioButton_1.setEnabled(1)
            self.radioButton_2.setEnabled(1)
            self.radioButton_3.setEnabled(1)

            self.lineEdit_operater.setEnabled(0)
            self.lineEdit_reader.setEnabled(0)

            self.checkBox_checkMode.setEnabled(1)

        buttom_check()

        qmessagebox.about(self, '导入数据', '导入成功')

    def clearAll(self):
        self.set_box_able(False)
        self.set_all_able(False)
        self.set_box_check(False)
        for i in range(1, 5):
            self.clearBox('L', i)
            self.clearBox('R', i)

    def dataUpdate(self) -> bool:
        qmessagebox = QMessageBox()
        # 添加操作者
        if self.lineEdit_operater.text() == '':
            qmessagebox.warning(self, '警告', '请输入操作者姓名')
            return
        else:
            dataGroup[index_cur][operatorAlise] = self.lineEdit_operater.text()
        dataGroup[index_cur][readerAlise] = self.lineEdit_reader.text()
        def clear_and_load():
            self.clearAll()
            for i in key_label:
                if i in optional_label:
                    dataGroup[index_cur][i] = ''
                self.set_box_able(False)

        def allupdate():
            aliseGroup = ['patterAlise', 'startAlise', 'endAlise', 'fadeInAlise', 'fadeOutAlise']
            boxGroup = ['index', 'start', 'end', 'fade_in', 'fade_out']
            for handStr in ['L', 'R']:
                for index in range(1, 5):
                    for i in range(len(aliseGroup)):
                        line1 = 'dataGroup[index_cur][' + aliseGroup[i] + '_' + handStr + '_' + str(index) + ']'
                        lineCheck = 'self.checkBox_' + handStr + '_' + str(index) + '.isChecked()'
                        if eval(lineCheck):
                            line2 = '=float(self.lineEdit_pattern_' + boxGroup[i] + '_' + handStr + '_' + \
                                    str(index) + '.text())'
                        else:
                            line2 = "=''"
                            self.clearBox(handStr, index)

                        exec(line1 + line2)
            '''        
            if self.checkBox_L_1.isChecked():
                dataGroup[index_cur][patterAlise_L_1] = float(self.lineEdit_pattern_index_L_1.text())
                dataGroup[index_cur][startAlise_L_1] = float(self.lineEdit_pattern_start_L_1.text())
                dataGroup[index_cur][endAlise_L_1] = float(self.lineEdit_pattern_end_L_1.text())
                dataGroup[index_cur][fadeInAlise_L_1] = float(self.lineEdit_pattern_fade_in_L_1.text())
                dataGroup[index_cur][fadeOutAlise_L_1] = float(self.lineEdit_pattern_fade_out_L_1.text())
            else:
                dataGroup[index_cur][patterAlise_L_1] = ''
                .........
                self.clearBox('L', 1)
            ................
                '''
        if self.checkBox_checkMode.isChecked():
            if dataGroup[index_cur][videoConAlise] == '':
                qmessagebox.warning(self, '警告', '请评估视频质量')
                return False
            if self.radioButton_3.isChecked():
                qmessagebox.warning(self, '警告', '请校对标注结果')
                return False

            if self.radioButton_1.isChecked():
                dataGroup[index_cur][isProofALise] = 1
                allupdate()
            elif self.radioButton_2.isChecked():
                dataGroup[index_cur][isProofALise] = 2

        else:
            if self.radioButton_1.isChecked():
                dataGroup[index_cur][isCorrectAlise] = 1
                allupdate()
            elif self.radioButton_2.isChecked():
                dataGroup[index_cur][isCorrectAlise] = 2
                clear_and_load()
            elif self.radioButton_3.isChecked():
                dataGroup[index_cur][isCorrectAlise] = 3
                clear_and_load()

        dataGroup[index_cur][remarkAlise] = rem_tmp

        # 添加日期
        t = time.localtime()
        dataGroup[index_cur][dateAlise] = str(t.tm_mon) + '_' + str(t.tm_mday)

        return True

    def clearBox(self, hand: str, index: int):
        for strType in ['index', 'start', 'end', 'fade_in', 'fade_out']:
            line = 'self.lineEdit_pattern_' + strType + '_' + hand + '_' + str(index) + r'.setText("")'
            exec(line)

    def save(self):
        qmessagebox = QMessageBox()

        workbook = xlwt.Workbook(encoding='utf-8')
        ws = workbook.add_sheet("Sheet1")

        if not self.check_isnum_valid():
            return

        if not self.dataUpdate():
            return

        # 检查需修改的情况下是否有动作信息
        if not self.check_isChecked():
            return

        if not self.check_frame_valid():
            return

        rows = len(dataBase)
        lines = len(dataBase[0])

        for i in range(rows):
            for j in range(lines):
                if i != 0:
                    dataBase[i][j] = dataGroup[i - 1][key_label[j]]
                ws.write(i, j, dataBase[i][j])
        try:
            opName = self.lineEdit_operater.text().strip()
            reName = self.lineEdit_reader.text().strip()
            file = os.path.join(rootPath,
                                '词目动作原语模板分类标注工具_' + opName + '_' + reName + '.xls')

            workbook.save(file)
        except:
            qmessagebox.warning(self, '警告', '文件保存失败,请检查姓名、日期、表格是否被占用')
            return
        # self.load()
        qmessagebox.about(self, '保存文件', '保存成功')

        self.label_save_condi.setText("文件已保存")
        global saveCon
        saveCon = 1

    def saveConti(self) -> bool:
        qmessagebox = QMessageBox()
        global saveCon
        if saveCon == 1:
            return True
        else:
            reply = QMessageBox.question(self, '警告', '数据未保存,是否继续', QMessageBox.Yes | QMessageBox.No)
            return reply == QMessageBox.Yes

    def check_isChecked(self) -> bool:
        qmessagebox = QMessageBox()
        if dataGroup[index_cur][isCorrectAlise] != '':
            if not self.checkBox_checkMode.isChecked() and self.radioButton_1.isChecked():
                haveChecked = self.checkBox_L_1.isChecked() + self.checkBox_R_1.isChecked()
                # print(haveChecked)
                if not haveChecked:
                    qmessagebox.warning(self, '警告', '请至少填入一个动作')
                    return False
        return True

    def changeMode(self):
        qmessagebox = QMessageBox()
        if self.checkBox_checkMode.isChecked():
            qmessagebox.warning(self, '提示', '进入校对模式')
            self.radioButton_1.setText('需修改')
            self.radioButton_2.setText('标注通过')
            self.radioButton_3.setText('未校对')
            self.pushButton_readme.setText('视频评估')

        else:
            qmessagebox.warning(self, '提示', '进入录入模式')
            self.radioButton_1.setText('需修改')
            self.radioButton_2.setText('不确定')
            self.radioButton_3.setText('未处理')
            self.pushButton_readme.setText('添加备注')

        self.refresh(index_cur)

    def check_isnum_valid(self) -> bool:
        qmessagebox = QMessageBox()
        boxGroup = ['index', 'fade_in', 'fade_out', 'start', 'end']
        blankCon_isnum = []
        for strHand in ['L', 'R']:
            for index in range(1, 5):
                if eval('self.checkBox_' + strHand + '_' + str(index) + '.isChecked()'):
                    blankCon_isnum = []
                    for box in boxGroup:
                        exec('blankCon_isnum.append(not self.lineEdit_pattern_' + box + '_' + strHand + '_' +
                            str(index) + '.text().isnumeric())')

                    if eval('sum(blankCon_isnum) != 0'):
                        exec('qmessagebox.warning(self, "警告", "动作" + strHand + str(index) + "填写不规范")')
                        return False

        '''if self.checkBox_L_1.isChecked():
            blankCon_L_1_isnum = [
                not self.lineEdit_pattern_index_L_1.text().isnumeric(),
                not self.lineEdit_pattern_fade_in_L_1.text().isnumeric(),
                not self.lineEdit_pattern_fade_out_L_1.text().isnumeric(),
                not self.lineEdit_pattern_start_L_1.text().isnumeric(),
                not self.lineEdit_pattern_end_L_1.text().isnumeric(),
            ]
            if sum(blankCon_L_1_isnum) != 0:
                qmessagebox.warning(self, '警告', '动作L1填写不规范')
                return False
            .......................................
        '''
        return True

    def check_frame_valid(self) -> bool:
        qmessagebox = QMessageBox()
        blankCon_frame_valid_tmp = []
        index_start = 1
        index_end = 61
        frameGap = 5
        for strHand in ['L', 'R']:
            for index in range(1, 5):
                if eval('self.checkBox_' + strHand + '_' + str(index) + '.isChecked()'):
                    blankCon_frame_valid_tmp = []
                    exec('blankCon_frame_valid_tmp.append(int(self.lineEdit_pattern_index_' +
                         strHand + '_' + str(index) + '.text().strip()) < index_start)')
                    exec('blankCon_frame_valid_tmp.append(int(self.lineEdit_pattern_index_' +
                         strHand + '_' + str(index) + '.text().strip()) > index_end)')
                    exec('blankCon_frame_valid_tmp.append(int(self.lineEdit_pattern_fade_in_' +
                         strHand + '_' + str(index) + '.text().strip()) < 0)')
                    exec('blankCon_frame_valid_tmp.append(int(self.lineEdit_pattern_start_' +
                         strHand + '_' + str(index) + '.text().strip()) <= int(self.lineEdit_pattern_fade_in_' +
                         strHand + '_' + str(index) + '.text().strip()) + frameGap)')
                    exec('blankCon_frame_valid_tmp.append(int(self.lineEdit_pattern_end_' +
                         strHand + '_' + str(index) + '.text().strip()) <= int(self.lineEdit_pattern_start_' +
                         strHand + '_' + str(index) + '.text().strip()) + frameGap)')
                    exec('blankCon_frame_valid_tmp.append(int(self.lineEdit_pattern_fade_out_' +
                         strHand + '_' + str(index) + '.text().strip()) <= int(self.lineEdit_pattern_end_' +
                         strHand + '_' + str(index) + '.text().strip()) + frameGap)')
                    exec('blankCon_frame_valid_tmp.append(int(self.lineEdit_pattern_fade_out_' +
                         strHand + '_' + str(index) + '.text().strip()) > dataGroup[index_cur][max_frameAlise])')
                # print(blankCon_frame_valid_tmp)
                if eval('sum(blankCon_frame_valid_tmp) != 0'):
                    exec('qmessagebox.warning(self, "警告", "动作" + strHand + str(index) + "帧数设置有误")')
                    return False

        '''if self.checkBox_L_1.isChecked():

            blankCon_L_1_frame_valid = [
                int(self.lineEdit_pattern_index_L_1.text().strip()) < index_start,
                int(self.lineEdit_pattern_index_L_1.text().strip()) > index_end,
                int(self.lineEdit_pattern_fade_in_L_1.text().strip()) < 0,
                int(self.lineEdit_pattern_start_L_1.text().strip()) <= int(self.lineEdit_pattern_fade_in_L_1.text().strip()),
                int(self.lineEdit_pattern_end_L_1.text().strip()) <= int(self.lineEdit_pattern_start_L_1.text().strip()),
                int(self.lineEdit_pattern_fade_out_L_1.text().strip()) <= int(self.lineEdit_pattern_end_L_1.text().strip()),
                int(self.lineEdit_pattern_fade_out_L_1.text().strip()) > dataGroup[index_cur][max_frameAlise]
            ]

            if sum(blankCon_L_1_frame_valid) != 0:
                qmessagebox.warning(self, '警告', '动作L1帧数设置有误')
                return False
            ....................................
        '''

        return True

    def glossNext(self):
        qmessagebox = QMessageBox()
        if not self.saveConti():
            return
        global index_cur
        if index_cur + 1 >= len(dataGroup):
            qmessagebox.warning(self, '警告', '没有下一个词')
            return
        index_cur += 1
        global saveCon
        saveCon = 1

        self.refresh(index_cur)

    def glossprev(self):
        qmessagebox = QMessageBox()
        if not self.saveConti():
            return
        global index_cur
        if index_cur == 0:
            qmessagebox.warning(self, '警告', '没有上一个词')
            return
        index_cur -= 1

        self.refresh(index_cur)

    def toIndex(self):
        global index_cur
        qmessagebox = QMessageBox()
        index_tmp = self.lineEdit_to_index.text()

        if not index_tmp.isnumeric():
            qmessagebox.warning(self, '警告', '请输入数字编号')
            return

        if str(self.lineEdit_to_index.text()) not in indexDict.keys():
            qmessagebox.warning(self, '警告', '无该编号对应的词')
            return

        if not self.saveConti():
            return
        index_cur = indexDict[self.lineEdit_to_index.text()]

        self.refresh(index_cur)

    def checkCon(self):
        qmessagebox = QMessageBox()
        if self.radioButton_1.isChecked() + self.radioButton_2.isChecked() == 0:
            qmessagebox.warning(self, '警告', '请至少选择一项处理意见')
            return 0
        return 1

    def open_video_res(self):
        qmessagebox = QMessageBox()

        class Video(object):
            def __init__(self, path):
                self.path = path

            def play(self):
                from os import startfile
                startfile(self.path, "open")

        class Movie_MP4(Video):
            type = 'MP4'  # 此处以MP4格式为例

        moviePath = os.path.join(rootPath, 'SourceVideo', str(int(dataGroup[index_cur][videoAlise_res])) + '.mp4')
        # print(rootPath)
        # movie = Movie_MP4(r'E:\之江\pattern\sourcevideo\00000001.mp4')
        try:
            movie = Movie_MP4(moviePath)
            movie.play()
        except:
            qmessagebox.warning(self, '警告', '视频打开失败')
            return

    def open_video_after(self):
        qmessagebox = QMessageBox()

        class Video(object):
            def __init__(self, path):
                self.path = path

            def play(self):
                from os import startfile
                startfile(self.path, "open")

        class Movie_MP4(Video):
            type = 'MP4'  # 此处以MP4格式为例

        def addZero(s: int) -> str:
            res = str(s)
            for _ in range(8 - len(str(s))):
                res = '0' + res
            return res
        moviePath = os.path.join(rootPath, 'SourceVideo', str(int(dataGroup[index_cur][videoAlise_aft])) + '.mp4')
        print(moviePath)
        # movie = Movie_MP4(r'E:\之江\pattern\sourcevideo\00000001.mp4')
        try:
            movie = Movie_MP4(moviePath)
            movie.play()
        except:
            qmessagebox.warning(self, '警告', '视频打开失败')
            return

    def set_box_able_all(self, con: bool, strHand: str, index: int):
        boxGroup = ['index', 'fade_in', 'end', 'fade_out', 'start']
        for box in boxGroup:
            exec('self.lineEdit_pattern_' + box + '_' + strHand + '_' + str(index) + '.setEnabled(con)')

    def set_box_able_line(self, strHand: str, index: int):
        exec("self.set_box_able_all(self.checkBox_" + strHand + "_" + str(index) + ".isChecked(), " + "strHand, " + str(index) + ")")
        exec("self.set_link_able_" + strHand + "()")

    # 绑定按钮函数
    def set_L_1_able(self):
        self.set_box_able_all(self.checkBox_L_1.isChecked(), 'L', 1)
        self.set_link_able_L()

    def set_L_2_able(self):
        self.set_box_able_all(self.checkBox_L_2.isChecked(), 'L', 2)
        self.set_link_able_L()

    def set_L_3_able(self):
        self.set_box_able_all(self.checkBox_L_3.isChecked(), 'L', 3)
        self.set_link_able_L()

    def set_L_4_able(self):
        self.set_box_able_all(self.checkBox_L_4.isChecked(), 'L', 4)
        self.set_link_able_L()

    def set_link_able_L(self):
        if self.checkBox_L_1.isChecked():
            self.checkBox_L_2.setEnabled(1)

        else:
            self.checkBox_L_2.setChecked(0)
            self.checkBox_L_2.setEnabled(0)
            self.set_box_able_all(False, 'L', 2)

        if self.checkBox_L_2.isChecked():
            self.checkBox_L_3.setEnabled(1)


        else:
            self.checkBox_L_3.setChecked(0)
            self.checkBox_L_3.setEnabled(0)
            self.set_box_able_all(False, 'L', 3)

        if self.checkBox_L_3.isChecked():
            self.checkBox_L_4.setEnabled(1)

        else:
            self.checkBox_L_4.setChecked(0)
            self.checkBox_L_4.setEnabled(0)
            self.set_box_able_all(False, 'L', 4)

    def set_R_1_able(self):
        self.set_box_able_all(self.checkBox_R_1.isChecked(), 'R', 1)
        self.set_link_able_R()

    def set_R_2_able(self):
        self.set_box_able_all(self.checkBox_R_2.isChecked(), 'R', 2)
        self.set_link_able_R()

    def set_R_3_able(self):
        self.set_box_able_all(self.checkBox_R_3.isChecked(), 'R', 3)
        self.set_link_able_R()

    def set_R_4_able(self):
        self.set_box_able_all(self.checkBox_R_4.isChecked(), 'R', 4)
        self.set_link_able_R()

    def set_link_able_R(self):
        if self.checkBox_R_1.isChecked():
            self.checkBox_R_2.setEnabled(1)
        else:
            self.checkBox_R_2.setChecked(0)
            self.checkBox_R_2.setEnabled(0)
            self.set_box_able_all(False, 'R', 2)

        if self.checkBox_R_2.isChecked():
            # self.set_R_3_able_all(1)
            self.checkBox_R_3.setEnabled(1)
        else:
            self.checkBox_R_3.setChecked(0)
            self.checkBox_R_3.setEnabled(0)
            self.set_box_able_all(False, 'R', 3)

        if self.checkBox_R_3.isChecked():
            self.checkBox_R_4.setEnabled(1)
            # self.set_R_4_able_all(1)
        else:
            self.checkBox_R_4.setChecked(0)
            self.checkBox_R_4.setEnabled(0)
            self.set_box_able_all(False, 'R', 4)

    def saveCondiChange(self):
        saveCon = 0
        self.label_save_condi.setText('未保存')

    def readme(self):
        global saveCon
        saveCon = 0
        self.label_save_condi.setText('未保存')
        if self.checkBox_checkMode.isChecked():
            self.dia = ProofWindow()
            self.dia.showDialog()
        else:
            self.dia = DialogWindow()
            self.dia.showDialog()

    def output(self):
        qmessagebox = QMessageBox()
        if saveCon == 0:
            qmessagebox.warning(self, '警告', '请先保存当前数据')
            return
        else:
            workbook = xlwt.Workbook(encoding='utf-8')
            ws = workbook.add_sheet("Sheet1")

            rows = len(dataBase)
            lines = len(dataBase[0])
            # print(rows)
            for i in range(rows):
                for j in range(lines):
                    if i != 0:
                        dataBase[i][j] = dataGroup[i - 1][key_label[j]]
                    ws.write(i, j, dataBase[i][j])
            try:
                t = time.localtime()
                file = os.path.join(rootPath,
                                    '词目动作原语模板分类标注工具' + '_' + self.lineEdit_operater.text() + '_' + str(t.tm_mon) + '_' + str(t.tm_mday) + '.xls')
                workbook.save(file)
            except:
                qmessagebox.warning(self, '警告', '文件保存失败,请检查姓名、日期、表格是否被占用')
                return
            # self.load()
            qmessagebox.about(self, '输出文件', '输出成功')

    def hint(self):
        self.hin = HintWindow()
        self.hin.showDialog()


if __name__ == '__main__':
    # dataBase_csv = csv.reader(open(r'D:\UI\word_box\data\data_w_rep.csv', 'r'))
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()

    sys.exit(app.exec_())
