# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(402, 205)
        icon = QIcon()
        icon.addFile(u":/ico/icons/audio.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(50, 0))
        self.label.setMaximumSize(QSize(50, 16777215))
        self.label.setMargin(2)

        self.horizontalLayout.addWidget(self.label)

        self.lSrcPath = QLineEdit(self.centralwidget)
        self.lSrcPath.setObjectName(u"lSrcPath")
        self.lSrcPath.setEnabled(True)
        self.lSrcPath.setMouseTracking(False)
        self.lSrcPath.setFocusPolicy(Qt.NoFocus)
        self.lSrcPath.setContextMenuPolicy(Qt.NoContextMenu)
        self.lSrcPath.setAcceptDrops(False)
        self.lSrcPath.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lSrcPath)

        self.btnSrc = QPushButton(self.centralwidget)
        self.btnSrc.setObjectName(u"btnSrc")

        self.horizontalLayout.addWidget(self.btnSrc)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(50, 0))
        self.label_2.setMaximumSize(QSize(50, 16777215))
        self.label_2.setMargin(2)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lSavePath = QLineEdit(self.centralwidget)
        self.lSavePath.setObjectName(u"lSavePath")
        self.lSavePath.setEnabled(True)
        self.lSavePath.setMouseTracking(False)
        self.lSavePath.setFocusPolicy(Qt.NoFocus)
        self.lSavePath.setAcceptDrops(False)
        self.lSavePath.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lSavePath)

        self.boxFormat = QComboBox(self.centralwidget)
        self.boxFormat.addItem("")
        self.boxFormat.addItem("")
        self.boxFormat.setObjectName(u"boxFormat")

        self.horizontalLayout_2.addWidget(self.boxFormat)

        self.btnSave = QPushButton(self.centralwidget)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout_2.addWidget(self.btnSave)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.btnCommit = QPushButton(self.centralwidget)
        self.btnCommit.setObjectName(u"btnCommit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnCommit.sizePolicy().hasHeightForWidth())
        self.btnCommit.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.btnCommit)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.sbV = QStatusBar(MainWindow)
        self.sbV.setObjectName(u"sbV")
        self.sbV.setStyleSheet(u"color: rgb(102, 102, 102);")
        MainWindow.setStatusBar(self.sbV)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u97f3\u9891\u63d0\u53d6", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6e90\u6587\u4ef6:", None))
        self.lSrcPath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u6e90\u6587\u4ef6\u5730\u5740", None))
        self.btnSrc.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u4e3a:", None))
        self.lSavePath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u4fdd\u5b58\u6587\u4ef6\u5939", None))
        self.boxFormat.setItemText(0, QCoreApplication.translate("MainWindow", u"mp3", None))
        self.boxFormat.setItemText(1, QCoreApplication.translate("MainWindow", u"wav", None))

        self.btnSave.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8def\u5f84", None))
        self.btnCommit.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
    # retranslateUi

