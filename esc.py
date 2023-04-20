import csv
import matplotlib.pyplot as plt


def esc():
    time = []
    value = []
    with open('data/exercise.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            split = row[0].split(';')
            time.append(split[0])
            value.append(float(split[1]))
    plt.figure(figsize=(10, 5))
    plt.bar(time, value, color="dodgerblue", edgecolor="white", width=1, linewidth=5)
    plt.xlabel('Day')
    plt.ylabel('Value')
    plt.title('Predictions')
    plt.yticks([10, 20, 30, 40], ['10kWh', '20kWh', '30kWh', '40kWh'])
    plt.grid(axis='y')
    plt.savefig('img/exercise.jpg', format='jpg')
    plt.close()

esc()