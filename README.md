# JPWPApp

## Instalowanie QtDesginer:
```
pip install PyQt6 
pip instal pyqt6-tools
```
przejdź do folderu z Pythonem Python310/Lib/site-packages/qt6_applications/QT/bin i otwórz aplikację designer  
https://www.youtube.com/watch?v=NU3DQwMKz00 tutorial instalacji

## Zadania
Postaraj się odtworzyć strone Predictions w aplikacji QtDesigner, przykładowa strona Predictions:
![Alt text](https://github.com/ddziechciarz/JPWPApp/blob/Excercise/assets/SampleUI.jpg?raw=true)
![Alt text](https://github.com/ddziechciarz/JPWPApp/blob/Excercise/assets/SampleProjetTree.jpg?raw=true)





Następnie dodaj funkcję przełączania do zakładki Predictions do odpowiedniego przycisku, np:
```
self.ui.infoButton.clicked.connect(lambda: self.ui.leftMenuContents.setCurrentIndex(0))
```
Wykorzystując biblioteki 'csv' odczytaj dane z pliku 'exercise.csv' znajdującego się w folderze 'data', przeykładowa implementacja: 

```
data = []
with open('data/basic.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        value = row[0].split(';')
        data.append(value[1])
```
Następnie przy pomocy modułu 'pyplot' biblioteki 'matplotlib' wygeneruj wykres, który zostanie zapisany w folderze 'img'. Po bardziej rozbudowany kod zaglądnij do pliku charts_read.py, przykładowa implementacja: 
```
plt.figure(figsize=(10, 5))
plt.plot(time, value, color="dodgerblue")
plt.savefig('img/charts_today.jpg', format='jpg')
plt.close()
```
Następnie dodaj wygenerowany wykres do utworzonej przez ciebie zakładki Predictions. Przykładowa implementacja dodawania wykresu do zakładki Home:
```
pixmapHome = QPixmap('img/charts_today.jpg')
self.ui.graphLabelHome.setPixmap(pixmapHome)
self.ui.graphLabelHome.setScaledContents(True)
```
Potem pobierz dane o przewidywanej wyprodukowanej energii i za ich pomocą uzupełnij pola przewidywanej produkcji i przewidywanej oszczędności, np:
```
def updateHomeStats(self, energy):
    self.ui.totalProducedValue.setText(str(energy) + "kWh")
    self.ui.moneySavedValue.setText(str(round(energy * 0.77,2)) + " PLN")
    self.ui.avoidedCO2Value.setText(str(round(energy * 0.452,2)) + " kg")
```
