import sys
from itertools import permutations

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QDialog

from twenty_count_ui import Ui_dialog


class subUi(QDialog, Ui_dialog):
    def __init__(self, parent=None):
        super(subUi, self).__init__(parent)
        self.setupUi(self)
        regx1 = QRegExp("^[0-9]{3}$")
        validator1 = QRegExpValidator(regx1, self.lineEdit)
        self.lineEdit.setValidator(validator1)
        validator2 = QRegExpValidator(regx1, self.lineEdit_2)
        self.lineEdit_2.setValidator(validator2)
        validator3 = QRegExpValidator(regx1, self.lineEdit_3)
        self.lineEdit_3.setValidator(validator3)
        validator4 = QRegExpValidator(regx1, self.lineEdit_4)
        self.lineEdit_4.setValidator(validator4)

        self.pushButton.clicked.connect(self.count_twenty_four)

    def count_twenty_four(self):
        # 输入检查
        # if self.lineEdit.text() != '':
        #     if int(self.lineEdit.text()) > 13:
        #         self.textBrowser.setText('')
        #         self.textBrowser.setText(self.lineEdit.objectName() + '大于13，请重新输入！')
        #         return
        #     else:
        #         pass
        #
        # if self.lineEdit_2.text() != '':
        #     if int(self.lineEdit_2.text()) > 13:
        #         self.textBrowser.setText('')
        #         self.textBrowser.setText(self.lineEdit_2.objectName() + '大于13，请重新输入！')
        #         return
        #     else:
        #         pass
        #
        # if self.lineEdit_3.text() != '':
        #     if int(self.lineEdit_3.text()) > 13:
        #         self.textBrowser.setText('')
        #         self.textBrowser.setText(self.lineEdit_3.objectName() + '大于13，请重新输入！')
        #         return
        #     else:
        #         pass
        #
        # if self.lineEdit_4.text() != '':
        #     if int(self.lineEdit_4.text()) > 13:
        #         self.textBrowser.setText('')
        #         self.textBrowser.setText(self.lineEdit_4.objectName() + '大于13，请重新输入！')
        #         return
        #     else:
        #         pass
        #
        # else:
        #     self.textBrowser.setText('')
        #     self.textBrowser.setText('输入不能为空！')
        #     return

        a = self.lineEdit.text()
        b = self.lineEdit_2.text()
        c = self.lineEdit_3.text()
        d = self.lineEdit_4.text()
        self.twenty_four_cal(a, b, c, d)

    def twenty_four_cal(self, a, b, c, d):
        list1 = [a, b, c, d]
        list2 = []
        for i in range(1, len(list1) + 1):
            iteraa = permutations(list1, i)
            list2.append(list(iteraa))

        sta_list = list2[-1]
        print(sta_list)
        listsig = ['+', '+', '+', '-', '-', '-', '*', '*', '*', '/', '/', '/']

        # listsig = ['+', '+', '+', '-', '-', '-', '*', '*', '*', '/', '/', '/', '**', '**', '**']
        combins = [c for c in permutations(listsig, 3)]
        print(combins[-50:])

        kuohao = [['(', ')', '', ''],
                  ['(', '', ')', ''],
                  ['(', ')', '(', ')'],
                  ['((', ')', ')', '']]
        tot_sta = []
        for i in sta_list:
            for j in kuohao:
                ori_list = [i[0], i[1], i[2], i[3]]
                for k in range(0, 4):
                    if j[k] != '':
                        if j[k] == '(' or j[k] == '((':
                            ori_list[k] = j[k] + ori_list[k]
                        elif j[k] == ')' or j[k] == '))':
                            ori_list[k] = ori_list[k] + j[k]
                    else:
                        pass
                tot_sta.append(ori_list)
        final_list = []
        for i in tot_sta:
            for j in combins:
                temp = i[0] + j[0] + i[1] + j[1] + i[2] + j[2] + i[3]
                final_list.append(temp)

        # 去重

        final_list_2 = []
        for i in final_list:
            if i in final_list_2:
                pass
            else:
                final_list_2.append(i)

        cal_re_list = []

        for i in final_list_2:
            try:
                exec('cal_result = ' + i)
                # exec('print(i + " = " + str(cal_result))')
                exec('cal_re_list.append(cal_result)')
            except Exception as e:
                exec('cal_re_list.append("None")')
                pass

        self.textBrowser.setText('')
        for i in range(len(cal_re_list)):
            if cal_re_list[i] == 24:
                self.textBrowser.append(final_list_2[i] + ' = 24 \n')
                # self.textBrowser.moveCursor(QTextCursor.End)

            if 24 not in cal_re_list:
                self.textBrowser.setText('没有办法呀，我算不出来...')
