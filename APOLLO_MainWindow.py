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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
                               QHBoxLayout, QLabel, QMainWindow, QPlainTextEdit,
                               QPushButton, QSizePolicy, QStackedWidget, QTextBrowser,
                               QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 710)
        MainWindow.setMinimumSize(QSize(1200, 710))
        MainWindow.setMaximumSize(QSize(2000, 2000))
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
        self.Close_Window_Button = QPushButton(self.centralwidget)
        self.Close_Window_Button.setObjectName(u"Close_Window_Button")
        self.Close_Window_Button.setGeometry(QRect(1134, 0, 66, 46))
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
        icon = QIcon()
        icon.addFile(u"Assets/Close_Window_Button.png", QSize(),
                     QIcon.Mode.Normal, QIcon.State.Off)
        self.Close_Window_Button.setIcon(icon)
        self.Close_Window_Button.setIconSize(QSize(64, 44))
        self.Close_Window_Button.setFlat(True)
        self.Minimize_Window_Button = QPushButton(self.centralwidget)
        self.Minimize_Window_Button.setObjectName(u"Minimize_Window_Button")
        self.Minimize_Window_Button.setGeometry(QRect(1072, 0, 66, 46))
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
        icon1 = QIcon()
        icon1.addFile(u"Assets/Minimize_Window_Button.png",
                      QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Minimize_Window_Button.setIcon(icon1)
        self.Minimize_Window_Button.setIconSize(QSize(64, 44))
        self.Minimize_Window_Button.setFlat(True)
        self.Main_Content = QStackedWidget(self.centralwidget)
        self.Main_Content.setObjectName(u"Main_Content")
        self.Main_Content.setGeometry(QRect(5, 45, 1190, 661))
        self.Main_Content.setMidLineWidth(0)
        self.Main_Page = QWidget()
        self.Main_Page.setObjectName(u"Main_Page")
        self.verticalLayoutWidget = QWidget(self.Main_Page)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 130, 842, 531))
        self.Main_Interface = QVBoxLayout(self.verticalLayoutWidget)
        self.Main_Interface.setSpacing(0)
        self.Main_Interface.setObjectName(u"Main_Interface")
        self.Main_Interface.setContentsMargins(0, 0, 0, 0)
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
                                            "line-height: 100%;\n"
                                            "}")
        self.Response_Display.setFrameShape(QFrame.StyledPanel)
        self.Response_Display.setFrameShadow(QFrame.Sunken)
        self.Response_Display.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.Response_Display.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        self.Response_Display.setOpenExternalLinks(True)
        self.Response_Display.setOpenLinks(True)

        self.Main_Interface.addWidget(self.Response_Display)

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
        self.Input_Field.setMinimumSize(QSize(400, 0))
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

        self.Send_Button = QCheckBox(self.groupBox)
        self.Send_Button.setObjectName(u"Send_Button")
        self.Send_Button.setMinimumSize(QSize(0, 0))
        self.Send_Button.setMaximumSize(QSize(64, 64))
        self.Send_Button.setToolTipDuration(-1)
        self.Send_Button.setAutoFillBackground(False)
        self.Send_Button.setStyleSheet(u"QCheckBox::indicator {\n"
                                       "min-width: 64px;\n"
                                       "min-height:64px;\n"
                                       "max-width: 64px;\n"
                                       "max-height:64px;\n"
                                       "image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Apollo_Send_Button.png);\n"
                                       "background:transparent;\n"
                                       "border:none;\n"
                                       "margin:0px;\n"
                                       "padding:0px;\n"
                                       "}\n"
                                       "QCheckBox::indicator:hover {\n"
                                       "min-width: 64px;\n"
                                       "min-height:64px;\n"
                                       "max-width: 64px;\n"
                                       "max-height:64px;\n"
                                       "image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Apollo_Send_Button_Down.png);\n"
                                       "background:transparent;\n"
                                       "border:none;\n"
                                       "margin:0px;\n"
                                       "padding:0px;\n"
                                       "}\n"
                                       "QCheckBox::indicator:checked {\n"
                                       "min-width: 64px;\n"
                                       "min-height:64px;\n"
                                       "max-width: 64px;\n"
                                       "max-height:64px;\n"
                                       "image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Cancel_Button.png);\n"
                                       "background:transparent;\n"
                                       "border:none;\n"
                                       "margin:0px;\n"
                                       "padding:0px;\n"
                                       "}\n"
                                       "QCheckBox::indicator:hover:checked {\n"
                                       "min-width: 64px;\n"
                                       "min-height:64px;\n"
                                       "max-width: 64px;\n"
                                       "max-"
                                       "height:64px;\n"
                                       "image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Cancel_Button_Down.png);\n"
                                       "background:transparent;\n"
                                       "border:none;\n"
                                       "margin:0px;\n"
                                       "padding:0px;\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       " \n"
                                       "\n"
                                       "\n"
                                       " \n"
                                       "")
        icon2 = QIcon()
        icon2.addFile(u"Assets/Apollo_Send_Button.png", QSize(),
                      QIcon.Mode.Normal, QIcon.State.Off)
        self.Send_Button.setIcon(icon2)
        self.Send_Button.setIconSize(QSize(64, 64))
        self.Send_Button.setCheckable(True)

        self.horizontalLayout.addWidget(self.Send_Button)

        self.Web_Search_Button = QCheckBox(self.groupBox)
        self.Web_Search_Button.setObjectName(u"Web_Search_Button")
        self.Web_Search_Button.setMinimumSize(QSize(0, 0))
        self.Web_Search_Button.setMaximumSize(QSize(64, 64))
        self.Web_Search_Button.setToolTipDuration(-1)
        self.Web_Search_Button.setAutoFillBackground(False)
        self.Web_Search_Button.setStyleSheet(u"QCheckBox::indicator {\n"
                                             "min-width: 64px;\n"
                                             "min-height:64px;\n"
                                             "max-width: 64px;\n"
                                             "max-height:64px;\n"
                                             "image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Web_Search_Button.png);\n"
                                             "background:transparent;\n"
                                             "border:none;\n"
                                             "margin:0px;\n"
                                             "padding:0px;\n"
                                             "}\n"
                                             "QCheckBox::indicator:hover {\n"
                                             "min-width: 64px;\n"
                                             "min-height:64px;\n"
                                             "max-width: 64px;\n"
                                             "max-height:64px;\n"
                                             "image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Web_Search_Button_Down.png);\n"
                                             "background:transparent;\n"
                                             "border:none;\n"
                                             "margin:0px;\n"
                                             "padding:0px;\n"
                                             "}\n"
                                             "QCheckBox::indicator:checked {\n"
                                             "min-width: 64px;\n"
                                             "min-height:64px;\n"
                                             "max-width: 64px;\n"
                                             "max-height:64px;\n"
                                             "image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Web_Search_Button_Down.png);\n"
                                             "background:transparent;\n"
                                             "border:none;\n"
                                             "margin:0px;\n"
                                             "padding:0px;\n"
                                             "}\n"
                                             "QCheckBox::indicator:hover:checked {\n"
                                             "min-width: 64px;\n"
                                             "min-height:64px;\n"
                                             "max-width: 64px;\n"
                                             ""
                                             "max-height:64px;\n"
                                             "image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Web_Search_Button_Down.png);\n"
                                             "background:transparent;\n"
                                             "border:none;\n"
                                             "margin:0px;\n"
                                             "padding:0px;\n"
                                             "}\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             " \n"
                                             "\n"
                                             "\n"
                                             " \n"
                                             "")
        self.Web_Search_Button.setIcon(icon2)
        self.Web_Search_Button.setIconSize(QSize(64, 64))
        self.Web_Search_Button.setCheckable(True)

        self.horizontalLayout.addWidget(self.Web_Search_Button)

        self.TTS_Button = QCheckBox(self.groupBox)
        self.TTS_Button.setObjectName(u"TTS_Button")
        self.TTS_Button.setMinimumSize(QSize(0, 0))
        self.TTS_Button.setMaximumSize(QSize(64, 64))
        self.TTS_Button.setToolTipDuration(-1)
        self.TTS_Button.setAutoFillBackground(False)
        self.TTS_Button.setStyleSheet(u"QCheckBox::indicator {\n"
                                      "min-width: 64px;\n"
                                      "min-height:64px;\n"
                                      "max-width: 64px;\n"
                                      "max-height:64px;\n"
                                      "image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/TTS_Button_Mute.png);\n"
                                      "background:transparent;\n"
                                      "border:none;\n"
                                      "margin:0px;\n"
                                      "padding:0px;\n"
                                      "}\n"
                                      "QCheckBox::indicator:hover {\n"
                                      "min-width: 64px;\n"
                                      "min-height:64px;\n"
                                      "max-width: 64px;\n"
                                      "max-height:64px;\n"
                                      "image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/TTS_Button_Mute_Down.png);\n"
                                      "background:transparent;\n"
                                      "border:none;\n"
                                      "margin:0px;\n"
                                      "padding:0px;\n"
                                      "}\n"
                                      "QCheckBox::indicator:checked {\n"
                                      "min-width: 64px;\n"
                                      "min-height:64px;\n"
                                      "max-width: 64px;\n"
                                      "max-height:64px;\n"
                                      "image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/TTS_Button_Down.png);\n"
                                      "background:transparent;\n"
                                      "border:none;\n"
                                      "margin:0px;\n"
                                      "padding:0px;\n"
                                      "}\n"
                                      "QCheckBox::indicator:hover:checked {\n"
                                      "min-width: 64px;\n"
                                      "min-height:64px;\n"
                                      "max-width: 64px;\n"
                                      "max-heig"
                                      "ht:64px;\n"
                                      "image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/TTS_Button_Down.png);\n"
                                      "background:transparent;\n"
                                      "border:none;\n"
                                      "margin:0px;\n"
                                      "padding:0px;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      " \n"
                                      "\n"
                                      "\n"
                                      " \n"
                                      "")
        self.TTS_Button.setIcon(icon2)
        self.TTS_Button.setIconSize(QSize(64, 64))
        self.TTS_Button.setCheckable(True)

        self.horizontalLayout.addWidget(self.TTS_Button)

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
                                          "QPushButton:pressed {\n"
                                          "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Refresh_Button_Down.png);\n"
                                          "background-repeat: no-repeat;\n"
                                          "padding: 0px;\n"
                                          "margin: 0px;\n"
                                          "border: none;\n"
                                          "background-position:center;\n"
                                          "outline:none;}\n"
                                          "QPushButton:disabled {\n"
                                          "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Refresh_Button_Down_Disabled.png);\n"
                                          "background-repeat: no-repeat;}")
        icon3 = QIcon()
        icon3.addFile(u"Assets/Refresh_Button.png", QSize(),
                      QIcon.Mode.Normal, QIcon.State.Off)
        self.Refresh_Button.setIcon(icon3)
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
                                       "QPushButton:pressed {\n"
                                       "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Save_Button_Down.png);\n"
                                       "background-repeat: no-repeat;\n"
                                       "padding: 0px;\n"
                                       "margin: 0px;\n"
                                       "border: none;\n"
                                       "background-position:center;\n"
                                       "outline:none;}\n"
                                       "QPushButton:disabled {\n"
                                       "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Save_Button_Down_Disabled.png);\n"
                                       "background-repeat: no-repeat;}")
        icon4 = QIcon()
        icon4.addFile(u"Assets/Save_Button.png", QSize(),
                      QIcon.Mode.Normal, QIcon.State.Off)
        self.Save_Button.setIcon(icon4)
        self.Save_Button.setIconSize(QSize(64, 64))
        self.Save_Button.setFlat(True)

        self.horizontalLayout.addWidget(self.Save_Button)

        self.Load_Button = QPushButton(self.groupBox)
        self.Load_Button.setObjectName(u"Load_Button")
        self.Load_Button.setMinimumSize(QSize(64, 64))
        self.Load_Button.setMaximumSize(QSize(64, 64))
        self.Load_Button.setAcceptDrops(False)
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
                                       "QPushButton:pressed {\n"
                                       "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Load_Button_Down.png);\n"
                                       "background-repeat: no-repeat;\n"
                                       "padding: 0px;\n"
                                       "margin: 0px;\n"
                                       "border: none;\n"
                                       "background-position:center;\n"
                                       "outline:none;}\n"
                                       "QPushButton:disabled {\n"
                                       "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Load_Button_Down_Disabled.png);\n"
                                       "background-repeat: no-repeat;}")
        self.Load_Button.setIconSize(QSize(64, 64))
        self.Load_Button.setFlat(True)

        self.horizontalLayout.addWidget(self.Load_Button)

        self.Main_Interface.addWidget(
            self.groupBox, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.Model_Box = QGroupBox(self.Main_Page)
        self.Model_Box.setObjectName(u"Model_Box")
        self.Model_Box.setGeometry(QRect(870, 140, 300, 521))
        self.Model_Box.setStyleSheet(u"QGroupBox {\n"
                                     "border-color:#98c5de;\n"
                                     "border-style: solid;\n"
                                     "border-width: 0px;\n"
                                     "border-radius: 10px;}")
        self.verticalLayout_2 = QVBoxLayout(self.Model_Box)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 10, 10, 0)
        self.Apollo_Sprite = QLabel(self.Model_Box)
        self.Apollo_Sprite.setObjectName(u"Apollo_Sprite")
        self.Apollo_Sprite.setPixmap(QPixmap(u"Assets/Apollo_Idle.gif"))
        self.Apollo_Sprite.setScaledContents(False)

        self.verticalLayout_2.addWidget(self.Apollo_Sprite)

        self.Change_Model_Button = QPushButton(self.Model_Box)
        self.Change_Model_Button.setObjectName(u"Change_Model_Button")
        self.Change_Model_Button.setMinimumSize(QSize(128, 128))
        self.Change_Model_Button.setMaximumSize(QSize(128, 128))
        self.Change_Model_Button.setStyleSheet(u"QPushButton {\n"
                                               "qproperty-icon: url(\" \");\n"
                                               "qproperty-iconSize: 128px 128px;\n"
                                               "width: 128px;\n"
                                               "height:128px;\n"
                                               "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Edit_Model_Button.png);\n"
                                               "  background-repeat: no-repeat;}\n"
                                               "QPushButton:hover {\n"
                                               "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Edit_Model_Button_Down.png);\n"
                                               "background-repeat: no-repeat;}\n"
                                               "QPushButton:pressed {\n"
                                               "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Edit_Model_Button_Down.png);\n"
                                               "background-repeat: no-repeat;\n"
                                               "padding: 0px;\n"
                                               "margin: 0px;\n"
                                               "border: none;\n"
                                               "background-position:center;\n"
                                               "outline:none;}\n"
                                               "QPushButton:disabled {\n"
                                               "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Edit_Model_Button_Down_Disabled.png);\n"
                                               "background-repeat: no-repeat;}")
        self.Change_Model_Button.setCheckable(False)
        self.Change_Model_Button.setFlat(True)

        self.verticalLayout_2.addWidget(
            self.Change_Model_Button, 0, Qt.AlignHCenter)

        self.Initials = QLabel(self.Main_Page)
        self.Initials.setObjectName(u"Initials")
        self.Initials.setGeometry(QRect(770, 100, 61, 26))
        self.Initials.setPixmap(QPixmap(u"Assets/APOLLO_Initials.png"))
        self.Title_Label = QLabel(self.Main_Page)
        self.Title_Label.setObjectName(u"Title_Label")
        self.Title_Label.setGeometry(QRect(400, 10, 357, 117))
        self.Title_Label.setMaximumSize(QSize(600, 16777215))
        self.Title_Label.setStyleSheet(u"")
        self.Title_Label.setPixmap(QPixmap(u"Assets/APOLLO_Title.png"))
        self.Title_Label.setScaledContents(False)
        self.Title_Label.setAlignment(Qt.AlignCenter)
        self.Title_Label.setMargin(0)
        self.Main_Content.addWidget(self.Main_Page)
        self.Settings_Page = QWidget()
        self.Settings_Page.setObjectName(u"Settings_Page")
        self.Settings_Title = QLabel(self.Settings_Page)
        self.Settings_Title.setObjectName(u"Settings_Title")
        self.Settings_Title.setGeometry(QRect(370, 10, 491, 121))
        self.Settings_Title.setPixmap(QPixmap(u"Assets/Settings_Title.png"))
        self.Checkbox_Frame = QFrame(self.Settings_Page)
        self.Checkbox_Frame.setObjectName(u"Checkbox_Frame")
        self.Checkbox_Frame.setGeometry(QRect(360, 140, 511, 400))
        self.Checkbox_Frame.setStyleSheet(u"QFrame {\n"
                                          "background-color: #243169;\n"
                                          "border-color:#98c5de;\n"
                                          "border-style: solid;\n"
                                          "border-width: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QCheckBox {\n"
                                          "background-color: #243169;\n"
                                          "font-size: 24px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton {\n"
                                          "background-color: #243169;\n"
                                          "}")
        self.verticalLayout = QVBoxLayout(self.Checkbox_Frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 0, 0, 0)
        self.Font_Setting_CheckBox = QCheckBox(self.Checkbox_Frame)
        self.Font_Setting_CheckBox.setObjectName(u"Font_Setting_CheckBox")
        self.Font_Setting_CheckBox.setTristate(False)

        self.verticalLayout.addWidget(self.Font_Setting_CheckBox)

        self.Autosave_CheckBox = QCheckBox(self.Checkbox_Frame)
        self.Autosave_CheckBox.setObjectName(u"Autosave_CheckBox")

        self.verticalLayout.addWidget(self.Autosave_CheckBox)

        self.Memory_CheckBox = QCheckBox(self.Checkbox_Frame)
        self.Memory_CheckBox.setObjectName(u"Memory_CheckBox")
        self.Memory_CheckBox.setChecked(True)

        self.verticalLayout.addWidget(self.Memory_CheckBox)

        self.checkBox_5 = QCheckBox(self.Checkbox_Frame)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout.addWidget(self.checkBox_5)

        self.checkBox_3 = QCheckBox(self.Checkbox_Frame)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout.addWidget(self.checkBox_3)

        self.Apply_Changes_Button = QPushButton(self.Settings_Page)
        self.Apply_Changes_Button.setObjectName(u"Apply_Changes_Button")
        self.Apply_Changes_Button.setGeometry(QRect(480, 540, 256, 64))
        self.Apply_Changes_Button.setMinimumSize(QSize(256, 64))
        self.Apply_Changes_Button.setMaximumSize(QSize(256, 16777215))
        self.Apply_Changes_Button.setStyleSheet(u"QPushButton {\n"
                                                "qproperty-icon: url(\" \");\n"
                                                "qproperty-iconSize: 256px 64px;\n"
                                                "width: 256px;\n"
                                                "height:64px;\n"
                                                "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Apply_Changes_Button.png);\n"
                                                "  background-repeat: no-repeat;}\n"
                                                "QPushButton:hover {\n"
                                                "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Apply_Changes_Button_Down.png);\n"
                                                "background-repeat: no-repeat;}\n"
                                                "QPushButton:pressed {\n"
                                                "background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/A.P.O.L.L.O/Assets/Apply_Changes_Button_Down.png);\n"
                                                "background-repeat: no-repeat;\n"
                                                "padding: 0px;\n"
                                                "margin: 0px;\n"
                                                "border: none;\n"
                                                "background-position:center;\n"
                                                "outline:none;}")
        self.Apply_Changes_Button.setFlat(True)
        self.Main_Content.addWidget(self.Settings_Page)
        self.Settings_Button = QPushButton(self.centralwidget)
        self.Settings_Button.setObjectName(u"Settings_Button")
        self.Settings_Button.setGeometry(QRect(10, 10, 38, 38))
        icon5 = QIcon()
        icon5.addFile(u"Assets/Cog.png", QSize(),
                      QIcon.Mode.Normal, QIcon.State.Off)
        self.Settings_Button.setIcon(icon5)
        self.Settings_Button.setIconSize(QSize(76, 76))
        self.Settings_Button.setCheckable(True)
        self.Settings_Button.setFlat(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Close_Window_Button.setDefault(False)
        self.Minimize_Window_Button.setDefault(False)
        self.Main_Content.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"A.P.O.L.L.O", None))
        self.Close_Window_Button.setText("")
        self.Minimize_Window_Button.setText("")
        self.Response_Display.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                 "p, li { white-space: pre-wrap; }\n"
                                                                 "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:32px; font-weight:400; font-style:normal;\">\n"
                                                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:30px;\"><br /></p></body></html>", None))
        self.groupBox.setTitle("")
# if QT_CONFIG(tooltip)
        self.Send_Button.setToolTip(
            QCoreApplication.translate("MainWindow", u"Submit", None))
# endif // QT_CONFIG(tooltip)
        self.Send_Button.setText("")
# if QT_CONFIG(tooltip)
        self.Web_Search_Button.setToolTip(
            QCoreApplication.translate("MainWindow", u"Web Search", None))
# endif // QT_CONFIG(tooltip)
        self.Web_Search_Button.setText("")
# if QT_CONFIG(tooltip)
        self.TTS_Button.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Text-to-Speech", None))
# endif // QT_CONFIG(tooltip)
        self.TTS_Button.setText("")
# if QT_CONFIG(tooltip)
        self.Refresh_Button.setToolTip(
            QCoreApplication.translate("MainWindow", u"Refresh", None))
# endif // QT_CONFIG(tooltip)
        self.Refresh_Button.setText("")
# if QT_CONFIG(tooltip)
        self.Save_Button.setToolTip(
            QCoreApplication.translate("MainWindow", u"Save", None))
# endif // QT_CONFIG(tooltip)
        self.Save_Button.setText("")
# if QT_CONFIG(tooltip)
        self.Load_Button.setToolTip(
            QCoreApplication.translate("MainWindow", u"Load", None))
# endif // QT_CONFIG(tooltip)
        self.Load_Button.setText("")
        self.Model_Box.setTitle("")
        self.Apollo_Sprite.setText("")
# if QT_CONFIG(tooltip)
        self.Change_Model_Button.setToolTip(
            QCoreApplication.translate("MainWindow", u"Change Model", None))
# endif // QT_CONFIG(tooltip)
        self.Change_Model_Button.setText("")
        self.Initials.setText("")
        self.Title_Label.setText("")
        self.Settings_Title.setText("")
        self.Font_Setting_CheckBox.setText(
            QCoreApplication.translate("MainWindow", u"Larger Font", None))
        self.Autosave_CheckBox.setText(QCoreApplication.translate(
            "MainWindow", u"Automatically save last conversation when closing", None))
        self.Memory_CheckBox.setText(QCoreApplication.translate(
            "MainWindow", u"Save conversations to memory", None))
        self.checkBox_5.setText(QCoreApplication.translate(
            "MainWindow", u"Nothing yet", None))
        self.checkBox_3.setText(QCoreApplication.translate(
            "MainWindow", u"Nothing yet", None))
        self.Apply_Changes_Button.setText("")
        self.Settings_Button.setText("")
    # retranslateUi
