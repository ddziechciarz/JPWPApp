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
        self.setFixedSize(1072, 683)
        self.show()

        self.ui.infoButton.clicked.connect(lambda: self.ui.leftMenuContents.setCurrentIndex(0))
        self.ui.helpButton.clicked.connect(lambda: self.ui.leftMenuContents.setCurrentIndex(1))

        self.ui.homeButton.clicked.connect(lambda: self.ui.mainContent.setCurrentIndex(0))
        self.ui.statsButton.clicked.connect(lambda: self.ui.mainContent.setCurrentIndex(1))
        self.ui.predButton.clicked.connect(lambda: self.ui.mainContent.setCurrentIndex(2))

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

        self.todayTotalEnergy = charts_read.get_sum_energy_today()
        self.thisMonthTotalEnergy = charts_read.get_sum_energy_today_month()
        self.lastMonthTotalEnergy = charts_read.get_sum_energy_last_month()
        self.predictedTotalEnergy = charts_read.get_sum_energy_prediction()

        self.updateHomeStats(self.todayTotalEnergy)
        self.updatePredictionStats(self.predictedTotalEnergy)
        self.updateStaticData(charts_read.get_static_data())
        self.comboBoxClicked()



    def comboBoxClicked(self):
        currentSelection = self.ui.comboBox.currentText()
        if currentSelection == 'Last Day':
            self.ui.stackedWidetStats.setCurrentIndex(0)
            self.updateStats(self.todayTotalEnergy)
        elif currentSelection == 'This Month':
            self.ui.stackedWidetStats.setCurrentIndex(2)
            self.updateStats(self.thisMonthTotalEnergy)
        else:
            self.ui.stackedWidetStats.setCurrentIndex(1)
            self.updateStats(self.lastMonthTotalEnergy)

    def updateHomeStats(self, energy):
        self.ui.totalProducedValue.setText(str(energy) + "kWh")
        self.ui.moneySavedValue.setText(str(round(energy * 0.77,2)) + " PLN")
        self.ui.avoidedCO2Value.setText(str(round(energy * 0.452,2)) + " kg")

    def updatePredictionStats(self, energy):
        self.ui.predictedProductionValue.setText(str(energy) + "kWh")
        self.ui.predictedSavingsValue.setText(str(round(energy * 0.77,2)) + " PLN")

    def updateStats(self, energy):
        self.ui.totalProducedValueStat.setText(str(energy) + "kWh")
        self.ui.moneySavedValueStat.setText(str(round(energy * 0.77, 2)) + " PLN")
        self.ui.avoidedCO2ValueStat.setText(str(round(energy * 0.452, 2)) + " kg")

    def updateStaticData(self, data):
        self.ui.capacityLabel.setText("Capacity: " + str(data[0]) + "kWh")
        self.ui.angleLabel.setText("Angle of Inclination: " + str(data[1]))
        date = data[2].split("-")
        self.ui.installedDateLavel.setText("Installation Date: " + str(date[0]) + "." + str(date[1]) + "." + str(date[2]))

if __name__ == "__main__":
    #for requirement in freeze(local_only=True):
    #    print(requirement)
    #charts_read.chart_today_img()

    #print(charts_read.get_static_data())
    charts_read.all_img()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

