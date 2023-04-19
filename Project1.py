# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Project1FvVsBs.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGraphicsView,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1072, 683)
        MainWindow.setStyleSheet(u"*{\n"
"	border:none;\n"
"	background-color: transparent;\n"
"	background: none;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #000000;\n"
"\n"
"}\n"
"#centralwidget{\n"
"	background-color: #023047;\n"
"}\n"
"#leftMenuSubcontainer{\n"
"	background-color: #FFBC42;\n"
"	border-radius: 10px;\n"
"}\n"
"#leftMenuSubcontainer QPushButton{\n"
"	background-color: #8ecae6;\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	margin-top: 10px\n"
"}\n"
"#centerLeftMenuSubcontainer{\n"
"	background-color: #219ebc;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"#contents{\n"
"	background-color: #219ebc;\n"
"}\n"
"#settingsPage{\n"
"	background-color: #219ebc;\n"
"}\n"
"#infoPage{\n"
"	background-color: #219ebc;\n"
"}\n"
"#helpPage{\n"
"	background-color: #219ebc;\n"
"}\n"
"#avoidedCO2Widget{\n"
"	background-color: #8ecae6;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"#moneySaved"
                        "Widget{\n"
"	background-color: #8ecae6;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"#totalProduced{\n"
"	background-color: #8ecae6;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"#predictedProductionWidget{\n"
"	background-color: #8ecae6;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"#predictedSavingsWidget{\n"
"	background-color: #8ecae6;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"#statGraphSettingsWidet{\n"
"	background-color: #8ecae6;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"#graphWidgetName{\n"
"	background-color: #8ecae6;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"#graphWidgetName_2{\n"
"	background-color: #8ecae6;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"#angleWidget{\n"
"	background-color: #FFBC42;\n"
"	border-top-left-radius"
                        ": 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"#capacityWidget{\n"
"	background-color: #FFBC42;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"#installedDateWidget{\n"
"	background-color: #FFBC42;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"#helpLabelsWidget{\n"
"	background-color: #FFBC42;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, -1, -1, -1)
        self.leftMenuSubcontainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubcontainer.setObjectName(u"leftMenuSubcontainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubcontainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.leftMenuSubcontainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menuButton = QPushButton(self.frame)
        self.menuButton.setObjectName(u"menuButton")
        self.menuButton.setMinimumSize(QSize(0, 60))
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.menuButton)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubcontainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.statsButton = QPushButton(self.frame_2)
        self.statsButton.setObjectName(u"statsButton")
        self.statsButton.setMinimumSize(QSize(0, 60))
        self.statsButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.statsButton.setIcon(icon1)
        self.statsButton.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.statsButton)

        self.predButton = QPushButton(self.frame_2)
        self.predButton.setObjectName(u"predButton")
        self.predButton.setMinimumSize(QSize(0, 60))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/data.png", QSize(), QIcon.Normal, QIcon.Off)
        self.predButton.setIcon(icon2)
        self.predButton.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.predButton)

        self.homeButton = QPushButton(self.frame_2)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setMinimumSize(QSize(0, 60))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/prediction.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon3)
        self.homeButton.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.homeButton)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubcontainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 10)
        self.settingButton = QPushButton(self.frame_3)
        self.settingButton.setObjectName(u"settingButton")
        self.settingButton.setMinimumSize(QSize(0, 60))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingButton.setIcon(icon4)
        self.settingButton.setIconSize(QSize(32, 32))

        self.verticalLayout_5.addWidget(self.settingButton)

        self.infoButton = QPushButton(self.frame_3)
        self.infoButton.setObjectName(u"infoButton")
        self.infoButton.setMinimumSize(QSize(0, 60))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/information.png", QSize(), QIcon.Normal, QIcon.Off)
        self.infoButton.setIcon(icon5)
        self.infoButton.setIconSize(QSize(32, 32))

        self.verticalLayout_5.addWidget(self.infoButton)

        self.helpButton = QPushButton(self.frame_3)
        self.helpButton.setObjectName(u"helpButton")
        self.helpButton.setMinimumSize(QSize(0, 60))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/question.png", QSize(), QIcon.Normal, QIcon.Off)
        self.helpButton.setIcon(icon6)
        self.helpButton.setIconSize(QSize(32, 32))

        self.verticalLayout_5.addWidget(self.helpButton)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubcontainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.leftMenuContainer)

        self.centerMenuContainer = QWidget(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.horizontalLayout_3 = QHBoxLayout(self.centerMenuContainer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.centerLeftMenuSubcontainer = QWidget(self.centerMenuContainer)
        self.centerLeftMenuSubcontainer.setObjectName(u"centerLeftMenuSubcontainer")
        self.centerLeftMenuSubcontainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_8 = QVBoxLayout(self.centerLeftMenuSubcontainer)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.centerLeftMenuBar = QWidget(self.centerLeftMenuSubcontainer)
        self.centerLeftMenuBar.setObjectName(u"centerLeftMenuBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centerLeftMenuBar.sizePolicy().hasHeightForWidth())
        self.centerLeftMenuBar.setSizePolicy(sizePolicy1)
        self.horizontalLayout_4 = QHBoxLayout(self.centerLeftMenuBar)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menuLabel = QLabel(self.centerLeftMenuBar)
        self.menuLabel.setObjectName(u"menuLabel")

        self.horizontalLayout_4.addWidget(self.menuLabel)

        self.closeButton = QPushButton(self.centerLeftMenuBar)
        self.closeButton.setObjectName(u"closeButton")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon7)
        self.closeButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.closeButton, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.centerLeftMenuBar)

        self.contents = QWidget(self.centerLeftMenuSubcontainer)
        self.contents.setObjectName(u"contents")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.contents.sizePolicy().hasHeightForWidth())
        self.contents.setSizePolicy(sizePolicy2)
        self.contents.setMinimumSize(QSize(0, 0))
        self.leftMenuContents = QStackedWidget(self.contents)
        self.leftMenuContents.setObjectName(u"leftMenuContents")
        self.leftMenuContents.setGeometry(QRect(0, 0, 180, 601))
        sizePolicy.setHeightForWidth(self.leftMenuContents.sizePolicy().hasHeightForWidth())
        self.leftMenuContents.setSizePolicy(sizePolicy)
        self.leftMenuContents.setMinimumSize(QSize(100, 0))
        self.leftMenuContents.setMaximumSize(QSize(180, 16777215))
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.label_2 = QLabel(self.settingsPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 70, 49, 16))
        self.leftMenuContents.addWidget(self.settingsPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.label_3 = QLabel(self.helpPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 540, 49, 16))
        self.helpInnerWidget = QWidget(self.helpPage)
        self.helpInnerWidget.setObjectName(u"helpInnerWidget")
        self.helpInnerWidget.setGeometry(QRect(0, 0, 180, 500))
        self.helpInnerWidget.setMinimumSize(QSize(180, 500))
        self.helpInnerWidget.setMaximumSize(QSize(180, 500))
        self.verticalLayout_20 = QVBoxLayout(self.helpInnerWidget)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.helpLabelsWidget = QWidget(self.helpInnerWidget)
        self.helpLabelsWidget.setObjectName(u"helpLabelsWidget")
        self.helpLabelsWidget.setMinimumSize(QSize(0, 100))
        self.helpLabelsWidget.setMaximumSize(QSize(16777215, 150))
        self.verticalLayout_21 = QVBoxLayout(self.helpLabelsWidget)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_7 = QLabel(self.helpLabelsWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.label_7, 0, Qt.AlignTop)

        self.label_9 = QLabel(self.helpLabelsWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.label_9)


        self.verticalLayout_20.addWidget(self.helpLabelsWidget, 0, Qt.AlignTop)

        self.leftMenuContents.addWidget(self.helpPage)
        self.infoPage = QWidget()
        self.infoPage.setObjectName(u"infoPage")
        self.label = QLabel(self.infoPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 550, 81, 16))
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.infoPanelDataWidget = QWidget(self.infoPage)
        self.infoPanelDataWidget.setObjectName(u"infoPanelDataWidget")
        self.infoPanelDataWidget.setGeometry(QRect(0, 0, 180, 300))
        self.infoPanelDataWidget.setMinimumSize(QSize(180, 300))
        self.infoPanelDataWidget.setMaximumSize(QSize(180, 300))
        self.verticalLayout_16 = QVBoxLayout(self.infoPanelDataWidget)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, -1, -1, -1)
        self.capacityWidget = QWidget(self.infoPanelDataWidget)
        self.capacityWidget.setObjectName(u"capacityWidget")
        self.capacityWidget.setMinimumSize(QSize(170, 50))
        self.capacityWidget.setMaximumSize(QSize(150, 50))
        self.verticalLayout_17 = QVBoxLayout(self.capacityWidget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.capacityLabel = QLabel(self.capacityWidget)
        self.capacityLabel.setObjectName(u"capacityLabel")
        self.capacityLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.capacityLabel)


        self.verticalLayout_16.addWidget(self.capacityWidget, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.angleWidget = QWidget(self.infoPanelDataWidget)
        self.angleWidget.setObjectName(u"angleWidget")
        self.angleWidget.setMinimumSize(QSize(170, 50))
        self.angleWidget.setMaximumSize(QSize(100, 50))
        self.verticalLayout_18 = QVBoxLayout(self.angleWidget)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.angleLabel = QLabel(self.angleWidget)
        self.angleLabel.setObjectName(u"angleLabel")
        self.angleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.angleLabel)


        self.verticalLayout_16.addWidget(self.angleWidget, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.installedDateWidget = QWidget(self.infoPanelDataWidget)
        self.installedDateWidget.setObjectName(u"installedDateWidget")
        self.installedDateWidget.setMinimumSize(QSize(170, 50))
        self.installedDateWidget.setMaximumSize(QSize(150, 50))
        self.verticalLayout_19 = QVBoxLayout(self.installedDateWidget)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.installedDateLavel = QLabel(self.installedDateWidget)
        self.installedDateLavel.setObjectName(u"installedDateLavel")
        self.installedDateLavel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.installedDateLavel)


        self.verticalLayout_16.addWidget(self.installedDateWidget, 0, Qt.AlignHCenter)

        self.leftMenuContents.addWidget(self.infoPage)

        self.verticalLayout_8.addWidget(self.contents)


        self.horizontalLayout_3.addWidget(self.centerLeftMenuSubcontainer, 0, Qt.AlignLeft)

        self.centerMenuSubcontainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubcontainer.setObjectName(u"centerMenuSubcontainer")
        self.verticalLayout_7 = QVBoxLayout(self.centerMenuSubcontainer)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_4 = QFrame(self.centerMenuSubcontainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 330))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_7.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.mainContent = QStackedWidget(self.centerMenuSubcontainer)
        self.mainContent.setObjectName(u"mainContent")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.label_4 = QLabel(self.homePage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(300, 560, 49, 16))
        self.graphWidget = QWidget(self.homePage)
        self.graphWidget.setObjectName(u"graphWidget")
        self.graphWidget.setGeometry(QRect(20, 30, 620, 380))
        self.verticalLayout_11 = QVBoxLayout(self.graphWidget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.graphWidgetName = QWidget(self.graphWidget)
        self.graphWidgetName.setObjectName(u"graphWidgetName")
        self.graphWidgetName.setMinimumSize(QSize(200, 20))
        self.graphWidgetName.setMaximumSize(QSize(150, 30))
        self.horizontalLayout_8 = QHBoxLayout(self.graphWidgetName)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 4, -1, -1)
        self.label_10 = QLabel(self.graphWidgetName)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 20))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_10, 0, Qt.AlignVCenter)


        self.verticalLayout_11.addWidget(self.graphWidgetName, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.graphLabelHome = QLabel(self.graphWidget)
        self.graphLabelHome.setObjectName(u"graphLabelHome")
        self.graphLabelHome.setMinimumSize(QSize(0, 320))
        self.graphLabelHome.setMaximumSize(QSize(16777215, 320))

        self.verticalLayout_11.addWidget(self.graphLabelHome)

        self.dataWidget = QWidget(self.homePage)
        self.dataWidget.setObjectName(u"dataWidget")
        self.dataWidget.setGeometry(QRect(20, 430, 621, 74))
        self.horizontalLayout_9 = QHBoxLayout(self.dataWidget)
        self.horizontalLayout_9.setSpacing(30)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(9, -1, -1, -1)
        self.totalProduced = QWidget(self.dataWidget)
        self.totalProduced.setObjectName(u"totalProduced")
        self.verticalLayout_10 = QVBoxLayout(self.totalProduced)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.totalProducedLabel = QLabel(self.totalProduced)
        self.totalProducedLabel.setObjectName(u"totalProducedLabel")
        self.totalProducedLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.totalProducedLabel)

        self.totalProducedValue = QLabel(self.totalProduced)
        self.totalProducedValue.setObjectName(u"totalProducedValue")
        self.totalProducedValue.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.totalProducedValue)


        self.horizontalLayout_9.addWidget(self.totalProduced)

        self.moneySavedWidget = QWidget(self.dataWidget)
        self.moneySavedWidget.setObjectName(u"moneySavedWidget")
        self.verticalLayout_9 = QVBoxLayout(self.moneySavedWidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.moneySavedTodayLabel = QLabel(self.moneySavedWidget)
        self.moneySavedTodayLabel.setObjectName(u"moneySavedTodayLabel")
        self.moneySavedTodayLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.moneySavedTodayLabel)

        self.moneySavedValue = QLabel(self.moneySavedWidget)
        self.moneySavedValue.setObjectName(u"moneySavedValue")
        self.moneySavedValue.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.moneySavedValue)


        self.horizontalLayout_9.addWidget(self.moneySavedWidget)

        self.avoidedCO2Widget = QWidget(self.dataWidget)
        self.avoidedCO2Widget.setObjectName(u"avoidedCO2Widget")
        self.verticalLayout_6 = QVBoxLayout(self.avoidedCO2Widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.avoidedCO2Label = QLabel(self.avoidedCO2Widget)
        self.avoidedCO2Label.setObjectName(u"avoidedCO2Label")
        self.avoidedCO2Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.avoidedCO2Label)

        self.avoidedCO2Value = QLabel(self.avoidedCO2Widget)
        self.avoidedCO2Value.setObjectName(u"avoidedCO2Value")
        self.avoidedCO2Value.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.avoidedCO2Value)


        self.horizontalLayout_9.addWidget(self.avoidedCO2Widget)

        self.mainContent.addWidget(self.homePage)
        self.statisticsPage = QWidget()
        self.statisticsPage.setObjectName(u"statisticsPage")
        self.label_5 = QLabel(self.statisticsPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(280, 580, 121, 31))
        self.statGraphWidget = QWidget(self.statisticsPage)
        self.statGraphWidget.setObjectName(u"statGraphWidget")
        self.statGraphWidget.setGeometry(QRect(20, 30, 620, 380))
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.statGraphWidget.sizePolicy().hasHeightForWidth())
        self.statGraphWidget.setSizePolicy(sizePolicy3)
        self.verticalLayout_12 = QVBoxLayout(self.statGraphWidget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.statGraphSettingsWidet = QWidget(self.statGraphWidget)
        self.statGraphSettingsWidet.setObjectName(u"statGraphSettingsWidet")
        self.statGraphSettingsWidet.setMinimumSize(QSize(280, 30))
        self.statGraphSettingsWidet.setMaximumSize(QSize(400, 20))
        self.horizontalLayout_5 = QHBoxLayout(self.statGraphSettingsWidet)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.statGraphSettingsWidet)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        self.label_8.setMaximumSize(QSize(120, 16777215))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_8, 0, Qt.AlignTop)

        self.comboBox = QComboBox(self.statGraphSettingsWidet)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy5)
        self.comboBox.setMinimumSize(QSize(170, 0))
        self.comboBox.setMaximumSize(QSize(170, 16777215))

        self.horizontalLayout_5.addWidget(self.comboBox, 0, Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.statGraphSettingsWidet, 0, Qt.AlignRight|Qt.AlignTop)

        self.stackedWidetStats = QStackedWidget(self.statGraphWidget)
        self.stackedWidetStats.setObjectName(u"stackedWidetStats")
        self.lastDayPage = QWidget()
        self.lastDayPage.setObjectName(u"lastDayPage")
        self.lastDayGraph = QLabel(self.lastDayPage)
        self.lastDayGraph.setObjectName(u"lastDayGraph")
        self.lastDayGraph.setGeometry(QRect(0, 0, 602, 326))
        self.stackedWidetStats.addWidget(self.lastDayPage)
        self.lastMonthPage = QWidget()
        self.lastMonthPage.setObjectName(u"lastMonthPage")
        self.lastMonthGraph = QLabel(self.lastMonthPage)
        self.lastMonthGraph.setObjectName(u"lastMonthGraph")
        self.lastMonthGraph.setGeometry(QRect(0, 0, 602, 326))
        self.stackedWidetStats.addWidget(self.lastMonthPage)
        self.thisMonthPage = QWidget()
        self.thisMonthPage.setObjectName(u"thisMonthPage")
        self.thisMonthGraph = QLabel(self.thisMonthPage)
        self.thisMonthGraph.setObjectName(u"thisMonthGraph")
        self.thisMonthGraph.setGeometry(QRect(0, 0, 602, 326))
        self.stackedWidetStats.addWidget(self.thisMonthPage)

        self.verticalLayout_12.addWidget(self.stackedWidetStats)

        self.mainContent.addWidget(self.statisticsPage)
        self.predictionsPage = QWidget()
        self.predictionsPage.setObjectName(u"predictionsPage")
        self.label_6 = QLabel(self.predictionsPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(270, 550, 101, 41))
        self.graphWidget_2 = QWidget(self.predictionsPage)
        self.graphWidget_2.setObjectName(u"graphWidget_2")
        self.graphWidget_2.setEnabled(True)
        self.graphWidget_2.setGeometry(QRect(20, 30, 620, 380))
        self.verticalLayout_13 = QVBoxLayout(self.graphWidget_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.graphWidgetName_2 = QWidget(self.graphWidget_2)
        self.graphWidgetName_2.setObjectName(u"graphWidgetName_2")
        self.graphWidgetName_2.setMinimumSize(QSize(220, 20))
        self.graphWidgetName_2.setMaximumSize(QSize(200, 30))
        self.horizontalLayout_10 = QHBoxLayout(self.graphWidgetName_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.predictedGraphName = QLabel(self.graphWidgetName_2)
        self.predictedGraphName.setObjectName(u"predictedGraphName")
        self.predictedGraphName.setMinimumSize(QSize(200, 0))
        self.predictedGraphName.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.predictedGraphName, 0, Qt.AlignHCenter)


        self.verticalLayout_13.addWidget(self.graphWidgetName_2, 0, Qt.AlignHCenter)

        self.graphicsView_3 = QGraphicsView(self.graphWidget_2)
        self.graphicsView_3.setObjectName(u"graphicsView_3")
        self.graphicsView_3.setMinimumSize(QSize(0, 100))

        self.verticalLayout_13.addWidget(self.graphicsView_3)

        self.predictionsDataWidget = QWidget(self.predictionsPage)
        self.predictionsDataWidget.setObjectName(u"predictionsDataWidget")
        self.predictionsDataWidget.setGeometry(QRect(20, 430, 620, 74))
        self.predictionsDataWidget.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_7 = QHBoxLayout(self.predictionsDataWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.predictedProductionWidget = QWidget(self.predictionsDataWidget)
        self.predictedProductionWidget.setObjectName(u"predictedProductionWidget")
        self.predictedProductionWidget.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_14 = QVBoxLayout(self.predictedProductionWidget)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.predictedProductionLabel = QLabel(self.predictedProductionWidget)
        self.predictedProductionLabel.setObjectName(u"predictedProductionLabel")

        self.verticalLayout_14.addWidget(self.predictedProductionLabel, 0, Qt.AlignHCenter)

        self.predictedProductionValue = QLabel(self.predictedProductionWidget)
        self.predictedProductionValue.setObjectName(u"predictedProductionValue")

        self.verticalLayout_14.addWidget(self.predictedProductionValue, 0, Qt.AlignHCenter)


        self.horizontalLayout_7.addWidget(self.predictedProductionWidget)

        self.predictedSavingsWidget = QWidget(self.predictionsDataWidget)
        self.predictedSavingsWidget.setObjectName(u"predictedSavingsWidget")
        self.predictedSavingsWidget.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_15 = QVBoxLayout(self.predictedSavingsWidget)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.predictedSavingsLabel = QLabel(self.predictedSavingsWidget)
        self.predictedSavingsLabel.setObjectName(u"predictedSavingsLabel")

        self.verticalLayout_15.addWidget(self.predictedSavingsLabel, 0, Qt.AlignHCenter)

        self.predictedSavingsValue = QLabel(self.predictedSavingsWidget)
        self.predictedSavingsValue.setObjectName(u"predictedSavingsValue")

        self.verticalLayout_15.addWidget(self.predictedSavingsValue, 0, Qt.AlignHCenter)


        self.horizontalLayout_7.addWidget(self.predictedSavingsWidget)

        self.mainContent.addWidget(self.predictionsPage)

        self.verticalLayout_7.addWidget(self.mainContent)


        self.horizontalLayout_3.addWidget(self.centerMenuSubcontainer)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainContent.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuButton.setToolTip(QCoreApplication.translate("MainWindow", u"Meny", None))
#endif // QT_CONFIG(tooltip)
        self.menuButton.setText("")
#if QT_CONFIG(tooltip)
        self.statsButton.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.statsButton.setText(QCoreApplication.translate("MainWindow", u"   Home", None))
#if QT_CONFIG(tooltip)
        self.predButton.setToolTip(QCoreApplication.translate("MainWindow", u"Statistics", None))
#endif // QT_CONFIG(tooltip)
        self.predButton.setText(QCoreApplication.translate("MainWindow", u"    Statistics", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Predictions", None))
#if QT_CONFIG(tooltip)
        self.settingButton.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingButton.setText(QCoreApplication.translate("MainWindow", u"    Settings", None))
#if QT_CONFIG(tooltip)
        self.infoButton.setToolTip(QCoreApplication.translate("MainWindow", u"Information", None))
#endif // QT_CONFIG(tooltip)
        self.infoButton.setText(QCoreApplication.translate("MainWindow", u"    Information", None))
#if QT_CONFIG(tooltip)
        self.helpButton.setToolTip(QCoreApplication.translate("MainWindow", u"Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpButton.setText(QCoreApplication.translate("MainWindow", u"    Help", None))
        self.menuLabel.setText(QCoreApplication.translate("MainWindow", u"More Menu", None))
        self.closeButton.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"App made by: Micha\u0142 Tajak and Dominik Dziechciarz for JPWP", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"For additional help please contant: veryrealemail@gmail.com", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.capacityLabel.setText(QCoreApplication.translate("MainWindow", u"Capacity: 400kWh", None))
        self.angleLabel.setText(QCoreApplication.translate("MainWindow", u"Angle of Inclination:  30   ", None))
        self.installedDateLavel.setText(QCoreApplication.translate("MainWindow", u"Date of Installation: 20.02.202", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Today's production", None))
        self.graphLabelHome.setText("")
        self.totalProducedLabel.setText(QCoreApplication.translate("MainWindow", u"Total Produced Energy Today", None))
        self.totalProducedValue.setText(QCoreApplication.translate("MainWindow", u"10kWh", None))
        self.moneySavedTodayLabel.setText(QCoreApplication.translate("MainWindow", u"Money saved today", None))
        self.moneySavedValue.setText(QCoreApplication.translate("MainWindow", u"50 PLN", None))
        self.avoidedCO2Label.setText(QCoreApplication.translate("MainWindow", u"CO2 Avoided Today", None))
        self.avoidedCO2Value.setText(QCoreApplication.translate("MainWindow", u"200kg", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"statistics", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Choose Range:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Last Day", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"This Month", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Last Month", None))

        self.lastDayGraph.setText("")
        self.lastMonthGraph.setText("")
        self.thisMonthGraph.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Predictions", None))
        self.predictedGraphName.setText(QCoreApplication.translate("MainWindow", u"Predicted production for next week", None))
        self.predictedProductionLabel.setText(QCoreApplication.translate("MainWindow", u"Predicted Production:", None))
        self.predictedProductionValue.setText(QCoreApplication.translate("MainWindow", u"10 kWh", None))
        self.predictedSavingsLabel.setText(QCoreApplication.translate("MainWindow", u"Predicted Savings:", None))
        self.predictedSavingsValue.setText(QCoreApplication.translate("MainWindow", u"10 PLN", None))
    # retranslateUi

