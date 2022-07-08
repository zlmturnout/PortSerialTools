# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_Serial_COM_tool.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)
import qpprcc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(992, 806)
        icon = QIcon()
        icon.addFile(u":/icons/icons/port_ico.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(128, 128))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_7 = QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.groupBox_2.setMaximumSize(QSize(16777215, 16000))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.groupBox_2.setFont(font)
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(9, 12, -1, 12)
        self.recv_data = QTextEdit(self.groupBox_2)
        self.recv_data.setObjectName(u"recv_data")
        self.recv_data.setMinimumSize(QSize(450, 250))
        self.recv_data.setMaximumSize(QSize(16777215, 280))
        palette = QPalette()
        brush = QBrush(QColor(255, 85, 176, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush1 = QBrush(QColor(255, 85, 176, 128))
        brush1.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        brush3 = QBrush(QColor(0, 0, 0, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.recv_data.setPalette(palette)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(16)
        font1.setBold(False)
        self.recv_data.setFont(font1)

        self.gridLayout_3.addWidget(self.recv_data, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 58, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Hex_check = QCheckBox(self.centralwidget)
        self.Hex_check.setObjectName(u"Hex_check")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Hex_check.sizePolicy().hasHeightForWidth())
        self.Hex_check.setSizePolicy(sizePolicy1)
        self.Hex_check.setMinimumSize(QSize(100, 30))
        self.Hex_check.setFont(font)

        self.verticalLayout_2.addWidget(self.Hex_check)

        self.time_stamp = QCheckBox(self.centralwidget)
        self.time_stamp.setObjectName(u"time_stamp")
        self.time_stamp.setFont(font)

        self.verticalLayout_2.addWidget(self.time_stamp)

        self.save_text = QPushButton(self.centralwidget)
        self.save_text.setObjectName(u"save_text")
        sizePolicy1.setHeightForWidth(self.save_text.sizePolicy().hasHeightForWidth())
        self.save_text.setSizePolicy(sizePolicy1)
        self.save_text.setMinimumSize(QSize(100, 40))
        self.save_text.setFont(font)

        self.verticalLayout_2.addWidget(self.save_text)

        self.clear_recv = QPushButton(self.centralwidget)
        self.clear_recv.setObjectName(u"clear_recv")
        sizePolicy1.setHeightForWidth(self.clear_recv.sizePolicy().hasHeightForWidth())
        self.clear_recv.setSizePolicy(sizePolicy1)
        self.clear_recv.setMinimumSize(QSize(100, 40))
        self.clear_recv.setFont(font)

        self.verticalLayout_2.addWidget(self.clear_recv)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 0, 2, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setMinimumSize(QSize(200, 300))
        self.groupBox.setFont(font)
        self.gridLayout_5 = QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.search_port = QPushButton(self.groupBox)
        self.search_port.setObjectName(u"search_port")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.search_port.sizePolicy().hasHeightForWidth())
        self.search_port.setSizePolicy(sizePolicy3)
        self.search_port.setMinimumSize(QSize(200, 0))
        palette1 = QPalette()
        brush4 = QBrush(QColor(255, 85, 127, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        brush5 = QBrush(QColor(0, 170, 255, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush5)
        brush6 = QBrush(QColor(0, 170, 127, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush6)
        brush7 = QBrush(QColor(255, 85, 127, 128))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        brush8 = QBrush(QColor(170, 255, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        brush9 = QBrush(QColor(240, 240, 240, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.search_port.setPalette(palette1)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(18)
        font2.setBold(True)
        self.search_port.setFont(font2)
        self.search_port.setIconSize(QSize(30, 30))

        self.gridLayout_5.addWidget(self.search_port, 0, 0, 1, 6)

        self.COM_info = QLabel(self.groupBox)
        self.COM_info.setObjectName(u"COM_info")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.COM_info.sizePolicy().hasHeightForWidth())
        self.COM_info.setSizePolicy(sizePolicy4)
        palette2 = QPalette()
        brush10 = QBrush(QColor(21, 193, 255, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        self.COM_info.setPalette(palette2)
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.COM_info.setFont(font3)
        self.COM_info.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.COM_info, 2, 0, 1, 6)

        self.COM_port = QComboBox(self.groupBox)
        self.COM_port.setObjectName(u"COM_port")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.COM_port.sizePolicy().hasHeightForWidth())
        self.COM_port.setSizePolicy(sizePolicy5)
        self.COM_port.setMinimumSize(QSize(80, 0))

        self.gridLayout_5.addWidget(self.COM_port, 1, 1, 1, 3)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 4, 0, 1, 2)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_2, 3, 0, 1, 2)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_5.addWidget(self.label_6, 6, 0, 1, 2)

        self.stopbits = QComboBox(self.groupBox)
        self.stopbits.addItem("")
        self.stopbits.addItem("")
        self.stopbits.addItem("")
        self.stopbits.setObjectName(u"stopbits")

        self.gridLayout_5.addWidget(self.stopbits, 6, 3, 1, 3)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(50, 0))
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)

        self.bytesize = QComboBox(self.groupBox)
        self.bytesize.addItem("")
        self.bytesize.addItem("")
        self.bytesize.addItem("")
        self.bytesize.addItem("")
        self.bytesize.setObjectName(u"bytesize")

        self.gridLayout_5.addWidget(self.bytesize, 4, 3, 1, 3)

        self.parity = QComboBox(self.groupBox)
        self.parity.addItem("")
        self.parity.addItem("")
        self.parity.addItem("")
        self.parity.addItem("")
        self.parity.addItem("")
        self.parity.setObjectName(u"parity")

        self.gridLayout_5.addWidget(self.parity, 5, 3, 1, 3)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(50, 0))

        self.gridLayout_5.addWidget(self.label_4, 5, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy6)
        self.label_7.setMinimumSize(QSize(30, 30))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_7, 7, 0, 1, 2)

        self.baudrate = QComboBox(self.groupBox)
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.setObjectName(u"baudrate")

        self.gridLayout_5.addWidget(self.baudrate, 3, 3, 1, 3)

        self.COM_status = QLabel(self.groupBox)
        self.COM_status.setObjectName(u"COM_status")
        palette3 = QPalette()
        brush11 = QBrush(QColor(0, 200, 0, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush11)
        brush12 = QBrush(QColor(85, 255, 0, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush12)
        brush13 = QBrush(QColor(85, 255, 0, 128))
        brush13.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush13)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush11)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush13)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.COM_status.setPalette(palette3)

        self.gridLayout_5.addWidget(self.COM_status, 1, 4, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 7, 5, 1, 1)

        self.transmit_time = QSpinBox(self.groupBox)
        self.transmit_time.setObjectName(u"transmit_time")
        self.transmit_time.setAlignment(Qt.AlignCenter)
        self.transmit_time.setMinimum(100)
        self.transmit_time.setMaximum(10000)
        self.transmit_time.setSingleStep(100)

        self.gridLayout_5.addWidget(self.transmit_time, 7, 2, 1, 3)


        self.gridLayout_6.addWidget(self.groupBox, 0, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 118, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 1, 1, 2, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox1 = QGroupBox(self.centralwidget)
        self.groupBox1.setObjectName(u"groupBox1")
        self.groupBox1.setMinimumSize(QSize(450, 0))
        self.groupBox1.setMaximumSize(QSize(16777215, 200))
        self.groupBox1.setFont(font)
        self.gridLayout = QGridLayout(self.groupBox1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 12, 9, 12)
        self.send_data = QTextEdit(self.groupBox1)
        self.send_data.setObjectName(u"send_data")
        self.send_data.setMinimumSize(QSize(400, 150))
        self.send_data.setMaximumSize(QSize(16777215, 180))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Text, brush6)
        brush14 = QBrush(QColor(0, 170, 127, 128))
        brush14.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.send_data.setPalette(palette4)
        self.send_data.setFont(font1)

        self.gridLayout.addWidget(self.send_data, 0, 0, 1, 1)

        self.Crc_code = QLineEdit(self.groupBox1)
        self.Crc_code.setObjectName(u"Crc_code")

        self.gridLayout.addWidget(self.Crc_code, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox1, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.is_hex = QCheckBox(self.centralwidget)
        self.is_hex.setObjectName(u"is_hex")
        self.is_hex.setFont(font)

        self.verticalLayout.addWidget(self.is_hex)

        self.hex_send = QPushButton(self.centralwidget)
        self.hex_send.setObjectName(u"hex_send")
        sizePolicy1.setHeightForWidth(self.hex_send.sizePolicy().hasHeightForWidth())
        self.hex_send.setSizePolicy(sizePolicy1)
        self.hex_send.setMinimumSize(QSize(100, 40))
        self.hex_send.setFont(font)

        self.verticalLayout.addWidget(self.hex_send)

        self.Add_crc16 = QPushButton(self.centralwidget)
        self.Add_crc16.setObjectName(u"Add_crc16")
        sizePolicy1.setHeightForWidth(self.Add_crc16.sizePolicy().hasHeightForWidth())
        self.Add_crc16.setSizePolicy(sizePolicy1)
        self.Add_crc16.setMinimumSize(QSize(100, 40))
        self.Add_crc16.setFont(font)

        self.verticalLayout.addWidget(self.Add_crc16)

        self.text_send = QPushButton(self.centralwidget)
        self.text_send.setObjectName(u"text_send")
        sizePolicy1.setHeightForWidth(self.text_send.sizePolicy().hasHeightForWidth())
        self.text_send.setSizePolicy(sizePolicy1)
        self.text_send.setMinimumSize(QSize(100, 40))
        self.text_send.setFont(font)

        self.verticalLayout.addWidget(self.text_send)

        self.clear_send = QPushButton(self.centralwidget)
        self.clear_send.setObjectName(u"clear_send")
        sizePolicy1.setHeightForWidth(self.clear_send.sizePolicy().hasHeightForWidth())
        self.clear_send.setSizePolicy(sizePolicy1)
        self.clear_send.setMinimumSize(QSize(100, 40))
        self.clear_send.setFont(font)

        self.verticalLayout.addWidget(self.clear_send)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_2, 2, 0, 3, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.open_port = QPushButton(self.centralwidget)
        self.open_port.setObjectName(u"open_port")
        self.open_port.setMinimumSize(QSize(100, 40))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(16)
        font4.setBold(True)
        self.open_port.setFont(font4)

        self.horizontalLayout.addWidget(self.open_port)

        self.close_port = QPushButton(self.centralwidget)
        self.close_port.setObjectName(u"close_port")
        self.close_port.setMinimumSize(QSize(100, 40))
        self.close_port.setFont(font4)

        self.horizontalLayout.addWidget(self.close_port)


        self.gridLayout_6.addLayout(self.horizontalLayout, 3, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 88, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_4, 4, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 992, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Receive DATA", None))
        self.Hex_check.setText(QCoreApplication.translate("MainWindow", u"Hex Recev", None))
        self.time_stamp.setText(QCoreApplication.translate("MainWindow", u"Time stamp", None))
        self.save_text.setText(QCoreApplication.translate("MainWindow", u"Save text", None))
        self.clear_recv.setText(QCoreApplication.translate("MainWindow", u"Cear", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Serial Port", None))
        self.search_port.setText(QCoreApplication.translate("MainWindow", u"Search port", None))
        self.COM_info.setText(QCoreApplication.translate("MainWindow", u"Select COM port", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Bytesize:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Baudrate:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Stopbits:", None))
        self.stopbits.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.stopbits.setItemText(1, QCoreApplication.translate("MainWindow", u"1.5", None))
        self.stopbits.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Port:", None))
        self.bytesize.setItemText(0, QCoreApplication.translate("MainWindow", u"8", None))
        self.bytesize.setItemText(1, QCoreApplication.translate("MainWindow", u"5", None))
        self.bytesize.setItemText(2, QCoreApplication.translate("MainWindow", u"6", None))
        self.bytesize.setItemText(3, QCoreApplication.translate("MainWindow", u"7", None))

        self.parity.setItemText(0, QCoreApplication.translate("MainWindow", u"N", None))
        self.parity.setItemText(1, QCoreApplication.translate("MainWindow", u"E", None))
        self.parity.setItemText(2, QCoreApplication.translate("MainWindow", u"O", None))
        self.parity.setItemText(3, QCoreApplication.translate("MainWindow", u"M", None))
        self.parity.setItemText(4, QCoreApplication.translate("MainWindow", u"S", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Parity:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Trans_T:", None))
        self.baudrate.setItemText(0, QCoreApplication.translate("MainWindow", u"9600", None))
        self.baudrate.setItemText(1, QCoreApplication.translate("MainWindow", u"2400", None))
        self.baudrate.setItemText(2, QCoreApplication.translate("MainWindow", u"4800", None))
        self.baudrate.setItemText(3, QCoreApplication.translate("MainWindow", u"14400", None))
        self.baudrate.setItemText(4, QCoreApplication.translate("MainWindow", u"19200", None))
        self.baudrate.setItemText(5, QCoreApplication.translate("MainWindow", u"38400", None))
        self.baudrate.setItemText(6, QCoreApplication.translate("MainWindow", u"57600", None))
        self.baudrate.setItemText(7, QCoreApplication.translate("MainWindow", u"76800", None))
        self.baudrate.setItemText(8, QCoreApplication.translate("MainWindow", u"12800", None))
        self.baudrate.setItemText(9, QCoreApplication.translate("MainWindow", u"115200", None))

        self.COM_status.setText(QCoreApplication.translate("MainWindow", u"Wait", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.groupBox1.setTitle(QCoreApplication.translate("MainWindow", u"Send DATA", None))
        self.send_data.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.Crc_code.setToolTip(QCoreApplication.translate("MainWindow", u"add CRC if needed", None))
#endif // QT_CONFIG(tooltip)
        self.Crc_code.setInputMask("")
        self.Crc_code.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CRC NUM", None))
        self.is_hex.setText(QCoreApplication.translate("MainWindow", u"Is Hex?", None))
        self.hex_send.setText(QCoreApplication.translate("MainWindow", u"Hex Send", None))
        self.Add_crc16.setText(QCoreApplication.translate("MainWindow", u"Add CRC16", None))
        self.text_send.setText(QCoreApplication.translate("MainWindow", u"Text Send", None))
        self.clear_send.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.open_port.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.close_port.setText(QCoreApplication.translate("MainWindow", u"Close", None))
    # retranslateUi

