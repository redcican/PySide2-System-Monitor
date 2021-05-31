# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar
from PySide2extn.SpiralProgressBar import spiralProgressBar

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(905, 668)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(72, 72, 72);\n"
"border:none\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"background-color:#2c313c\n"
"}")
        self.centralwidget.setLocale(QLocale(QLocale.English, QLocale.Germany))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy)
        self.header_frame.setLayoutDirection(Qt.LeftToRight)
        self.header_frame.setStyleSheet(u"background-color:#24354b")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.header_frame.setLineWidth(1)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(10, 5, 5, 0)
        self.header_left_frame = QFrame(self.header_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        self.header_left_frame.setStyleSheet(u"padding:0;\n"
"margin:0")
        self.header_left_frame.setFrameShape(QFrame.StyledPanel)
        self.header_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 5)
        self.open_close_side_bar_btn = QPushButton(self.header_left_frame)
        self.open_close_side_bar_btn.setObjectName(u"open_close_side_bar_btn")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.open_close_side_bar_btn.setFont(font)
        self.open_close_side_bar_btn.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"margin:0;")
        icon1 = QIcon()
        icon1.addFile(u"icons/left_align.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_btn.setIcon(icon1)
        self.open_close_side_bar_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.open_close_side_bar_btn)


        self.horizontalLayout.addWidget(self.header_left_frame, 0, Qt.AlignLeft)

        self.header_center_frame = QFrame(self.header_frame)
        self.header_center_frame.setObjectName(u"header_center_frame")
        self.header_center_frame.setFrameShape(QFrame.StyledPanel)
        self.header_center_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_center_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.header_center_frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(20, 20))
        font1 = QFont()
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.label.setPixmap(QPixmap(u"icons/air-play.svg"))
        self.label.setScaledContents(False)

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignRight)

        self.label_2 = QLabel(self.header_center_frame)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(14)
        self.label_2.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.header_center_frame)

        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.header_right_frame)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon2 = QIcon()
        icon2.addFile(u"icons/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.header_right_frame)
        self.restore_window_button.setObjectName(u"restore_window_button")
        icon3 = QIcon()
        icon3.addFile(u"icons/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.header_right_frame)
        self.close_window_button.setObjectName(u"close_window_button")
        icon4 = QIcon()
        icon4.addFile(u"icons/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon4)
        self.close_window_button.setFlat(False)

        self.horizontalLayout_2.addWidget(self.close_window_button)


        self.horizontalLayout.addWidget(self.header_right_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy1)
        self.main_body_frame.setFrameShape(QFrame.StyledPanel)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.left_menu_cont_frame = QFrame(self.main_body_frame)
        self.left_menu_cont_frame.setObjectName(u"left_menu_cont_frame")
        self.left_menu_cont_frame.setMinimumSize(QSize(50, 0))
        self.left_menu_cont_frame.setMaximumSize(QSize(20, 16777215))
        self.left_menu_cont_frame.setStyleSheet(u"background-color:#24354b")
        self.left_menu_cont_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_cont_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.left_menu_cont_frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 10, 0, 0)
        self.menu_frame = QFrame(self.left_menu_cont_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(100, 0))
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.menu_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.menu_frame)
        self.label_7.setObjectName(u"label_7")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.label_7.setFont(font3)
        self.label_7.setMargin(5)

        self.gridLayout.addWidget(self.label_7, 3, 1, 1, 1, Qt.AlignLeft)

        self.label_8 = QLabel(self.menu_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)
        self.label_8.setMargin(5)

        self.gridLayout.addWidget(self.label_8, 4, 1, 1, 1, Qt.AlignLeft)

        self.storage_page_btn = QPushButton(self.menu_frame)
        self.storage_page_btn.setObjectName(u"storage_page_btn")
        self.storage_page_btn.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u"icons/storage.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.storage_page_btn.setIcon(icon5)
        self.storage_page_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.storage_page_btn, 4, 0, 1, 1, Qt.AlignLeft)

        self.label_4 = QLabel(self.menu_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setMargin(5)

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1, Qt.AlignLeft)

        self.label_5 = QLabel(self.menu_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)
        self.label_5.setMargin(5)

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1, Qt.AlignLeft)

        self.system_page_btn = QPushButton(self.menu_frame)
        self.system_page_btn.setObjectName(u"system_page_btn")
        self.system_page_btn.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u"icons/system.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.system_page_btn.setIcon(icon6)
        self.system_page_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.system_page_btn, 2, 0, 1, 1, Qt.AlignLeft)

        self.network_page_btn = QPushButton(self.menu_frame)
        self.network_page_btn.setObjectName(u"network_page_btn")
        self.network_page_btn.setFont(font1)
        icon7 = QIcon()
        icon7.addFile(u"icons/network.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.network_page_btn.setIcon(icon7)
        self.network_page_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.network_page_btn, 5, 0, 1, 1, Qt.AlignLeft)

        self.label_10 = QLabel(self.menu_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setMargin(5)

        self.gridLayout.addWidget(self.label_10, 5, 1, 1, 1, Qt.AlignLeft)

        self.cpu_page_btn = QPushButton(self.menu_frame)
        self.cpu_page_btn.setObjectName(u"cpu_page_btn")
        self.cpu_page_btn.setFont(font1)
        icon8 = QIcon()
        icon8.addFile(u"icons/cpu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cpu_page_btn.setIcon(icon8)
        self.cpu_page_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.cpu_page_btn, 0, 0, 1, 1, Qt.AlignLeft)

        self.activity_page_btn = QPushButton(self.menu_frame)
        self.activity_page_btn.setObjectName(u"activity_page_btn")
        self.activity_page_btn.setFont(font1)
        icon9 = QIcon()
        icon9.addFile(u"icons/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.activity_page_btn.setIcon(icon9)
        self.activity_page_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.activity_page_btn, 3, 0, 1, 1, Qt.AlignLeft)

        self.battery_page_btn = QPushButton(self.menu_frame)
        self.battery_page_btn.setObjectName(u"battery_page_btn")
        self.battery_page_btn.setFont(font1)
        icon10 = QIcon()
        icon10.addFile(u"icons/battery.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.battery_page_btn.setIcon(icon10)
        self.battery_page_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.battery_page_btn, 1, 0, 1, 1, Qt.AlignLeft)

        self.label_6 = QLabel(self.menu_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
        self.label_6.setMargin(5)

        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1, Qt.AlignLeft)


        self.horizontalLayout_9.addWidget(self.menu_frame, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_8.addWidget(self.left_menu_cont_frame)

        self.main_body_contents = QFrame(self.main_body_frame)
        self.main_body_contents.setObjectName(u"main_body_contents")
        self.main_body_contents.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_body_contents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.main_body_contents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.cpu_and_memory_delete = QWidget()
        self.cpu_and_memory_delete.setObjectName(u"cpu_and_memory_delete")
        self.verticalLayout_3 = QVBoxLayout(self.cpu_and_memory_delete)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget.addWidget(self.cpu_and_memory_delete)
        self.cpu_and_memory = QWidget()
        self.cpu_and_memory.setObjectName(u"cpu_and_memory")
        self.verticalLayout_15 = QVBoxLayout(self.cpu_and_memory)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.cpu_and_memory)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.cpu_ram_info_frame = QFrame(self.frame)
        self.cpu_ram_info_frame.setObjectName(u"cpu_ram_info_frame")
        self.cpu_ram_info_frame.setFrameShape(QFrame.StyledPanel)
        self.cpu_ram_info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.cpu_ram_info_frame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.cpu_info = QFrame(self.cpu_ram_info_frame)
        self.cpu_info.setObjectName(u"cpu_info")
        self.cpu_info.setFrameShape(QFrame.StyledPanel)
        self.cpu_info.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.cpu_info)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_9 = QLabel(self.cpu_info)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_6.addWidget(self.label_9, 0, 0, 1, 1)

        self.cpu_count = QLabel(self.cpu_info)
        self.cpu_count.setObjectName(u"cpu_count")

        self.gridLayout_6.addWidget(self.cpu_count, 0, 1, 1, 1)

        self.label_16 = QLabel(self.cpu_info)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_6.addWidget(self.label_16, 1, 0, 1, 1)

        self.cpu_per = QLabel(self.cpu_info)
        self.cpu_per.setObjectName(u"cpu_per")

        self.gridLayout_6.addWidget(self.cpu_per, 1, 1, 1, 1)

        self.label_19 = QLabel(self.cpu_info)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_6.addWidget(self.label_19, 2, 0, 1, 1)

        self.cpu_main_core = QLabel(self.cpu_info)
        self.cpu_main_core.setObjectName(u"cpu_main_core")

        self.gridLayout_6.addWidget(self.cpu_main_core, 2, 1, 1, 1)


        self.verticalLayout_16.addWidget(self.cpu_info)

        self.ram_info = QFrame(self.cpu_ram_info_frame)
        self.ram_info.setObjectName(u"ram_info")
        self.ram_info.setFrameShape(QFrame.StyledPanel)
        self.ram_info.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.ram_info)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_21 = QLabel(self.ram_info)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_7.addWidget(self.label_21, 0, 0, 1, 1)

        self.total_ram = QLabel(self.ram_info)
        self.total_ram.setObjectName(u"total_ram")

        self.gridLayout_7.addWidget(self.total_ram, 0, 1, 1, 1)

        self.label_25 = QLabel(self.ram_info)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_7.addWidget(self.label_25, 1, 0, 1, 1)

        self.availabel_ram = QLabel(self.ram_info)
        self.availabel_ram.setObjectName(u"availabel_ram")

        self.gridLayout_7.addWidget(self.availabel_ram, 1, 1, 1, 1)

        self.label_31 = QLabel(self.ram_info)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_7.addWidget(self.label_31, 2, 0, 1, 1)

        self.used_ram = QLabel(self.ram_info)
        self.used_ram.setObjectName(u"used_ram")

        self.gridLayout_7.addWidget(self.used_ram, 2, 1, 1, 1)

        self.label_34 = QLabel(self.ram_info)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_7.addWidget(self.label_34, 3, 0, 1, 1)

        self.free_ram = QLabel(self.ram_info)
        self.free_ram.setObjectName(u"free_ram")

        self.gridLayout_7.addWidget(self.free_ram, 3, 1, 1, 1)

        self.label_41 = QLabel(self.ram_info)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_7.addWidget(self.label_41, 4, 0, 1, 1)

        self.ram_usage = QLabel(self.ram_info)
        self.ram_usage.setObjectName(u"ram_usage")

        self.gridLayout_7.addWidget(self.ram_usage, 4, 1, 1, 1)


        self.verticalLayout_16.addWidget(self.ram_info)


        self.horizontalLayout_14.addWidget(self.cpu_ram_info_frame)

        self.progressbar_frame = QFrame(self.frame)
        self.progressbar_frame.setObjectName(u"progressbar_frame")
        self.progressbar_frame.setFrameShape(QFrame.StyledPanel)
        self.progressbar_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.progressbar_frame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.cpu_usage_progressbar = roundProgressBar(self.progressbar_frame)
        self.cpu_usage_progressbar.setObjectName(u"cpu_usage_progressbar")

        self.verticalLayout_17.addWidget(self.cpu_usage_progressbar)

        self.raw_usage_spiralbar = spiralProgressBar(self.progressbar_frame)
        self.raw_usage_spiralbar.setObjectName(u"raw_usage_spiralbar")
        self.raw_usage_spiralbar.setMinimumSize(QSize(0, 0))

        self.verticalLayout_17.addWidget(self.raw_usage_spiralbar)


        self.horizontalLayout_14.addWidget(self.progressbar_frame)


        self.verticalLayout_15.addWidget(self.frame)

        self.stackedWidget.addWidget(self.cpu_and_memory)
        self.battery = QWidget()
        self.battery.setObjectName(u"battery")
        self.verticalLayout_4 = QVBoxLayout(self.battery)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_27 = QLabel(self.battery)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font)

        self.verticalLayout_4.addWidget(self.label_27, 0, Qt.AlignBottom)

        self.frame_2 = QFrame(self.battery)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFont(font1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(20)
        self.gridLayout_4.setContentsMargins(-1, -1, -1, 30)
        self.battery_charge = QLabel(self.frame_2)
        self.battery_charge.setObjectName(u"battery_charge")
        self.battery_charge.setFont(font1)

        self.gridLayout_4.addWidget(self.battery_charge, 1, 1, 1, 1)

        self.label_28 = QLabel(self.frame_2)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)

        self.gridLayout_4.addWidget(self.label_28, 0, 0, 1, 1)

        self.battery_plugged = QLabel(self.frame_2)
        self.battery_plugged.setObjectName(u"battery_plugged")
        self.battery_plugged.setFont(font1)

        self.gridLayout_4.addWidget(self.battery_plugged, 3, 1, 1, 1)

        self.battery_status = QLabel(self.frame_2)
        self.battery_status.setObjectName(u"battery_status")
        self.battery_status.setFont(font1)

        self.gridLayout_4.addWidget(self.battery_status, 0, 1, 1, 1)

        self.label_30 = QLabel(self.frame_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font1)

        self.gridLayout_4.addWidget(self.label_30, 1, 0, 1, 1)

        self.label_35 = QLabel(self.frame_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font1)

        self.gridLayout_4.addWidget(self.label_35, 3, 0, 1, 1)

        self.label_33 = QLabel(self.frame_2)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font1)

        self.gridLayout_4.addWidget(self.label_33, 2, 0, 1, 1)

        self.battery_time_left = QLabel(self.frame_2)
        self.battery_time_left.setObjectName(u"battery_time_left")
        self.battery_time_left.setFont(font1)

        self.gridLayout_4.addWidget(self.battery_time_left, 2, 1, 1, 1)

        self.battery_progressbar = roundProgressBar(self.frame_2)
        self.battery_progressbar.setObjectName(u"battery_progressbar")
        self.battery_progressbar.setMinimumSize(QSize(150, 150))
        self.battery_progressbar.setMaximumSize(QSize(150, 150))

        self.gridLayout_4.addWidget(self.battery_progressbar, 0, 2, 4, 1)


        self.verticalLayout_4.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.battery)
        self.activities = QWidget()
        self.activities.setObjectName(u"activities")
        self.verticalLayout_6 = QVBoxLayout(self.activities)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_4 = QFrame(self.activities)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_50 = QLabel(self.frame_4)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font3)

        self.horizontalLayout_10.addWidget(self.label_50)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.activity_search = QLineEdit(self.frame_7)
        self.activity_search.setObjectName(u"activity_search")
        self.activity_search.setFont(font1)
        self.activity_search.setStyleSheet(u"color:rgb(255, 255, 255)")

        self.horizontalLayout_11.addWidget(self.activity_search)

        self.pushButton_3 = QPushButton(self.frame_7)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon11 = QIcon()
        icon11.addFile(u"icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon11)

        self.horizontalLayout_11.addWidget(self.pushButton_3)


        self.horizontalLayout_10.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.activities)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.tableWidget = QTableWidget(self.frame_5)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet(u"background-color:#24354b")
        self.tableWidget.setGridStyle(Qt.SolidLine)

        self.horizontalLayout_13.addWidget(self.tableWidget)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.activities)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        self.pushButton_4.setFont(font4)
        self.pushButton_4.setStyleSheet(u"color:rgb(255, 255, 255)")

        self.horizontalLayout_12.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font4)
        self.pushButton_5.setStyleSheet(u"color:rgb(255, 255, 255)")

        self.horizontalLayout_12.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font4)
        self.pushButton_6.setStyleSheet(u"color:rgb(255, 255, 255)")

        self.horizontalLayout_12.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_6)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font4)
        self.pushButton_7.setStyleSheet(u"color:rgb(255, 255, 255)")

        self.horizontalLayout_12.addWidget(self.pushButton_7)


        self.verticalLayout_6.addWidget(self.frame_6, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.activities)
        self.storage = QWidget()
        self.storage.setObjectName(u"storage")
        self.verticalLayout_7 = QVBoxLayout(self.storage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_51 = QLabel(self.storage)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font)

        self.verticalLayout_7.addWidget(self.label_51)

        self.storageTable = QTableWidget(self.storage)
        if (self.storageTable.columnCount() < 9):
            self.storageTable.setColumnCount(9)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font1);
        __qtablewidgetitem8.setBackground(QColor(255, 255, 255));
        self.storageTable.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font1);
        self.storageTable.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font1);
        self.storageTable.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font1);
        self.storageTable.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font1);
        self.storageTable.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font1);
        self.storageTable.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font1);
        self.storageTable.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font1);
        self.storageTable.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(8, __qtablewidgetitem16)
        self.storageTable.setObjectName(u"storageTable")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(False)
        self.storageTable.setFont(font5)

        self.verticalLayout_7.addWidget(self.storageTable)

        self.stackedWidget.addWidget(self.storage)
        self.sensors = QWidget()
        self.sensors.setObjectName(u"sensors")
        self.verticalLayout_8 = QVBoxLayout(self.sensors)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.stackedWidget.addWidget(self.sensors)
        self.networks = QWidget()
        self.networks.setObjectName(u"networks")
        self.verticalLayout_9 = QVBoxLayout(self.networks)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.scrollArea = QScrollArea(self.networks)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -135, 802, 772))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_53 = QLabel(self.frame_8)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font)

        self.verticalLayout_11.addWidget(self.label_53)

        self.net_stats_table = QTableWidget(self.frame_8)
        if (self.net_stats_table.columnCount() < 5):
            self.net_stats_table.setColumnCount(5)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font1);
        self.net_stats_table.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font1);
        self.net_stats_table.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font1);
        self.net_stats_table.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font1);
        self.net_stats_table.setHorizontalHeaderItem(4, __qtablewidgetitem21)
        self.net_stats_table.setObjectName(u"net_stats_table")
        self.net_stats_table.setMinimumSize(QSize(0, 150))

        self.verticalLayout_11.addWidget(self.net_stats_table)


        self.verticalLayout_10.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_54 = QLabel(self.frame_9)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font)

        self.verticalLayout_12.addWidget(self.label_54)

        self.net_io_table = QTableWidget(self.frame_9)
        if (self.net_io_table.columnCount() < 9):
            self.net_io_table.setColumnCount(9)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font1);
        self.net_io_table.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font1);
        self.net_io_table.setHorizontalHeaderItem(1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font1);
        self.net_io_table.setHorizontalHeaderItem(2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font1);
        self.net_io_table.setHorizontalHeaderItem(3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font1);
        self.net_io_table.setHorizontalHeaderItem(4, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font1);
        self.net_io_table.setHorizontalHeaderItem(5, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font1);
        self.net_io_table.setHorizontalHeaderItem(6, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font1);
        self.net_io_table.setHorizontalHeaderItem(7, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font1);
        self.net_io_table.setHorizontalHeaderItem(8, __qtablewidgetitem30)
        self.net_io_table.setObjectName(u"net_io_table")
        self.net_io_table.setMinimumSize(QSize(0, 150))

        self.verticalLayout_12.addWidget(self.net_io_table)


        self.verticalLayout_10.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_55 = QLabel(self.frame_10)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font)

        self.verticalLayout_13.addWidget(self.label_55)

        self.net_addresses_table = QTableWidget(self.frame_10)
        if (self.net_addresses_table.columnCount() < 6):
            self.net_addresses_table.setColumnCount(6)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFont(font1);
        self.net_addresses_table.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFont(font1);
        self.net_addresses_table.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFont(font1);
        self.net_addresses_table.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setFont(font1);
        self.net_addresses_table.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setFont(font1);
        self.net_addresses_table.setHorizontalHeaderItem(4, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setFont(font1);
        self.net_addresses_table.setHorizontalHeaderItem(5, __qtablewidgetitem36)
        self.net_addresses_table.setObjectName(u"net_addresses_table")
        self.net_addresses_table.setMinimumSize(QSize(0, 150))

        self.verticalLayout_13.addWidget(self.net_addresses_table)


        self.verticalLayout_10.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.scrollAreaWidgetContents)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_11)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_56 = QLabel(self.frame_11)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font)

        self.verticalLayout_14.addWidget(self.label_56)

        self.net_connections_table = QTableWidget(self.frame_11)
        if (self.net_connections_table.columnCount() < 7):
            self.net_connections_table.setColumnCount(7)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setFont(font1);
        self.net_connections_table.setHorizontalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setFont(font1);
        self.net_connections_table.setHorizontalHeaderItem(1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFont(font1);
        self.net_connections_table.setHorizontalHeaderItem(2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setFont(font1);
        self.net_connections_table.setHorizontalHeaderItem(3, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setFont(font1);
        self.net_connections_table.setHorizontalHeaderItem(4, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setFont(font1);
        self.net_connections_table.setHorizontalHeaderItem(5, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(6, __qtablewidgetitem43)
        self.net_connections_table.setObjectName(u"net_connections_table")
        self.net_connections_table.setMinimumSize(QSize(0, 150))

        self.verticalLayout_14.addWidget(self.net_connections_table)


        self.verticalLayout_10.addWidget(self.frame_11)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_9.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.networks)
        self.system_information = QWidget()
        self.system_information.setObjectName(u"system_information")
        self.verticalLayout_5 = QVBoxLayout(self.system_information)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_3 = QFrame(self.system_information)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(15)
        self.label_39 = QLabel(self.frame_3)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font3)

        self.gridLayout_5.addWidget(self.label_39, 3, 0, 1, 1)

        self.label_46 = QLabel(self.frame_3)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font3)

        self.gridLayout_5.addWidget(self.label_46, 4, 2, 1, 1)

        self.system_machine = QLabel(self.frame_3)
        self.system_machine.setObjectName(u"system_machine")
        self.system_machine.setFont(font1)

        self.gridLayout_5.addWidget(self.system_machine, 3, 3, 1, 1)

        self.label_36 = QLabel(self.frame_3)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font)

        self.gridLayout_5.addWidget(self.label_36, 0, 0, 1, 1)

        self.label_40 = QLabel(self.frame_3)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font3)

        self.gridLayout_5.addWidget(self.label_40, 4, 0, 1, 1)

        self.system_system = QLabel(self.frame_3)
        self.system_system.setObjectName(u"system_system")
        self.system_system.setFont(font3)

        self.gridLayout_5.addWidget(self.system_system, 1, 0, 1, 1)

        self.system_platform = QLabel(self.frame_3)
        self.system_platform.setObjectName(u"system_platform")
        self.system_platform.setFont(font1)

        self.gridLayout_5.addWidget(self.system_platform, 2, 1, 1, 1)

        self.system_processor = QLabel(self.frame_3)
        self.system_processor.setObjectName(u"system_processor")
        self.system_processor.setFont(font1)

        self.gridLayout_5.addWidget(self.system_processor, 2, 3, 1, 1)

        self.label_45 = QLabel(self.frame_3)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font3)

        self.gridLayout_5.addWidget(self.label_45, 3, 2, 1, 1)

        self.label_38 = QLabel(self.frame_3)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font3)

        self.gridLayout_5.addWidget(self.label_38, 2, 0, 1, 1)

        self.system_date = QLabel(self.frame_3)
        self.system_date.setObjectName(u"system_date")
        self.system_date.setFont(font1)

        self.gridLayout_5.addWidget(self.system_date, 4, 1, 1, 1)

        self.system_version = QLabel(self.frame_3)
        self.system_version.setObjectName(u"system_version")
        self.system_version.setFont(font1)

        self.gridLayout_5.addWidget(self.system_version, 3, 1, 1, 1)

        self.system_time = QLabel(self.frame_3)
        self.system_time.setObjectName(u"system_time")
        self.system_time.setFont(font1)

        self.gridLayout_5.addWidget(self.system_time, 4, 3, 1, 1)

        self.label_44 = QLabel(self.frame_3)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font3)

        self.gridLayout_5.addWidget(self.label_44, 2, 2, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.system_information)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.main_body_contents)


        self.verticalLayout.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.footer_left_frame = QFrame(self.footer_frame)
        self.footer_left_frame.setObjectName(u"footer_left_frame")
        self.footer_left_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_left_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.footer_left_frame)
        self.label_3.setObjectName(u"label_3")
        font6 = QFont()
        font6.setPointSize(12)
        self.label_3.setFont(font6)

        self.horizontalLayout_6.addWidget(self.label_3)


        self.horizontalLayout_5.addWidget(self.footer_left_frame, 0, Qt.AlignLeft)

        self.footer_right_frame = QFrame(self.footer_frame)
        self.footer_right_frame.setObjectName(u"footer_right_frame")
        self.footer_right_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.footer_right_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_2 = QPushButton(self.footer_right_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font6)
        self.pushButton_2.setStyleSheet(u"color:rgb(255, 255, 255)")

        self.horizontalLayout_7.addWidget(self.pushButton_2, 0, Qt.AlignRight)


        self.horizontalLayout_5.addWidget(self.footer_right_frame)

        self.size_grip = QFrame(self.footer_frame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.size_grip, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open_close_side_bar_btn.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">PSUTIL MANAGER</span></p></body></html>", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Activity</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Storage</span></p></body></html>", None))
        self.storage_page_btn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">CPU</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Battery</span></p></body></html>", None))
        self.system_page_btn.setText("")
        self.network_page_btn.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Network</span></p></body></html>", None))
        self.cpu_page_btn.setText("")
        self.activity_page_btn.setText("")
        self.battery_page_btn.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">System Information</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">CPU Count</span></p></body></html>", None))
        self.cpu_count.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">N/A</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">CPU Per</span></p></body></html>", None))
        self.cpu_per.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">N/A</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">CPU Main Core</span></p></body></html>", None))
        self.cpu_main_core.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">N/A</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Total RAM</span></p></body></html>", None))
        self.total_ram.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">N/A</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Available RAM</span></p></body></html>", None))
        self.availabel_ram.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">N/A</span></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Used RAM</span></p></body></html>", None))
        self.used_ram.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">N/A</span></p></body></html>", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Free RAM</span></p></body></html>", None))
        self.free_ram.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">N/A</span></p></body></html>", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">RAM Usage</span></p></body></html>", None))
        self.ram_usage.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">N/A</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Battery Information</span></p></body></html>", None))
        self.battery_charge.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">N/A</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Status</span></p></body></html>", None))
        self.battery_plugged.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">N/A</span></p></body></html>", None))
        self.battery_status.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">N/A</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Charge</span></p></body></html>", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Plugged In</span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Time Left</span></p></body></html>", None))
        self.battery_time_left.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">N/A</span></p></body></html>", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Activities</span></p></body></html>", None))
        self.activity_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Process", None))
        self.pushButton_3.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Process ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Process Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Process Status", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Started", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Suspend", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Resume", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Terminate", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Kill", None));
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Suspend", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Resume", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Terminate", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Kill", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Disk Partitions</span></p></body></html>", None))
        ___qtablewidgetitem8 = self.storageTable.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Device", None));
        ___qtablewidgetitem9 = self.storageTable.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Mount Point", None));
        ___qtablewidgetitem10 = self.storageTable.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"OPTS", None));
        ___qtablewidgetitem11 = self.storageTable.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Max File", None));
        ___qtablewidgetitem12 = self.storageTable.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Max Path", None));
        ___qtablewidgetitem13 = self.storageTable.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Total Storage", None));
        ___qtablewidgetitem14 = self.storageTable.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Used Storage", None));
        ___qtablewidgetitem15 = self.storageTable.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Free Storage", None));
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Stats</span></p></body></html>", None))
        ___qtablewidgetitem16 = self.net_stats_table.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"ISUP", None));
        ___qtablewidgetitem17 = self.net_stats_table.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Duplex", None));
        ___qtablewidgetitem18 = self.net_stats_table.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Speed", None));
        ___qtablewidgetitem19 = self.net_stats_table.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"MTU", None));
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Network IO Counters</span></p></body></html>", None))
        ___qtablewidgetitem20 = self.net_io_table.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"IO", None));
        ___qtablewidgetitem21 = self.net_io_table.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Bytes Sent", None));
        ___qtablewidgetitem22 = self.net_io_table.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Bytes Received", None));
        ___qtablewidgetitem23 = self.net_io_table.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Packets Sent", None));
        ___qtablewidgetitem24 = self.net_io_table.horizontalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Packets Received", None));
        ___qtablewidgetitem25 = self.net_io_table.horizontalHeaderItem(5)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Err In", None));
        ___qtablewidgetitem26 = self.net_io_table.horizontalHeaderItem(6)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Err Out", None));
        ___qtablewidgetitem27 = self.net_io_table.horizontalHeaderItem(7)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Drop In", None));
        ___qtablewidgetitem28 = self.net_io_table.horizontalHeaderItem(8)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Drop Out", None));
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Network Addresses</span></p></body></html>", None))
        ___qtablewidgetitem29 = self.net_addresses_table.horizontalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Family", None));
        ___qtablewidgetitem30 = self.net_addresses_table.horizontalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem31 = self.net_addresses_table.horizontalHeaderItem(3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Netmask", None));
        ___qtablewidgetitem32 = self.net_addresses_table.horizontalHeaderItem(4)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Broadcast", None));
        ___qtablewidgetitem33 = self.net_addresses_table.horizontalHeaderItem(5)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"PTP", None));
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Network Connections</span></p></body></html>", None))
        ___qtablewidgetitem34 = self.net_connections_table.horizontalHeaderItem(0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"FD", None));
        ___qtablewidgetitem35 = self.net_connections_table.horizontalHeaderItem(1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Family", None));
        ___qtablewidgetitem36 = self.net_connections_table.horizontalHeaderItem(2)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Family", None));
        ___qtablewidgetitem37 = self.net_connections_table.horizontalHeaderItem(3)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"LADDR", None));
        ___qtablewidgetitem38 = self.net_connections_table.horizontalHeaderItem(4)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"RADDR", None));
        ___qtablewidgetitem39 = self.net_connections_table.horizontalHeaderItem(5)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem40 = self.net_connections_table.horizontalHeaderItem(6)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"PID", None));
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Version</span></p></body></html>", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">System Time</span></p></body></html>", None))
        self.system_machine.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">N/A</span></p></body></html>", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">System Information</span></p></body></html>", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">System Date</span></p></body></html>", None))
        self.system_system.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">N/A</span></p></body></html>", None))
        self.system_platform.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">N/A</span></p></body></html>", None))
        self.system_processor.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">N/A</span></p></body></html>", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Machine</span></p></body></html>", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Platform</span></p></body></html>", None))
        self.system_date.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">N/A</span></p></body></html>", None))
        self.system_version.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">N/A</span></p></body></html>", None))
        self.system_time.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">N/A</span></p></body></html>", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Processor</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Version 1.0.0.0 | CopyRight</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

