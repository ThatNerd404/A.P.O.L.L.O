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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
                               QHBoxLayout, QLabel, QMainWindow, QPlainTextEdit,
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
                                         "color: #98c5de;\n"
                                         "}")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 0, 822, 671))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Title_Label = QLabel(self.verticalLayoutWidget)
        self.Title_Label.setObjectName(u"Title_Label")
        self.Title_Label.setMaximumSize(QSize(600, 16777215))
        self.Title_Label.setStyleSheet(u"")
        self.Title_Label.setPixmap(QPixmap(u"Assets/APOLLO_Title.png"))
        self.Title_Label.setScaledContents(False)
        self.Title_Label.setAlignment(Qt.AlignCenter)
        self.Title_Label.setMargin(0)

        self.verticalLayout.addWidget(self.Title_Label, 0, Qt.AlignHCenter)

        self.Response_Display = QTextBrowser(self.verticalLayoutWidget)
        self.Response_Display.setObjectName(u"Response_Display")
        self.Response_Display.setMinimumSize(QSize(820, 0))
        self.Response_Display.setMaximumSize(QSize(800, 421))
        self.Response_Display.setStyleSheet(u"QTextBrowser {\n"
                                            "background-color: #243169;\n"
                                            "border-color:#98c5de;\n"
                                            "border-style: solid;\n"
                                            "border-width: 5px;\n"
                                            "border-radius: 10px;\n"
                                            "font-size: 15px;\n"
                                            "}")
        self.Response_Display.setFrameShape(QFrame.StyledPanel)
        self.Response_Display.setFrameShadow(QFrame.Sunken)
        self.Response_Display.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.Response_Display.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        self.Response_Display.setOpenLinks(True)

        self.verticalLayout.addWidget(
            self.Response_Display, 0, Qt.AlignHCenter)

        self.Input_Field = QPlainTextEdit(self.verticalLayoutWidget)
        self.Input_Field.setObjectName(u"Input_Field")
        self.Input_Field.setMinimumSize(QSize(800, 0))
        self.Input_Field.setMaximumSize(QSize(1000, 150))
        self.Input_Field.setStyleSheet(u"QPlainTextEdit {\n"
                                       "background-color: #243169;\n"
                                       "border-color:#98c5de;\n"
                                       "border-style: solid;\n"
                                       "border-width: 5px;\n"
                                       "border-radius: 10px;\n"
                                       "}")
        self.Input_Field.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Input_Field.setBackgroundVisible(False)
        self.Input_Field.setCenterOnScroll(False)

        self.verticalLayout.addWidget(self.Input_Field)

        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 68))
        self.groupBox.setMaximumSize(QSize(250, 100))
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
                                    "border-color:#98c5de;\n"
                                    "border-style: solid;\n"
                                    "border-width: 0px;\n"
                                    "border-radius: 10px;}")
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Send_Button = QPushButton(self.groupBox)
        self.Send_Button.setObjectName(u"Send_Button")
        self.Send_Button.setMaximumSize(QSize(128, 1000))
        self.Send_Button.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u"Assets/Apollo_Send_Button.png", QSize(),
                     QIcon.Mode.Normal, QIcon.State.Off)
        self.Send_Button.setIcon(icon)
        self.Send_Button.setIconSize(QSize(128, 64))
        self.Send_Button.setAutoDefault(False)
        self.Send_Button.setFlat(True)

        self.horizontalLayout.addWidget(self.Send_Button)

        self.Refresh_Button = QPushButton(self.groupBox)
        self.Refresh_Button.setObjectName(u"Refresh_Button")
        self.Refresh_Button.setMaximumSize(QSize(64, 64))
        icon1 = QIcon()
        icon1.addFile(u"Assets/Refresh_Button.png", QSize(),
                      QIcon.Mode.Normal, QIcon.State.Off)
        self.Refresh_Button.setIcon(icon1)
        self.Refresh_Button.setIconSize(QSize(64, 64))
        self.Refresh_Button.setFlat(True)

        self.horizontalLayout.addWidget(self.Refresh_Button)

        self.verticalLayout.addWidget(
            self.groupBox, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(860, 120, 300, 471))
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
                                      "border-color:#98c5de;\n"
                                      "border-style: solid;\n"
                                      "border-width: 0px;\n"
                                      "border-radius: 10px;}")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Apollo_Sprite = QLabel(self.groupBox_2)
        self.Apollo_Sprite.setObjectName(u"Apollo_Sprite")
        self.Apollo_Sprite.setPixmap(QPixmap(u"Assets/Apollo_Idle.gif"))
        self.Apollo_Sprite.setScaledContents(False)

        self.verticalLayout_2.addWidget(self.Apollo_Sprite)

        self.Model_Chooser = QComboBox(self.groupBox_2)
        self.Model_Chooser.addItem("")
        self.Model_Chooser.addItem("")
        self.Model_Chooser.addItem("")
        self.Model_Chooser.setObjectName(u"Model_Chooser")
        self.Model_Chooser.setMinimumSize(QSize(0, 60))
        self.Model_Chooser.setLayoutDirection(Qt.LeftToRight)
        self.Model_Chooser.setFrame(True)

        self.verticalLayout_2.addWidget(self.Model_Chooser)

        MainWindow.setCentralWidget(self.centralwidget)
        self.groupBox_2.raise_()
        self.verticalLayoutWidget.raise_()

        self.retranslateUi(MainWindow)

        self.Send_Button.setDefault(False)
        self.Model_Chooser.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"A.P.O.L.L.O", None))
        self.Title_Label.setText("")
        self.Response_Display.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                 "p, li { white-space: pre-wrap; }\n"
                                                                 "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:15px; font-weight:400; font-style:normal;\">\n"
                                                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:30px;\"><br /></p></body></html>", None))
        self.Input_Field.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Ask your question here!", None))
        self.groupBox.setTitle("")
        self.Send_Button.setText("")
        self.Refresh_Button.setText("")
        self.groupBox_2.setTitle("")
        self.Apollo_Sprite.setText("")
        self.Model_Chooser.setItemText(
            0, QCoreApplication.translate("MainWindow", u"General", None))
        self.Model_Chooser.setItemText(
            1, QCoreApplication.translate("MainWindow", u"Tutoring", None))
        self.Model_Chooser.setItemText(
            2, QCoreApplication.translate("MainWindow", u"Coding", None))

        self.Model_Chooser.setCurrentText(
            QCoreApplication.translate("MainWindow", u"General", None))
    # retranslateUi
