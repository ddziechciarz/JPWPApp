# JPWPApp

## Instalowanie QtDesginer:
```
pip install PyQt6 
pip instal pyqt6-tools
```
przejdź do folderu z Pythonem Python310/Lib/site-packages/qt6_applications/QT/bin i otwórz aplikację designer  
https://www.youtube.com/watch?v=NU3DQwMKz00 tutorial instalacji

## zadania
Postaraj się odtworzyć strone Predictions w aplikacji QtDesigner  
Przykładowa strona Predictions:
![Alt text](https://github.com/ddziechciarz/JPWPApp/blob/Excercise/assets/SampleUI.jpg?raw=true)
![Alt text](https://github.com/ddziechciarz/JPWPApp/blob/Excercise/assets/SampleProjetTree.jpg?raw=true)





Wykorzystując biblioteki 'csv' odczytaj dane z pliku 'charts.csv' znajdującego się w folderze 'data', przeykładowa implementacja: 
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
