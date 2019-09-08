

# Form implementation generated from reading ui file 'design.ui'                #-*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QMenu, QHBoxLayout,QWidget, QMessageBox
from pymongdb import TestMongo
import re,sys,you_get,webbrowser,os
import tkinter.messagebox as msgbox
from PyQt5.QtCore import QStringListModel,Qt
import webbrowser as web
class Ui_Dialog(QWidget):



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(781, 585)

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(430, 100, 93, 31))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(50, 100, 350, 31))
        self.textEdit.setObjectName("textEdit")

        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(60, 30, 231, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 100, 93, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton.clicked.connect(lambda :self.store())
        self.pushButton_2.clicked.connect(lambda: self.download())
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(50, 190, 650, 261))
        self.listView.setObjectName("listView")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 530, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 30, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        self.pushButton_3.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.qList = []     #所有网址
        conLayout = QHBoxLayout()


        self.listView.setContextMenuPolicy(Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.listView.customContextMenuRequested.connect(self.generateMenu)  ####右键菜单

        # self.setLayout(conLayout)




    def generateMenu(self, pos):
        print(len(self.qList))
        row_num = -1
        for i in self.listView.selectionModel().selection().indexes():
            row_num = i.row()

        if  row_num >=0 and row_num< len(self.qList):

            menu = QMenu()
            menu.addAction(u'删除', lambda: self.del_Item1(1))                  #action = menu.exec_(self.listView.mapToGlobal(pos)) #if action == item1:
            menu.addAction(u"扩展", lambda: self.del_Item2(1))
            menu.addAction(u"访问", lambda: self.del_Item3(1))
            action = menu.exec_(self.listView.mapToGlobal(pos))         #生成菜单
            #
            #     print ("delete")
            #
            #     print('您选了选项一，当前行文字内容是：', self.listView.item(row_num, 0).text(),
            #           self.listView.item(row_num, 1).text(), self.listView.item(row_num, 2).text())
            #
            # elif action == item2:
            #     print("你选择了", self.listView.model().stringList())
            #     # print('您选了选项二，当前行文字内容是：', self.listView.item(row_num, 0).text(),
            #     #       self.listView.item(row_num, 1).text(), self.listView.item(row_num, 2).text())
            #
            # elif action == item3:
            #     print(u"你选择了", self.listView.model().stringList())
            #     # print('您选了选项三，当前行文字内容是：', self.listView.item(row_num, 0).text(),
            #     #       self.listView.item(row_num, 1).text(), self.listView.item(row_num, 2).text())
            # else:
            #     return
    def del_Item1(self,type=1):
        print ("删除1")
        # for model_index in self.listView.selectionModel().selectedRows():
        #     index = QtCore.QPersistentModelIndex(model_index)
        #
        #     self.listView.removeRow(index.row())
    def del_Item2(self,type=1):
        index=self.listView.currentIndex()
        print (index.row())
        # self.qList.removeRow(index.row())
    def del_Item3(self,type=1):
        web.open_new("www.baidu.com")




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "QT"))
        self.pushButton.setText(_translate("Dialog", "保存"))
        self.pushButton_2.setText(_translate("Dialog", "下载"))

        self.pushButton_3.setText(_translate("Dialog", "关闭"))
        self.pushButton_4.setText(_translate("Dialog", "打开文件夹"))
    def store(self):                   #讲网址存入数据库
        if self.textEdit.toPlainText()=="":
            reply=QMessageBox.warning(self,'Message','网址为空，重新填写', QMessageBox.Yes ,QMessageBox.Yes)   #
            if reply==QMessageBox.Yes:
                return


        else :
            urltosave=self.textEdit.toPlainText()
            #if re.match(r'^https?:/{2}\w.+$', urltosave):
            save=TestMongo()
            save.save(urltosave)
            self.textEdit.clear()

            slm = QStringListModel()  # 创建mode


            self.qList.append(urltosave)
            slm.setStringList(self.qList)  # 将数据设置到model
            self.listView.setModel(slm)  ##绑定 listView 和 model


    def download(self):


        path='D:\\test'
        checkdict = TestMongo().read_line()
        for item in checkdict:

            # 正则表达是判定是否为合法链接
            # url = self.url.get()
            url = item["url"]
            #path = self.path.get()

            if re.match(r'^https?:/{2}\w.+$', url):
                if path != '':
                    msgbox.showwarning(title='警告', message='下载过程中窗口如果出现短暂卡顿说明文件正在下载中！')
                    try:
                        sys.argv = ['you-get', '-o', path, url]
                        you_get.main()
                    except Exception as e:
                        print(e)
                        msgbox.showerror(title='error', message=e)
                    msgbox.showinfo(title='info', message='下载完成！')
                else:
                    msgbox.showerror(title='error', message='输出地址错误！')
            else:
                msgbox.showerror(title='error', message='视频地址错误！')




