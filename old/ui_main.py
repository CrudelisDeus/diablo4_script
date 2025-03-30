# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import rc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 401)
        icon = QIcon()
        icon.addFile(u":/ui/logo.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"        stop:0 #1c0000, \n"
"        stop:0.5 #8b0000, \n"
"        stop:1 #ff3300);")
        MainWindow.setAnimated(False)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_actv = QPushButton(self.centralwidget)
        self.btn_actv.setObjectName(u"btn_actv")
        self.btn_actv.setGeometry(QRect(24, 327, 752, 49))
        self.btn_actv.setStyleSheet(u"QPushButton {\n"
"    color: #FFFFFF; /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    background-color: #550000; /* \u0422\u0451\u043c\u043d\u043e-\u043a\u0440\u0430\u0441\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    border-radius: 10px;\n"
"    font-size: 16px;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #770000; /* \u0421\u0432\u0435\u0442\u043b\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #990000; /* \u0415\u0449\u0451 \u044f\u0440\u0447\u0435 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.script_1 = QLabel(self.centralwidget)
        self.script_1.setObjectName(u"script_1")
        self.script_1.setGeometry(QRect(24, 24, 410, 49))
        self.script_1.setStyleSheet(u"QLabel {\n"
"    color: #E0B0FF;\n"
"    background-color: #330000;\n"
"    border-radius: 10px;\n"
"\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}")
        self.script_2 = QLabel(self.centralwidget)
        self.script_2.setObjectName(u"script_2")
        self.script_2.setGeometry(QRect(24, 97, 410, 49))
        self.script_2.setStyleSheet(u"QLabel {\n"
"    color: #E0B0FF;\n"
"    background-color: #330000;\n"
"    border-radius: 10px;\n"
"\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}")
        self.script_3 = QLabel(self.centralwidget)
        self.script_3.setObjectName(u"script_3")
        self.script_3.setGeometry(QRect(24, 170, 410, 49))
        self.script_3.setStyleSheet(u"QLabel {\n"
"    color: #E0B0FF;\n"
"    background-color: #330000;\n"
"    border-radius: 10px;\n"
"\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(530, 24, 173, 279))
        self.label.setStyleSheet(u"background:transparent;")
        self.label.setPixmap(QPixmap(u":/ui/logo.png"))
        self.label.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"D4 Script", None))
        self.btn_actv.setText(QCoreApplication.translate("MainWindow", u"Activate", None))
        self.script_1.setText(QCoreApplication.translate("MainWindow", u"script_1", None))
        self.script_2.setText(QCoreApplication.translate("MainWindow", u"script_2", None))
        self.script_3.setText(QCoreApplication.translate("MainWindow", u"script_3", None))
        self.label.setText("")
    # retranslateUi

