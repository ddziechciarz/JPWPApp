# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Project1ceEVrj.ui'
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
"")
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
        self.label_3.setGeometry(QRect(70, 110, 49, 16))
        self.leftMenuContents.addWidget(self.helpPage)
        self.infoPage = QWidget()
        self.infoPage.setObjectName(u"infoPage")
        self.label = QLabel(self.infoPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 90, 81, 16))
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
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
        self.graphWidget.setGeometry(QRect(20, 30, 621, 391))
        self.verticalLayout_11 = QVBoxLayout(self.graphWidget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_7 = QLabel(self.graphWidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_11.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.graphicsView = QGraphicsView(self.graphWidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_11.addWidget(self.graphicsView)

        self.totalProduced = QWidget(self.homePage)
        self.totalProduced.setObjectName(u"totalProduced")
        self.totalProduced.setGeometry(QRect(20, 440, 170, 56))
        self.verticalLayout_10 = QVBoxLayout(self.totalProduced)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.totalProducedLabel = QLabel(self.totalProduced)
        self.totalProducedLabel.setObjectName(u"totalProducedLabel")

        self.verticalLayout_10.addWidget(self.totalProducedLabel)

        self.totalProducedValue = QLabel(self.totalProduced)
        self.totalProducedValue.setObjectName(u"totalProducedValue")

        self.verticalLayout_10.addWidget(self.totalProducedValue)

        self.moneySavedWidget = QWidget(self.homePage)
        self.moneySavedWidget.setObjectName(u"moneySavedWidget")
        self.moneySavedWidget.setGeometry(QRect(240, 440, 121, 56))
        self.verticalLayout_9 = QVBoxLayout(self.moneySavedWidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.moneySavedValue = QLabel(self.moneySavedWidget)
        self.moneySavedValue.setObjectName(u"moneySavedValue")

        self.verticalLayout_9.addWidget(self.moneySavedValue)

        self.label_9 = QLabel(self.moneySavedWidget)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_9.addWidget(self.label_9)

        self.avoidedCO2Widget = QWidget(self.homePage)
        self.avoidedCO2Widget.setObjectName(u"avoidedCO2Widget")
        self.avoidedCO2Widget.setGeometry(QRect(460, 440, 122, 56))
        self.verticalLayout_6 = QVBoxLayout(self.avoidedCO2Widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.avoidedCO2Label = QLabel(self.avoidedCO2Widget)
        self.avoidedCO2Label.setObjectName(u"avoidedCO2Label")

        self.verticalLayout_6.addWidget(self.avoidedCO2Label)

        self.avoidedCO2Value = QLabel(self.avoidedCO2Widget)
        self.avoidedCO2Value.setObjectName(u"avoidedCO2Value")

        self.verticalLayout_6.addWidget(self.avoidedCO2Value)

        self.mainContent.addWidget(self.homePage)
        self.statisticsPage = QWidget()
        self.statisticsPage.setObjectName(u"statisticsPage")
        self.label_5 = QLabel(self.statisticsPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(280, 580, 121, 31))
        self.statGraphWidget = QWidget(self.statisticsPage)
        self.statGraphWidget.setObjectName(u"statGraphWidget")
        self.statGraphWidget.setGeometry(QRect(50, 70, 561, 361))
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.statGraphWidget.sizePolicy().hasHeightForWidth())
        self.statGraphWidget.setSizePolicy(sizePolicy3)
        self.verticalLayout_12 = QVBoxLayout(self.statGraphWidget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.statGraphSettingsWidet = QWidget(self.statGraphWidget)
        self.statGraphSettingsWidet.setObjectName(u"statGraphSettingsWidet")
        self.statGraphSettingsWidet.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_5 = QHBoxLayout(self.statGraphSettingsWidet)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.statGraphSettingsWidet)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)

        self.horizontalLayout_5.addWidget(self.label_8)

        self.comboBox = QComboBox(self.statGraphSettingsWidet)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_5.addWidget(self.comboBox)


        self.verticalLayout_12.addWidget(self.statGraphSettingsWidet)

        self.graphicsView_2 = QGraphicsView(self.statGraphWidget)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.verticalLayout_12.addWidget(self.graphicsView_2)

        self.mainContent.addWidget(self.statisticsPage)
        self.predictionsPage = QWidget()
        self.predictionsPage.setObjectName(u"predictionsPage")
        self.label_6 = QLabel(self.predictionsPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(270, 550, 101, 41))
        self.predictionsWidget = QWidget(self.predictionsPage)
        self.predictionsWidget.setObjectName(u"predictionsWidget")
        self.predictionsWidget.setGeometry(QRect(40, 40, 601, 511))
        self.verticalLayout_13 = QVBoxLayout(self.predictionsWidget)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.predictionsGraphWidget = QWidget(self.predictionsWidget)
        self.predictionsGraphWidget.setObjectName(u"predictionsGraphWidget")
        sizePolicy2.setHeightForWidth(self.predictionsGraphWidget.sizePolicy().hasHeightForWidth())
        self.predictionsGraphWidget.setSizePolicy(sizePolicy2)
        self.horizontalLayout_6 = QHBoxLayout(self.predictionsGraphWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.graphicsView_3 = QGraphicsView(self.predictionsGraphWidget)
        self.graphicsView_3.setObjectName(u"graphicsView_3")

        self.horizontalLayout_6.addWidget(self.graphicsView_3)


        self.verticalLayout_13.addWidget(self.predictionsGraphWidget)

        self.predictionsDataWidget = QWidget(self.predictionsWidget)
        self.predictionsDataWidget.setObjectName(u"predictionsDataWidget")
        self.predictionsDataWidget.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_7 = QHBoxLayout(self.predictionsDataWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.predictedProductionWidget = QWidget(self.predictionsDataWidget)
        self.predictedProductionWidget.setObjectName(u"predictedProductionWidget")
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
        self.verticalLayout_15 = QVBoxLayout(self.predictedSavingsWidget)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.predictedSavingsLabel = QLabel(self.predictedSavingsWidget)
        self.predictedSavingsLabel.setObjectName(u"predictedSavingsLabel")

        self.verticalLayout_15.addWidget(self.predictedSavingsLabel, 0, Qt.AlignHCenter)

        self.predictedSavingsValue = QLabel(self.predictedSavingsWidget)
        self.predictedSavingsValue.setObjectName(u"predictedSavingsValue")

        self.verticalLayout_15.addWidget(self.predictedSavingsValue, 0, Qt.AlignHCenter)


        self.horizontalLayout_7.addWidget(self.predictedSavingsWidget)


        self.verticalLayout_13.addWidget(self.predictionsDataWidget, 0, Qt.AlignBottom)

        self.mainContent.addWidget(self.predictionsPage)

        self.verticalLayout_7.addWidget(self.mainContent)


        self.horizontalLayout_3.addWidget(self.centerMenuSubcontainer)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainContent.setCurrentIndex(2)


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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Production in last 24 hours", None))
        self.totalProducedLabel.setText(QCoreApplication.translate("MainWindow", u"Total Produced Energy Today", None))
        self.totalProducedValue.setText(QCoreApplication.translate("MainWindow", u"10kWh", None))
        self.moneySavedValue.setText(QCoreApplication.translate("MainWindow", u"Money saved today", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"50 PLN", None))
        self.avoidedCO2Label.setText(QCoreApplication.translate("MainWindow", u"CO2 Avoided Today", None))
        self.avoidedCO2Value.setText(QCoreApplication.translate("MainWindow", u"200kg", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"statistics", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Choose Range", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Last Day", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Last Month", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Last Year", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Lifetime", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Predictions", None))
        self.predictedProductionLabel.setText(QCoreApplication.translate("MainWindow", u"Predicted Production:", None))
        self.predictedProductionValue.setText(QCoreApplication.translate("MainWindow", u"10 kWh", None))
        self.predictedSavingsLabel.setText(QCoreApplication.translate("MainWindow", u"Predicted Savings:", None))
        self.predictedSavingsValue.setText(QCoreApplication.translate("MainWindow", u"10 PLN", None))
    # retranslateUi

