import csv
import matplotlib.pyplot as plt


def chart_today_img():
    time = []
    value = []
    with open('data/charts_today.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            split = row[0].split(';')
            time.append(split[0])
            value.append(float(split[1]))
    plt.figure(figsize=(10, 5))
    plt.plot(time, value, color="dodgerblue")
    plt.xlabel('Hour')
    plt.ylabel('Value')
    plt.title('Daily production')
    plt.xticks(['6:00', '9:00', '12:00', '15:00', '18:00', '21:00'])
    plt.yticks([1, 2, 3, 4, 5, 6, 7], ['1kW', '2kW', '3kW', '4kW', '5kW', '6kW', '7kW'])
    plt.grid(axis='y')
    plt.savefig('img/charts_today.jpg', format='jpg')
    plt.close()


def charts_month_img(month):
    time = []
    value = []
    with open('data/charts_month_' + month + '.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            split = row[0].split(';')
            time.append(split[0])
            value.append(float(split[1]))
    plt.figure(figsize=(10, 5))
    plt.bar(time, value, color="dodgerblue", edgecolor="white", width=1, linewidth=5)
    plt.xlabel('Day')
    plt.ylabel('Value')
    plt.title('Monthly production')
    plt.yticks([10, 20, 30, 40], ['10kWh', '20kWh', '30kWh', '40kWh'])
    plt.grid(axis='y')
    plt.savefig('img/charts_month_' + month + '.jpg', format='jpg')
    plt.close()


def all_img():
    chart_today_img()
    charts_month_img('today')
    charts_month_img('last')

all_img()
