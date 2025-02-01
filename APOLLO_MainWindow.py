# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'APOLLO_Mainwindow.ui'
##
# Created by: Qt User Interface Compiler version 6.8.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPlainTextEdit,
                               QPushButton, QSizePolicy, QTextBrowser, QVBoxLayout,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 675)
        MainWindow.setMinimumSize(QSize(1200, 675))
        MainWindow.setMaximumSize(QSize(1200, 675))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
                                 "background-color: #4666a3 ;\n"
                                 "}\n"
                                 "")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
                                         "background-color: #4666a3 ;\n"
                                         "}")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(70, 0, 802, 671))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Title_Label = QLabel(self.verticalLayoutWidget)
        self.Title_Label.setObjectName(u"Title_Label")
        self.Title_Label.setMaximumSize(QSize(600, 16777215))
        self.Title_Label.setPixmap(QPixmap(u"Assets/APOLLO_Title.png"))
        self.Title_Label.setScaledContents(False)
        self.Title_Label.setAlignment(Qt.AlignCenter)
        self.Title_Label.setMargin(0)

        self.verticalLayout.addWidget(self.Title_Label, 0, Qt.AlignHCenter)

        self.Response_Display = QTextBrowser(self.verticalLayoutWidget)
        self.Response_Display.setObjectName(u"Response_Display")
        self.Response_Display.setMinimumSize(QSize(800, 0))
        self.Response_Display.setMaximumSize(QSize(800, 421))
        self.Response_Display.setStyleSheet(u"QTextBrowser {\n"
                                            "background-color: #243169;\n"
                                            "color: 6a93be}")
        self.Response_Display.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.Response_Display.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)

        self.verticalLayout.addWidget(self.Response_Display)

        self.Input_Field = QPlainTextEdit(self.verticalLayoutWidget)
        self.Input_Field.setObjectName(u"Input_Field")
        self.Input_Field.setMinimumSize(QSize(800, 0))
        self.Input_Field.setMaximumSize(QSize(1000, 150))
        self.Input_Field.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Input_Field.setBackgroundVisible(False)
        self.Input_Field.setCenterOnScroll(False)

        self.verticalLayout.addWidget(self.Input_Field)

        self.Send_Button = QPushButton(self.verticalLayoutWidget)
        self.Send_Button.setObjectName(u"Send_Button")
        self.Send_Button.setMaximumSize(QSize(1000, 1000))
        self.Send_Button.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u"Assets/Apollo_Send_Button.png", QSize(),
                     QIcon.Mode.Normal, QIcon.State.Off)
        self.Send_Button.setIcon(icon)
        self.Send_Button.setIconSize(QSize(128, 64))
        self.Send_Button.setAutoDefault(False)
        self.Send_Button.setFlat(True)

        self.verticalLayout.addWidget(self.Send_Button, 0, Qt.AlignHCenter)

        self.Apollo_Sprite = QLabel(self.centralwidget)
        self.Apollo_Sprite.setObjectName(u"Apollo_Sprite")
        self.Apollo_Sprite.setGeometry(QRect(900, 160, 280, 360))
        self.Apollo_Sprite.setPixmap(QPixmap(u"Assets/Apollo_Idle.gif"))
        self.Apollo_Sprite.setScaledContents(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Send_Button.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"A.P.O.L.L.O", None))
        self.Title_Label.setText("")
        self.Response_Display.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                 "p, li { white-space: pre-wrap; }\n"
                                                                 "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Input_Field.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Ask your question here!", None))
        self.Send_Button.setText("")
        self.Apollo_Sprite.setText("")
    # retranslateUi
