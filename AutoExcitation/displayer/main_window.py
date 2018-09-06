# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/9/2 14:02

from PyQt5 import QtGui
from displayer import designer
from displayer import text_display

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu, QAction

from log import setup_logging
import threading
import logging
import sys
import os


setup_logging(default_path=os.path.join(os.getcwd(), r".\log.yaml"))
logger = logging.getLogger("fileLogger")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = designer.Ui_MainWindow()
        self.ui.setupUi(self)
        self.texter = text_display.Texter()
        # 无边框并隐藏任务栏图标,以桌面形式显示在最底层
        self.setWindowFlags(Qt.Desktop |
                            Qt.WindowStaysOnBottomHint |
                            Qt.FramelessWindowHint |
                            Qt.ToolTip)
        # 背景透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 程序图标
        self.setWindowIcon(QtGui.QIcon(os.path.join(os.getcwd(), r".\icon.ico")))
        # 窗口位置
        self.move(self.texter.location_display()[0], self.texter.location_display()[1])
        # 图标托盘功能
        self.tray_icon = QSystemTrayIcon(QIcon(), self)
        self.tray_icon.setIcon(QtGui.QIcon(os.path.join(os.getcwd(), r".\icon.ico")))
        self.tray_icon.setToolTip("每日美句")
        # 托盘右键退出
        self.tray_icon_menu = QMenu(self)
        self.quitAction = QAction("退出(Q)", self, triggered=self.close)
        self.tray_icon_menu.addAction(self.quitAction)
        self.tray_icon.setContextMenu(self.tray_icon_menu)
        self.tray_icon.show()

    def display_text(self):
        def fun_display():
            # 文本标签尺寸
            self.ui.label.resize(self.texter.location_display()[0] * 0.99, self.texter.location_display()[1] * 50)
            # 设置字体颜色
            pe = QPalette()
            pe.setColor(QPalette.WindowText, Qt.white)
            # self.ui.label.setAutoFillBackground(True)  # 设置背景充满，为设置背景颜色的必要条件
            # pe.setColor(QPalette.Window, Qt.darkCyan)  # 设置背景颜色
            self.ui.label.setPalette(pe)
            # 文本内容
            self.ui.label.setText(self.texter.full_display())
            logger.info("Display text successfully.")
            # 设置定时器，每隔60s更新一条句子
            timer = threading.Timer(60, fun_display)
            timer.start()
        # 启动应用5s后第一次显示句子
        timer = threading.Timer(5, fun_display)
        timer.start()

    # 重构主窗体的closeEvent() 函数，关闭窗口后，子线程同时退出
    def closeEvent(self):
        sys.exit(app.exec_())


app = QApplication(sys.argv)


# 构造display方法
def display():
    win = MainWindow()
    win.display_text()
    win.show()
    win.closeEvent()


# Remember to modify related path of resource.json, log.yaml if run module directly
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.display_text()
    win.show()
    win.closeEvent()

