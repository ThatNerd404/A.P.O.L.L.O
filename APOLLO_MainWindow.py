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
        MainWindow.resize(1200, 710)
        MainWindow.setMinimumSize(QSize(1200, 675))
        MainWindow.setMaximumSize(QSize(1200, 710))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
                                 "background-color: #4666a3 ;\n"
                                 "border-color:#98c5de;\n"
                                 "border-style: solid;\n"
                                 "border-width: 5px;\n"
                                 "border-radius: 10px;\n"
                                 "}\n"
                                 "")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
                                         "background-color: #4666a3 ;\n"
                                         "color: #98c5de;\n"
                                         "\n"
                                         "}\n"
                                         "QWidget #centralwidget {\n"
                                         "border-width: 3px;\n"
                                         "border-style: solid;\n"
                                         "border-color: #243169;\n"
                                         "}")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 170, 842, 531))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Response_Display = QTextBrowser(self.verticalLayoutWidget)
        self.Response_Display.setObjectName(u"Response_Display")
        self.Response_Display.setMinimumSize(QSize(840, 0))
        self.Response_Display.setMaximumSize(QSize(1000, 1000))
        self.Response_Display.setStyleSheet(u"QTextBrowser {\n"
                                            "background-color: #243169;\n"
                                            "border-color:#98c5de;\n"
                                            "border-style: solid;\n"
                                            "border-width: 5px;\n"
                                            "font-size: 32px;\n"
                                            "}")
        self.Response_Display.setFrameShape(QFrame.StyledPanel)
        self.Response_Display.setFrameShadow(QFrame.Sunken)
        self.Response_Display.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.Response_Display.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        self.Response_Display.setOpenLinks(True)

        self.verticalLayout.addWidget(
            self.Response_Display, 0, Qt.AlignHCenter)

        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(840, 68))
        self.groupBox.setMaximumSize(QSize(1000, 100))
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
        self.Input_Field = QPlainTextEdit(self.groupBox)
        self.Input_Field.setObjectName(u"Input_Field")
        self.Input_Field.setMinimumSize(QSize(480, 0))
        self.Input_Field.setMaximumSize(QSize(1000, 50))
        self.Input_Field.setStyleSheet(u"QPlainTextEdit {\n"
                                       "background-color: #243169;\n"
                                       "border-color:#98c5de;\n"
                                       "border-style: solid;\n"
                                       "border-width: 5px;\n"
                                       "font-size: 16px;\n"
                                       "}")
        self.Input_Field.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Input_Field.setBackgroundVisible(False)
        self.Input_Field.setCenterOnScroll(False)

        self.horizontalLayout.addWidget(self.Input_Field)

        self.Send_Button = QPushButton(self.groupBox)
        self.Send_Button.setObjectName(u"Send_Button")
        self.Send_Button.setMinimumSize(QSize(64, 64))
        self.Send_Button.setMaximumSize(QSize(64, 64))
        self.Send_Button.setAutoFillBackground(False)
        self.Send_Button.setStyleSheet(u"QPushButton {\n"
                                       "qproperty-icon: url(\" \");\n"
                                       "qproperty-iconSize: 64px 64px;\n"
                                       "width: 64px;\n"
                                       "height:64px;\n"
                                       "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Apollo_Send_Button.png);\n"
                                       "  background-repeat: no-repeat;}\n"
                                       "QPushButton:hover {\n"
                                       "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Apollo_Send_Button_Down.png);\n"
                                       "background-repeat: no-repeat;}\n"
                                       "QPushButton:disabled {\n"
                                       "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Apollo_Send_Button_Down_Disabled.png);\n"
                                       "background-repeat: no-repeat;}\n"
                                       " \n"
                                       "")
        icon = QIcon()
        icon.addFile(u"Assets/Apollo_Send_Button.png", QSize(),
                     QIcon.Mode.Normal, QIcon.State.Off)
        self.Send_Button.setIcon(icon)
        self.Send_Button.setIconSize(QSize(64, 64))
        self.Send_Button.setAutoDefault(False)
        self.Send_Button.setFlat(True)

        self.horizontalLayout.addWidget(self.Send_Button)

        self.Cancel_Button = QPushButton(self.groupBox)
        self.Cancel_Button.setObjectName(u"Cancel_Button")
        self.Cancel_Button.setMaximumSize(QSize(64, 64))
        self.Cancel_Button.setStyleSheet(u"QPushButton {\n"
                                         "qproperty-icon: url(\" \");\n"
                                         "qproperty-iconSize: 64px 64px;\n"
                                         "width: 64px;\n"
                                         "height:64px;\n"
                                         "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Cancel_Button.png);\n"
                                         "  background-repeat: no-repeat;}\n"
                                         "QPushButton:hover {\n"
                                         "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Cancel_Button_Down.png);\n"
                                         "background-repeat: no-repeat;}\n"
                                         " ")
        icon1 = QIcon()
        icon1.addFile(u"Assets/Cancel_Button.png", QSize(),
                      QIcon.Mode.Normal, QIcon.State.Off)
        self.Cancel_Button.setIcon(icon1)
        self.Cancel_Button.setIconSize(QSize(64, 64))
        self.Cancel_Button.setFlat(True)

        self.horizontalLayout.addWidget(self.Cancel_Button)

        self.Refresh_Button = QPushButton(self.groupBox)
        self.Refresh_Button.setObjectName(u"Refresh_Button")
        self.Refresh_Button.setMinimumSize(QSize(64, 64))
        self.Refresh_Button.setMaximumSize(QSize(64, 64))
        self.Refresh_Button.setStyleSheet(u"QPushButton {\n"
                                          "qproperty-icon: url(\" \");\n"
                                          "qproperty-iconSize: 64px 64px;\n"
                                          "width: 64px;\n"
                                          "height:64px;\n"
                                          "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Refresh_Button.png);\n"
                                          "  background-repeat: no-repeat;}\n"
                                          "QPushButton:hover {\n"
                                          "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Refresh_Button_Down.png);\n"
                                          "background-repeat: no-repeat;}\n"
                                          "QPushButton:disabled {\n"
                                          "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Refresh_Button_Down_Disabled.png);\n"
                                          "background-repeat: no-repeat;}")
        icon2 = QIcon()
        icon2.addFile(u"Assets/Refresh_Button.png", QSize(),
                      QIcon.Mode.Normal, QIcon.State.Off)
        self.Refresh_Button.setIcon(icon2)
        self.Refresh_Button.setIconSize(QSize(64, 64))
        self.Refresh_Button.setFlat(True)

        self.horizontalLayout.addWidget(self.Refresh_Button)

        self.Save_Button = QPushButton(self.groupBox)
        self.Save_Button.setObjectName(u"Save_Button")
        self.Save_Button.setMinimumSize(QSize(64, 64))
        self.Save_Button.setMaximumSize(QSize(64, 64))
        self.Save_Button.setStyleSheet(u"QPushButton {\n"
                                       "qproperty-icon: url(\" \");\n"
                                       "qproperty-iconSize: 64px 64px;\n"
                                       "width: 64px;\n"
                                       "height:64px;\n"
                                       "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Save_Button.png);\n"
                                       "  background-repeat: no-repeat;}\n"
                                       "QPushButton:hover {\n"
                                       "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Save_Button_Down.png);\n"
                                       "background-repeat: no-repeat;}\n"
                                       "QPushButton:disabled {\n"
                                       "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Save_Button_Down_Disabled.png);\n"
                                       "background-repeat: no-repeat;}")
        icon3 = QIcon()
        icon3.addFile(u"Assets/Save_Button.png", QSize(),
                      QIcon.Mode.Normal, QIcon.State.Off)
        self.Save_Button.setIcon(icon3)
        self.Save_Button.setIconSize(QSize(64, 64))
        self.Save_Button.setFlat(True)

        self.horizontalLayout.addWidget(self.Save_Button)

        self.Load_Button = QPushButton(self.groupBox)
        self.Load_Button.setObjectName(u"Load_Button")
        self.Load_Button.setMinimumSize(QSize(64, 64))
        self.Load_Button.setMaximumSize(QSize(64, 64))
        self.Load_Button.setStyleSheet(u"QPushButton {\n"
                                       "qproperty-icon: url(\" \");\n"
                                       "qproperty-iconSize: 64px 64px;\n"
                                       "width: 64px;\n"
                                       "height:64px;\n"
                                       "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Load_Button.png);\n"
                                       "  background-repeat: no-repeat;}\n"
                                       "QPushButton:hover {\n"
                                       "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Load_Button_Down.png);\n"
                                       "background-repeat: no-repeat;}\n"
                                       "QPushButton:disabled {\n"
                                       "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Load_Button_Down_Disabled.png);\n"
                                       "background-repeat: no-repeat;}")
        self.Load_Button.setIconSize(QSize(64, 64))
        self.Load_Button.setFlat(True)

        self.horizontalLayout.addWidget(self.Load_Button)

        self.verticalLayout.addWidget(
            self.groupBox, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(870, 180, 300, 521))
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
                                      "border-color:#98c5de;\n"
                                      "border-style: solid;\n"
                                      "border-width: 0px;\n"
                                      "border-radius: 10px;}")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Apollo_Sprite = QLabel(self.groupBox_2)
        self.Apollo_Sprite.setObjectName(u"Apollo_Sprite")
        self.Apollo_Sprite.setPixmap(QPixmap(u"Assets/Apollo_Idle.gif"))
        self.Apollo_Sprite.setScaledContents(False)

        self.verticalLayout_2.addWidget(self.Apollo_Sprite)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 60))
        self.groupBox_3.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Model_Chooser = QComboBox(self.groupBox_3)
        self.Model_Chooser.addItem("")
        self.Model_Chooser.addItem("")
        self.Model_Chooser.addItem("")
        self.Model_Chooser.setObjectName(u"Model_Chooser")
        self.Model_Chooser.setMinimumSize(QSize(0, 60))
        self.Model_Chooser.setLayoutDirection(Qt.LeftToRight)
        self.Model_Chooser.setStyleSheet(u"QComboBox {\n"
                                         "background-color: #243169;\n"
                                         "border-color:#98c5de;\n"
                                         "border-style: solid;\n"
                                         "border-width: 5px;\n"
                                         "font-size:16px;\n"
                                         "}")
        self.Model_Chooser.setFrame(True)

        self.horizontalLayout_2.addWidget(self.Model_Chooser)

        self.Add_Model_Button = QPushButton(self.groupBox_3)
        self.Add_Model_Button.setObjectName(u"Add_Model_Button")
        self.Add_Model_Button.setMinimumSize(QSize(64, 64))
        self.Add_Model_Button.setMaximumSize(QSize(64, 64))
        self.Add_Model_Button.setStyleSheet(u"QPushButton {\n"
                                            "qproperty-icon: url(\" \");\n"
                                            "qproperty-iconSize: 64px 64px;\n"
                                            "width: 64px;\n"
                                            "height:64px;\n"
                                            "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Add_Model_Button.png);\n"
                                            "  background-repeat: no-repeat;}\n"
                                            "QPushButton:hover {\n"
                                            "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Add_Model_Button_Down.png);\n"
                                            "background-repeat: no-repeat;}")
        self.Add_Model_Button.setFlat(True)

        self.horizontalLayout_2.addWidget(self.Add_Model_Button)

        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.Title_Label = QLabel(self.centralwidget)
        self.Title_Label.setObjectName(u"Title_Label")
        self.Title_Label.setGeometry(QRect(430, 40, 357, 117))
        self.Title_Label.setMaximumSize(QSize(600, 16777215))
        self.Title_Label.setStyleSheet(u"")
        self.Title_Label.setPixmap(QPixmap(u"Assets/APOLLO_Title.png"))
        self.Title_Label.setScaledContents(False)
        self.Title_Label.setAlignment(Qt.AlignCenter)
        self.Title_Label.setMargin(0)
        self.Close_Window_Button = QPushButton(self.centralwidget)
        self.Close_Window_Button.setObjectName(u"Close_Window_Button")
        self.Close_Window_Button.setGeometry(QRect(1133, 0, 66, 46))
        self.Close_Window_Button.setStyleSheet(u"QPushButton {\n"
                                               "qproperty-icon: url(\" \");\n"
                                               "qproperty-iconSize: 64px 44px;\n"
                                               "width: 64px;\n"
                                               "height:44px;\n"
                                               "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Close_Window_Button.png);\n"
                                               "  background-repeat: no-repeat;}\n"
                                               "QPushButton:hover {\n"
                                               "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Close_Window_Button_Hover.png);\n"
                                               "qproperty-iconSize: 64px 44px;\n"
                                               "width: 64px;\n"
                                               "height:44px;\n"
                                               "}")
        icon4 = QIcon()
        icon4.addFile(u"Assets/Close_Window_Button.png", QSize(),
                      QIcon.Mode.Normal, QIcon.State.Off)
        self.Close_Window_Button.setIcon(icon4)
        self.Close_Window_Button.setIconSize(QSize(64, 44))
        self.Close_Window_Button.setFlat(True)
        self.Minimize_Window_Button = QPushButton(self.centralwidget)
        self.Minimize_Window_Button.setObjectName(u"Minimize_Window_Button")
        self.Minimize_Window_Button.setGeometry(QRect(1071, 0, 66, 46))
        self.Minimize_Window_Button.setStyleSheet(u"QPushButton {\n"
                                                  "qproperty-icon: url(\" \");\n"
                                                  "qproperty-iconSize: 64px 44px;\n"
                                                  "width: 64px;\n"
                                                  "height:44px;\n"
                                                  "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Minimize_Window_Button.png);\n"
                                                  "  background-repeat: no-repeat;}\n"
                                                  "QPushButton:hover {\n"
                                                  "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Minimize_Window_Button_Hover.png);\n"
                                                  "qproperty-iconSize: 64px 44px;\n"
                                                  "width: 64px;\n"
                                                  "height:44px;\n"
                                                  "}")
        icon5 = QIcon()
        icon5.addFile(u"Assets/Minimize_Window_Button.png",
                      QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Minimize_Window_Button.setIcon(icon5)
        self.Minimize_Window_Button.setIconSize(QSize(64, 44))
        self.Minimize_Window_Button.setFlat(True)
        self.Initials = QLabel(self.centralwidget)
        self.Initials.setObjectName(u"Initials")
        self.Initials.setGeometry(QRect(800, 130, 61, 26))
        self.Initials.setPixmap(QPixmap(u"Assets/APOLLO_Initials.png"))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 10, 38, 38))
        icon6 = QIcon()
        icon6.addFile(u"Assets/Cog.png", QSize(),
                      QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon6)
        self.pushButton.setIconSize(QSize(76, 76))
        self.pushButton.setFlat(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.groupBox_2.raise_()
        self.verticalLayoutWidget.raise_()
        self.Title_Label.raise_()
        self.Close_Window_Button.raise_()
        self.Minimize_Window_Button.raise_()
        self.Initials.raise_()
        self.pushButton.raise_()

        self.retranslateUi(MainWindow)

        self.Send_Button.setDefault(False)
        self.Model_Chooser.setCurrentIndex(0)
        self.Close_Window_Button.setDefault(False)
        self.Minimize_Window_Button.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"A.P.O.L.L.O", None))
        self.Response_Display.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                 "p, li { white-space: pre-wrap; }\n"
                                                                 "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:32px; font-weight:400; font-style:normal;\">\n"
                                                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:30px;\"><br /></p></body></html>", None))
        self.groupBox.setTitle("")
        self.Input_Field.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Ask your question here!", None))
        self.Send_Button.setText("")
        self.Cancel_Button.setText("")
        self.Refresh_Button.setText("")
        self.Save_Button.setText("")
        self.Load_Button.setText("")
        self.groupBox_2.setTitle("")
        self.Apollo_Sprite.setText("")
        self.groupBox_3.setTitle("")
        self.Model_Chooser.setItemText(
            0, QCoreApplication.translate("MainWindow", u"General", None))
        self.Model_Chooser.setItemText(
            1, QCoreApplication.translate("MainWindow", u"Tutoring", None))
        self.Model_Chooser.setItemText(
            2, QCoreApplication.translate("MainWindow", u"Coding", None))

        self.Model_Chooser.setCurrentText(
            QCoreApplication.translate("MainWindow", u"General", None))
        self.Add_Model_Button.setText("")
        self.Title_Label.setText("")
        self.Close_Window_Button.setText("")
        self.Minimize_Window_Button.setText("")
        self.Initials.setText("")
        self.pushButton.setText("")
    # retranslateUi
