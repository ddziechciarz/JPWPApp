import csv
import matplotlib.pyplot as plt


def chart_today_img():
    time = []
    value = []
    with open('data/energy.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            energy = float(row[0])
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
    return energy


def get_static_data():
    data = []
    with open('data/basic.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            value = row[0].split(';')
            data.append(value[1])
    return data


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


def charts_prediction_img():
    time = []
    value = []
    with open('data/energy_prediction.csv') as csvfile:
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
    plt.savefig('img/energy_prediction.jpg', format='jpg')
    plt.close()


def get_sum_energy_today():
    with open('data/energy.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            sum_today = float(row[0])
    return round(sum_today, 2)


def get_sum_energy_prediction():
    sum_prediction = 0
    with open('data/energy_prediction.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            split = row[0].split(';')
            sum_prediction += float(split[1])
    return round(sum_prediction, 2)


def get_sum_energy_today_month():
    sum_today_month = 0
    with open('data/charts_month_today.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            split = row[0].split(';')
            sum_today_month += float(split[1])
    return round(sum_today_month, 2)


def get_sum_energy_last_month():
    sum_last_month = 0
    with open('data/charts_month_last.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            split = row[0].split(';')
            sum_last_month += float(split[1])
    return round(sum_last_month, 2)


def all_img():
    chart_today_img()
    charts_month_img('today')
    charts_month_img('last')
    charts_prediction_img()
    # print(get_sum_energy_today())
    # print(get_sum_energy_prediction())
    # print(get_sum_energy_today_month())
    # print(get_sum_energy_last_month())


all_img()
