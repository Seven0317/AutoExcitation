一、PyQt5 插件安装 （IDE：Pycharm）

1. Tools
(1) QtDesigner

(2) PyUIC

(3) PyRCC （本应用中暂时未用到）

(4) pip install pyqt5-tools

2. Links

(1) https://www.jianshu.com/p/344bdf61e69e

二、PyQt5 知识点

1. 窗口属性设置

(1) 无边框，隐藏任务栏图标，以桌面形式显示在最底层
```
self.setWindowFlags(Qt.FramelessWindowHint |
               Qt.ToolTip |
               Qt.Desktop |
               Qt.WindowStaysOnBottomHint)
```
(2) 背景透明
```
self.setAttribute(Qt.WA_TranslucentBackground, True)
```
(3) 窗口位置
```
self.move((x1, y1), (x2, y2))
```
(4) 程序图标
```
self.setWindowIcon(QtGui.QIcon(r".\icon.ico"))
```

(5) 托盘功能
```
self.tray_icon = QSystemTrayIcon(QIcon(), self)
self.tray_icon.setIcon(QtGui.QIcon(os.path.join(os.getcwd(), r".\icon.ico")))
self.tray_icon.setToolTip("每日美句")
```
(6) 托盘右键退出
```
self.tray_icon_menu = QMenu(self)
self.quitAction = QAction("退出(Q)", self, triggered=self.close)
self.tray_icon_menu.addAction(self.quitAction)
self.tray_icon.setContextMenu(self.tray_icon_menu)
self.tray_icon.show()
```
2. 文本标签属性设置

(1) 重新设置标签尺寸
```
self.ui.label.resize((x1, y1), (x2, y2))
```
(2) 字体颜色
```
pe = QPalette()
pe.setColor(QPalette.WindowText, Qt.white)
```
(3) 显示内容
```
self.ui.label.setText("Hello world!")
```
(4) 背景填充（背景颜色的前提）
```
self.ui.label.setAutoFillBackground(True)
```
(5) 背景颜色
```
pe.setColor(QPalette.Window, Qt.darkCyan)
```
