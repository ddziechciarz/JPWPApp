import os
import sys
from pip._internal.operations.freeze import freeze

from Project1 import *
import charts_read

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.ui.settingButton.clicked.connect(lambda: self.smallButtonClicked(0))
        self.ui.infoButton.clicked.connect(lambda: self.smallButtonClicked(2))
        self.ui.helpButton.clicked.connect(lambda: self.smallButtonClicked(1))

        self.ui.homeButton.clicked.connect(lambda: self.ui.mainContent.setCurrentIndex(2))
        self.ui.statsButton.clicked.connect(lambda: self.statWindowClicked())
        self.ui.predButton.clicked.connect(lambda: self.ui.mainContent.setCurrentIndex(1))

        self.ui.menuButton.clicked.connect(lambda: self.ui.centerLeftMenuSubcontainer.setHidden(not self.ui.centerLeftMenuSubcontainer.isHidden()))

        self.ui.comboBox.activated.connect(lambda: self.comboBoxClicked())

        pixmapHome = QPixmap('img/charts_today.jpg')
        pixmapStatToday = QPixmap('img/charts_today.jpg')
        pixmapStatLastMonth = QPixmap('img/charts_month_last.jpg')
        pixmapStatThisMonth = QPixmap('img/charts_month_today.jpg')
        pixmapPrediction = QPixmap('img/energy_prediction.jpg')

        self.ui.graphLabelHome.setPixmap(pixmapHome)
        self.ui.graphLabelHome.setScaledContents(True)

        self.ui.lastDayGraph.setPixmap(pixmapStatToday)
        self.ui.lastDayGraph.setScaledContents(True)

        self.ui.lastMonthGraph.setPixmap(pixmapStatLastMonth)
        self.ui.lastMonthGraph.setScaledContents(True)

        self.ui.thisMonthGraph.setPixmap(pixmapStatThisMonth)
        self.ui.thisMonthGraph.setScaledContents(True)

        self.ui.predictedGraph.setPixmap(pixmapPrediction)
        self.ui.predictedGraph.setScaledContents(True)




    def comboBoxClicked(self):
        currentSelection = self.ui.comboBox.currentText()
        if currentSelection == 'Last Day':
            self.ui.stackedWidetStats.setCurrentIndex(0)
        elif currentSelection == 'This Month':
            self.ui.stackedWidetStats.setCurrentIndex(2)
        else:
            self.ui.stackedWidetStats.setCurrentIndex(1)


    def smallButtonClicked(self, index):
        if self.ui.leftMenuContents.currentIndex() == index:
            self.ui.centerLeftMenuSubcontainer.setHidden(not self.ui.centerLeftMenuSubcontainer.isHidden())
        else:
            self.ui.centerLeftMenuSubcontainer.setHidden(False)
        self.ui.leftMenuContents.setCurrentIndex(index)

    def homeWindowClicked(self):
        self.ui.mainContent.setCurrentIndex(2)
        self.ui.homeGraph.plotItem

    def statWindowClicked(self):
        self.ui.mainContent.setCurrentIndex(0)
        #self.ui.homeGraph





if __name__ == "__main__":
    #todayCharts = charts.charts_today()
    for requirement in freeze(local_only=True):
        print(requirement)
    charts_read.chart_today_img()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

