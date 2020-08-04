# -*-coding: utf-8 -*-
from PyQt5 import QtCore,QtGui,QtWidgets
import sys
import Main
import genSM2key
import os


#os.environ['PYTHON_VLC_MODULE_PATH'] = "./vlc-3.0.7.1"
import vlc


StyleSheet = """
    background: rgb(0,0,0);
    border: 1px solid #fff;
    border-radius: 10px;
"""
StyleSheet_one = """
    background: url('image/img.png') rgba(0,0,0,0);
    background-position: center;
    background-repeat: no-repeat;
    border: 0;
"""

StyleSheet_in = """
    background: rgba(0,0,0,0);
    border: 0;
"""

StyleSheet_min = """
QPushButton {
    background: url('image/min.png');
    width: 14px;
    height: 14px;
    margin-left: 2px;
    margin-right: 2px;
    background-repeat: no-repeat;
}
QPushButton:hover {
    background: url('image/min_c.png');
    background-repeat: no-repeat;
}
"""

StyleSheet_max = """
QPushButton {
    background: url('image/max.png');
    width: 14px;
    height: 14px;
    margin-left: 2px;
    margin-right: 2px;
    background-repeat: no-repeat;
}
"""

StyleSheet_close = """
QPushButton {
    background: url('image/close.png');
    width: 14px;
    height: 14px;
    margin-left: 2px;
    margin-right: 2px;
    background-repeat: no-repeat;
}
QPushButton:hover {
    background: url('image/close_c.png');
    background-repeat: no-repeat;
}
"""

StyleSheet_btn = """
QPushButton {
    background: white;
    width: 80px;
    height: 40px;
    border-radius: 20px;
    margin-left: 30px;
    margin-right: 30px;
}
QPushButton:hover {
    background: gray;
}
"""

StyleSheet_btn_c = """
QPushButton {
    background: white;
    width: 50px;
    height: 20px;
    border-radius: 10px;
    margin-left: 40px;
    margin-right: 40px;
}
QPushButton:hover {
    background: gray;
}
"""

StyleSheet_label = """
QLabel {
    color: #fff;
    font-size: 18px;
    font-family: SimHei;
    margin-top: 5px;
}
"""

StyleSheet_lineEdit = """
QLineEdit {
    background: #fff;
    margin-left: 5px;
}
"""

StyleSheet_btn_e = """
QPushButton {
    background: white;
    width: 30px;
    height: 15px;
    border-radius: 5px;
    margin-left: 5px;
    font-weight: 300
}
QPushButton:hover {
    background: gray;
}
"""



class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(600,300)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        
        self.one_widget = QtWidgets.QWidget()
        self.one_layout = QtWidgets.QGridLayout()
        self.one_widget.setLayout(self.one_layout)
        
        self.two_widget = QtWidgets.QWidget()
        self.two_layout = QtWidgets.QGridLayout()
        self.two_widget.setLayout(self.two_layout)
        
        self.three_widget = QtWidgets.QWidget()
        self.three_layout = QtWidgets.QGridLayout()
        self.three_widget.setLayout(self.three_layout)
        
        self.four_widget = QtWidgets.QWidget()
        self.four_layout = QtWidgets.QGridLayout()
        self.four_widget.setLayout(self.four_layout)
        
        self.five_widget = QtWidgets.QWidget()
        self.five_layout = QtWidgets.QGridLayout()
        self.five_widget.setLayout(self.five_layout)
        
        self.add_widget = QtWidgets.QWidget()
        self.add_layout = QtWidgets.QGridLayout()
        self.add_widget.setLayout(self.add_layout)
        
        self.minW = QtWidgets.QPushButton("")
        self.maxW = QtWidgets.QPushButton("")
        self.closeW = QtWidgets.QPushButton("")
        
        self.button_1 = QtWidgets.QPushButton("生成密钥")
        self.button_2 = QtWidgets.QPushButton("解密文件")
        self.button_3 = QtWidgets.QPushButton("发送证书请求")
        self.button_4 = QtWidgets.QPushButton("在线观看")
        
        self.main_widget.setStyleSheet(StyleSheet)
        self.one_widget.setStyleSheet(StyleSheet_one)
        self.two_widget.setStyleSheet(StyleSheet_in)
        self.three_widget.setStyleSheet(StyleSheet_in)
        self.four_widget.setStyleSheet(StyleSheet_in)
        self.five_widget.setStyleSheet(StyleSheet_in)
        self.add_widget.setStyleSheet(StyleSheet_in)
        
        self.minW.setStyleSheet(StyleSheet_min)
        self.maxW.setStyleSheet(StyleSheet_max)
        self.closeW.setStyleSheet(StyleSheet_close)
        
        self.button_1.setStyleSheet(StyleSheet_btn)
        self.button_2.setStyleSheet(StyleSheet_btn)
        self.button_3.setStyleSheet(StyleSheet_btn)
        self.button_4.setStyleSheet(StyleSheet_btn)
        
        self.setCentralWidget(self.main_widget) # 设置窗口主部件
        self.main_layout.addWidget(self.one_widget, 0, 0, 4, 14)
        self.main_layout.addWidget(self.two_widget, 0, 14, 14, 2)
        self.main_layout.addWidget(self.three_widget, 14, 2, 2, 14)
        self.main_layout.addWidget(self.four_widget, 4, 0, 12, 2)
        self.main_layout.addWidget(self.five_widget, 4, 2, 10, 12)
        
        self.two_layout.addWidget(self.minW, 0, 0, 1, 1)
        self.two_layout.addWidget(self.maxW, 0, 1, 1, 1)
        self.two_layout.addWidget(self.closeW, 0, 2, 1, 1)
        self.two_layout.addWidget(self.add_widget, 1, 0, 14, 3)
        
        self.five_layout.addWidget(self.button_1,0,0)
        self.five_layout.addWidget(self.button_2,0,1)
        self.five_layout.addWidget(self.button_3,1,0)
        self.five_layout.addWidget(self.button_4,1,1)
        
        self.main_layout.setSpacing(0)
        self.two_layout.setSpacing(0)
        
        self.setWindowOpacity(0.88) # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隐藏边框
        
        self.minW.clicked.connect(self.showMinimized)
        self.closeW.clicked.connect(self.close)
        self.button_1.clicked.connect(self.btn1)
        self.button_2.clicked.connect(self.btn2)
        self.button_3.clicked.connect(self.btn3)
        self.button_4.clicked.connect(self.btn4)
        
    def btn1(self):
        genSM2key.genSM2Key()
        QtWidgets.QMessageBox.information(self,'生成密钥','生成密钥成功！',QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.Cancel)
        
    def btn2(self):
        self.deUi = DecrypUi()
        self.deUi.show()
        
    def btn3(self):
        self.caUi = CAUi()
        self.caUi.show()
        
    def btn4(self):
        self.olUi = OlUi()
        self.olUi.show()
        
        
        
class DecrypUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(440,200)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.one_widget = QtWidgets.QWidget()
        self.one_layout = QtWidgets.QGridLayout()
        self.one_widget.setLayout(self.one_layout)
        
        self.two_widget = QtWidgets.QWidget()
        self.two_layout = QtWidgets.QGridLayout()
        self.two_widget.setLayout(self.two_layout)
        
        self.three_widget = QtWidgets.QWidget()
        self.three_layout = QtWidgets.QGridLayout()
        self.three_widget.setLayout(self.three_layout)
        
        self.four_widget = QtWidgets.QWidget()
        self.four_layout = QtWidgets.QGridLayout()
        self.four_widget.setLayout(self.four_layout)
        
        self.five_widget = QtWidgets.QWidget()
        self.five_layout = QtWidgets.QGridLayout()
        self.five_widget.setLayout(self.five_layout)
        
        self.add_widget = QtWidgets.QWidget()
        self.add_layout = QtWidgets.QGridLayout()
        self.add_widget.setLayout(self.add_layout)
        
        self.closeW = QtWidgets.QPushButton("")
        self.button_1 = QtWidgets.QPushButton("确定")
        self.button_2 = QtWidgets.QPushButton("返回")
        
        self.lable_0 = QtWidgets.QLabel("解密文件")
        self.lable_1 = QtWidgets.QLabel("<font color='#fff'>待解密视频文件路径</font>")
        self.lable_2 = QtWidgets.QLabel("<font color='#fff'>解密秘钥文件路径</font>")
        self.lable_3 = QtWidgets.QLabel("<font color='#fff'>用户私钥文件路径</font>")
        
        self.path_1 = QtWidgets.QLineEdit()
        self.path_2 = QtWidgets.QLineEdit()
        self.path_3 = QtWidgets.QLineEdit()
        
        self.edit_1 = QtWidgets.QPushButton("…")
        self.edit_2 = QtWidgets.QPushButton("…")
        self.edit_3 = QtWidgets.QPushButton("…")
        
        self.main_widget.setStyleSheet(StyleSheet)
        self.one_widget.setStyleSheet(StyleSheet_in)
        self.two_widget.setStyleSheet(StyleSheet_in)
        self.three_widget.setStyleSheet(StyleSheet_in)
        self.four_widget.setStyleSheet(StyleSheet_in)
        self.five_widget.setStyleSheet(StyleSheet_in)
        self.add_widget.setStyleSheet(StyleSheet_in)
        
        self.closeW.setStyleSheet(StyleSheet_close)
        self.lable_0.setStyleSheet(StyleSheet_label)
        self.button_1.setStyleSheet(StyleSheet_btn_c)
        self.button_2.setStyleSheet(StyleSheet_btn_c)
        self.path_1.setStyleSheet(StyleSheet_lineEdit)
        self.path_2.setStyleSheet(StyleSheet_lineEdit)
        self.path_3.setStyleSheet(StyleSheet_lineEdit)
        self.edit_1.setStyleSheet(StyleSheet_btn_e)
        self.edit_2.setStyleSheet(StyleSheet_btn_e)
        self.edit_3.setStyleSheet(StyleSheet_btn_e)
        
        self.setCentralWidget(self.main_widget) # 设置窗口主部件
        self.main_layout.addWidget(self.one_widget, 0, 0, 6, 1)
        self.main_layout.addWidget(self.two_widget, 0, 1, 1, 9)
        self.main_layout.addWidget(self.three_widget, 1, 1, 4, 9)
        self.main_layout.addWidget(self.four_widget, 5, 1, 1, 9)
        self.main_layout.addWidget(self.five_widget, 0, 10, 6, 1)
        
        self.five_layout.addWidget(self.closeW, 0, 0, 1, 1)
        self.five_layout.addWidget(self.add_widget, 1, 0, 5, 1)
        
        self.two_layout.addWidget(self.lable_0)
        self.three_layout.addWidget(self.lable_1,0,0)
        self.three_layout.addWidget(self.path_1,0,1)
        self.three_layout.addWidget(self.edit_1,0,2)
        self.three_layout.addWidget(self.lable_2,1,0)
        self.three_layout.addWidget(self.path_2,1,1)
        self.three_layout.addWidget(self.edit_2,1,2)
        self.three_layout.addWidget(self.lable_3,2,0)
        self.three_layout.addWidget(self.path_3,2,1)
        self.three_layout.addWidget(self.edit_3,2,2)
        
        self.four_layout.addWidget(self.button_1,0,0)
        self.four_layout.addWidget(self.button_2,0,1)
        
        self.main_layout.setSpacing(4)
        self.three_layout.setSpacing(4)
        
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隐藏边框
        
        self.closeW.clicked.connect(self.close)
        self.edit_1.clicked.connect(self.btn_Clicked_1)
        self.edit_2.clicked.connect(self.btn_Clicked_2)
        self.edit_3.clicked.connect(self.btn_Clicked_3)
        self.button_1.clicked.connect(self.decryp)
        self.button_2.clicked.connect(self.close)
        
    def btn_Clicked_1(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self)
        self.path_1.setText(str(filename[0]))
        
    def btn_Clicked_2(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self)
        self.path_2.setText(str(filename[0]))
        
    def btn_Clicked_3(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self)
        self.path_3.setText(str(filename[0]))
        
    def decryp(self):
        Main.getencrypt(self.path_1.text(),self.path_2.text(),self.path_3.text())
        QtWidgets.QMessageBox.information(self,'解密文件','解密成功！',QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.Cancel)
        
        
class CAUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(460,220)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.one_widget = QtWidgets.QWidget()
        self.one_layout = QtWidgets.QGridLayout()
        self.one_widget.setLayout(self.one_layout)
        
        self.two_widget = QtWidgets.QWidget()
        self.two_layout = QtWidgets.QGridLayout()
        self.two_widget.setLayout(self.two_layout)
        
        self.three_widget = QtWidgets.QWidget()
        self.three_layout = QtWidgets.QGridLayout()
        self.three_widget.setLayout(self.three_layout)
        
        self.four_widget = QtWidgets.QWidget()
        self.four_layout = QtWidgets.QGridLayout()
        self.four_widget.setLayout(self.four_layout)
        
        self.five_widget = QtWidgets.QWidget()
        self.five_layout = QtWidgets.QGridLayout()
        self.five_widget.setLayout(self.five_layout)
        
        self.add_widget = QtWidgets.QWidget()
        self.add_layout = QtWidgets.QGridLayout()
        self.add_widget.setLayout(self.add_layout)
        
        self.closeW = QtWidgets.QPushButton("")
        self.button_1 = QtWidgets.QPushButton("确定")
        self.button_2 = QtWidgets.QPushButton("返回")
        
        self.lable_0 = QtWidgets.QLabel("发送证书请求")
        self.lable_1 = QtWidgets.QLabel("<font color='#fff'>CA中心IP地址</font>")
        self.lable_2 = QtWidgets.QLabel("<font color='#fff'>用户名</font>")
        self.lable_3 = QtWidgets.QLabel("<font color='#fff'>用户密码</font>")
        self.lable_4 = QtWidgets.QLabel("<font color='#fff'>选择上传文件</font>")
        self.lable_5 = QtWidgets.QLabel("<font color='#fff'>选择加密密钥</font>")
        
        
        self.path_1 = QtWidgets.QLineEdit()
        self.path_2 = QtWidgets.QLineEdit()
        self.path_3 = QtWidgets.QLineEdit()
        self.path_4 = QtWidgets.QLineEdit()
        self.edit_4 = QtWidgets.QPushButton("…")
        self.path_5 = QtWidgets.QLineEdit()
        self.edit_5 = QtWidgets.QPushButton("…")
        
        self.main_widget.setStyleSheet(StyleSheet)
        self.one_widget.setStyleSheet(StyleSheet_in)
        self.two_widget.setStyleSheet(StyleSheet_in)
        self.three_widget.setStyleSheet(StyleSheet_in)
        self.four_widget.setStyleSheet(StyleSheet_in)
        self.five_widget.setStyleSheet(StyleSheet_in)
        self.add_widget.setStyleSheet(StyleSheet_in)
        
        self.closeW.setStyleSheet(StyleSheet_close)
        self.lable_0.setStyleSheet(StyleSheet_label)
        self.button_1.setStyleSheet(StyleSheet_btn_c)
        self.button_2.setStyleSheet(StyleSheet_btn_c)
        self.path_1.setStyleSheet(StyleSheet_lineEdit)
        self.path_2.setStyleSheet(StyleSheet_lineEdit)
        self.path_3.setStyleSheet(StyleSheet_lineEdit)
        self.path_4.setStyleSheet(StyleSheet_lineEdit)
        self.edit_4.setStyleSheet(StyleSheet_btn_e)
        self.path_5.setStyleSheet(StyleSheet_lineEdit)
        self.edit_5.setStyleSheet(StyleSheet_btn_e)
        
        self.setCentralWidget(self.main_widget) # 设置窗口主部件
        self.main_layout.addWidget(self.one_widget, 0, 0, 8, 1)
        self.main_layout.addWidget(self.two_widget, 0, 1, 2, 9)
        self.main_layout.addWidget(self.three_widget, 2, 1, 4, 9)
        self.main_layout.addWidget(self.four_widget, 6, 1, 2, 9)
        self.main_layout.addWidget(self.five_widget, 0, 10, 8, 1)
        
        self.five_layout.addWidget(self.closeW, 0, 0, 1, 1)
        self.five_layout.addWidget(self.add_widget, 1, 0, 5, 1)
        
        self.two_layout.addWidget(self.lable_0)
        self.three_layout.addWidget(self.lable_1,0,0)
        self.three_layout.addWidget(self.path_1,0,1)
        self.three_layout.addWidget(self.lable_2,1,0)
        self.three_layout.addWidget(self.path_2,1,1)
        self.three_layout.addWidget(self.lable_3,2,0)
        self.three_layout.addWidget(self.path_3,2,1)
        self.three_layout.addWidget(self.lable_4,3,0)
        self.three_layout.addWidget(self.path_4,3,1)
        self.three_layout.addWidget(self.edit_4,3,2)
        self.three_layout.addWidget(self.lable_5,4,0)
        self.three_layout.addWidget(self.path_5,4,1)
        self.three_layout.addWidget(self.edit_5,4,2)
        
        self.four_layout.addWidget(self.button_1,0,0)
        self.four_layout.addWidget(self.button_2,0,1)
        
        self.main_layout.setSpacing(0)
        self.three_layout.setSpacing(4)
        
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隐藏边框
        
        self.closeW.clicked.connect(self.close)
        self.button_1.clicked.connect(self.upload)
        self.button_2.clicked.connect(self.close)
        self.path_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_4.clicked.connect(self.btn_Clicked_4)
        self.edit_5.clicked.connect(self.btn_Clicked_5)
        
    def upload(self):
        Main.file_up(self.path_1.text(),self.path_2.text(),self.path_3.text(),self.path_4.text(),self.path_5.text())
        QtWidgets.QMessageBox.information(self,'发送证书请求','成功发送证书请求！',QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.Cancel)
        
    def btn_Clicked_4(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self)
        self.path_4.setText(str(filename[0]))
        
    def btn_Clicked_5(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self)
        self.path_5.setText(str(filename[0]))
        
        
        
class OlUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(440,200)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.one_widget = QtWidgets.QWidget()
        self.one_layout = QtWidgets.QGridLayout()
        self.one_widget.setLayout(self.one_layout)
        
        self.two_widget = QtWidgets.QWidget()
        self.two_layout = QtWidgets.QGridLayout()
        self.two_widget.setLayout(self.two_layout)
        
        self.three_widget = QtWidgets.QWidget()
        self.three_layout = QtWidgets.QGridLayout()
        self.three_widget.setLayout(self.three_layout)
        
        self.four_widget = QtWidgets.QWidget()
        self.four_layout = QtWidgets.QGridLayout()
        self.four_widget.setLayout(self.four_layout)
        
        self.five_widget = QtWidgets.QWidget()
        self.five_layout = QtWidgets.QGridLayout()
        self.five_widget.setLayout(self.five_layout)
        
        self.add_widget = QtWidgets.QWidget()
        self.add_layout = QtWidgets.QGridLayout()
        self.add_widget.setLayout(self.add_layout)
        
        self.closeW = QtWidgets.QPushButton("")
        self.button_1 = QtWidgets.QPushButton("确定")
        self.button_2 = QtWidgets.QPushButton("返回")
        
        self.lable_0 = QtWidgets.QLabel("在线观看")
        self.lable_1 = QtWidgets.QLabel("<font color='#fff'>服务器IP地址</font>")
        self.lable_2 = QtWidgets.QLabel("<font color='#fff'>ZUC密钥</font>")
        self.lable_3 = QtWidgets.QLabel("<font color='#fff'>选择解密密钥</font>")
        
        self.path_1 = QtWidgets.QLineEdit()
        self.path_2 = QtWidgets.QLineEdit()
        self.edit_2 = QtWidgets.QPushButton("…")
        self.path_3 = QtWidgets.QLineEdit()
        self.edit_3 = QtWidgets.QPushButton("…")
        
        self.main_widget.setStyleSheet(StyleSheet)
        self.one_widget.setStyleSheet(StyleSheet_in)
        self.two_widget.setStyleSheet(StyleSheet_in)
        self.three_widget.setStyleSheet(StyleSheet_in)
        self.four_widget.setStyleSheet(StyleSheet_in)
        self.five_widget.setStyleSheet(StyleSheet_in)
        self.add_widget.setStyleSheet(StyleSheet_in)
        
        self.closeW.setStyleSheet(StyleSheet_close)
        self.lable_0.setStyleSheet(StyleSheet_label)
        self.button_1.setStyleSheet(StyleSheet_btn_c)
        self.button_2.setStyleSheet(StyleSheet_btn_c)
        self.path_1.setStyleSheet(StyleSheet_lineEdit)
        self.path_2.setStyleSheet(StyleSheet_lineEdit)
        self.edit_2.setStyleSheet(StyleSheet_btn_e)
        self.path_3.setStyleSheet(StyleSheet_lineEdit)
        self.edit_3.setStyleSheet(StyleSheet_btn_e)
        
        self.setCentralWidget(self.main_widget) # 设置窗口主部件
        self.main_layout.addWidget(self.one_widget, 0, 0, 6, 1)
        self.main_layout.addWidget(self.two_widget, 0, 1, 1, 9)
        self.main_layout.addWidget(self.three_widget, 1, 1, 4, 9)
        self.main_layout.addWidget(self.four_widget, 5, 1, 1, 9)
        self.main_layout.addWidget(self.five_widget, 0, 10, 6, 1)
        
        self.five_layout.addWidget(self.closeW, 0, 0, 1, 1)
        self.five_layout.addWidget(self.add_widget, 1, 0, 5, 1)
        
        self.two_layout.addWidget(self.lable_0)
        self.three_layout.addWidget(self.lable_1,0,0)
        self.three_layout.addWidget(self.path_1,0,1)
        self.three_layout.addWidget(self.lable_2,1,0)
        self.three_layout.addWidget(self.path_2,1,1)
        self.three_layout.addWidget(self.edit_2,1,2)
        self.three_layout.addWidget(self.lable_3,2,0)
        self.three_layout.addWidget(self.path_3,2,1)
        self.three_layout.addWidget(self.edit_3,2,2)
        
        self.four_layout.addWidget(self.button_1,0,0)
        self.four_layout.addWidget(self.button_2,0,1)
        
        self.main_layout.setSpacing(0)
        
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隐藏边框
        
        self.closeW.clicked.connect(self.close)
        self.button_1.clicked.connect(self.player)
        self.button_2.clicked.connect(self.close)
        self.edit_2.clicked.connect(self.btn_Clicked_2)
        self.edit_3.clicked.connect(self.btn_Clicked_3)
        
    def btn_Clicked_2(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self)
        self.path_2.setText(str(filename[0]))
        
    def btn_Clicked_3(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self)
        self.path_3.setText(str(filename[0]))
        
    def player(self):
        #p = vlc.MediaPlayer('rtmp://' + self.path_1.text() + '/pcam/home1')
        p = vlc.MediaPlayer('rtmp://' + self.path_1.text() + '/pcam/home1')
        p.play()





def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()