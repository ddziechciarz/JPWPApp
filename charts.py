import requests
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import math
import datetime
from bs4 import BeautifulSoup
from login_pass import *
from charts_read import *


def login():
    driver = webdriver.Chrome()
    driver.get("https://home.solarman.cn/main.html")
    time.sleep(5)
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    username_field.send_keys(LOGIN_SOLARMAN)
    password_field.send_keys(PASSWORD_SOLARMAN)

    password_field.send_keys(Keys.RETURN)
    time.sleep(5)
    return driver


def energy(driver, month, day):
    driver.get(
        'https://home.solarman.cn/cpro/epc/plantDetail/showCharts.json?plantId=1623212&type=1&date=2023%2F04%2F11&plantTimezoneId=39')
    # driver.get('https://home.solarman.cn/cpro/epc/plantDetail/showCharts.json?plantId=1623212&type=1&date=2023%2F'+month+'%2F'+day+'&plantTimezoneId=39')
    charts_data = driver.page_source
    charts_split = charts_data.split('{')
    charts_line = charts_split[len(charts_split) - 1].split(',')
    charts_value = charts_line[2]
    energy = charts_value[9:len(charts_value)]
    return energy


def energy_prediction():
    month_percent = [0.039, 0.051, 0.081, 0.109, 0.114, 0.116, 0.123, 0.119, 0.096, 0.074, 0.045, 0.033]
    yearly = 1275.6 * 6 * 0.7683
    today = datetime.datetime.now()
    month = int(today.strftime("%m"))
    day = int(today.strftime("%d"))
    monthly = yearly * month_percent[month - 1]
    daily = monthly / 30
    average = daily / 0.57
    f = open('data/energy_prediction.csv', mode='w')
    for x in range(2, 9):
        url = "https://www.accuweather.com/pl/pl/wojnarowa/274421/daily-weather-forecast/274421?day=" + str(x)
        cloudiness = int(wheather_next(url, str(x))) / 100
        day += 1
        value = average * month_percent[month - 1] + average * (1 - cloudiness)
        f.write(str(day) + ";" + str(value) + '\n')
    f.close()


def wheather_today(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    soup = BeautifulSoup(response.text, "html.parser")

    temperature_soup = soup.find("div", class_="temperature").text.split()
    temperature = ''
    for x in temperature_soup[0]:
        if x != '°':
            temperature += x
        else:
            break

    wind_soup = soup.find("div", class_="left").find_all("span")
    if len(wind_soup) == 4:
        wind = wind_soup[2].text
    else:
        wind = wind_soup[1].text

    cloudiness_soup = soup.find("div", class_="right").find_all("span")
    cloudiness = cloudiness_soup[len(cloudiness_soup) - 1].text

    sun_soup = soup.find("div", class_="sunrise-sunset").find("div", class_="left").find_all("span",
                                                                                             class_="text-value")
    sunrise = sun_soup[0].text
    sunset = sun_soup[1].text
    fulldate = datetime.datetime.now()
    date = fulldate.strftime("%x")
    time = fulldate.strftime("%X")
    data = ['nazwa;wartosc', "Temperatura;" + temperature, "Predkosc wiatru;" + wind, "Zachmurzenie;" + cloudiness,
            "wschod;" + sunrise, "zachod;" + sunset, "data;" + date, "godzina;" + time]
    f = open('weather_tod.csv', mode='w')
    for y in data:
        text = y
        f.write(text + '\n')
    return cloudiness[0:len(cloudiness) - 1]
    f.close()


def wheather_next(url, day):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    soup = BeautifulSoup(response.text, "html.parser")

    temperature_soup = soup.find("div", class_="temperature").text.split()
    temperature = ''
    for x in temperature_soup[0]:
        if x != '°':
            temperature += x
        else:
            break

    wind_soup = soup.find("div", class_="left").find_all("span")
    if len(wind_soup) == 3:
        wind = wind_soup[1].text
    else:
        wind = wind_soup[2].text

    cloudiness_soup = soup.find("div", class_="right").find_all("span")
    cloudiness = cloudiness_soup[len(cloudiness_soup) - 1].text

    sun_soup = soup.find("div", class_="sunrise-sunset").find("div", class_="left").find_all("span",
                                                                                             class_="text-value")
    sunrise = sun_soup[0].text
    sunset = sun_soup[1].text

    data = ['nazwa;wartosc', "Temperatura;" + temperature, "Predkosc wiatru;" + wind, "Zachmurzenie;" + cloudiness,
            "wschod;" + sunrise, "zachod;" + sunset]
    f = open('weather_day' + day + '.csv', mode='w')
    for y in data:
        text = y
        f.write(text + '\n')
    return cloudiness[0:len(cloudiness) - 1]
    f.close()


def charts_today(driver, month, day):
    driver.get(
        'https://home.solarman.cn/cpro/epc/plantDetail/showCharts.json?plantId=1623212&type=1&date=2023%2F04%2F11&plantTimezoneId=39')
    # driver.get('https://home.solarman.cn/cpro/epc/plantDetail/showCharts.json?plantId=1623212&type=1&date=2023%2F'+month+'%2F'+day+'&plantTimezoneId=39')
    charts_data = driver.page_source
    charts_split = charts_data.split('{')
    final_charts = []
    for x in range(3, len(charts_split) - 1):
        charts_line = charts_split[x].split(',')
        charts_value = charts_line[3]
        if x == len(charts_split) - 2:
            final_charts.append(charts_value[8:len(charts_value) - 2])
            break
        final_charts.append(charts_value[8:len(charts_value) - 1])
    url = "https://www.accuweather.com/pl/pl/wojnarowa/274421/daily-weather-forecast/274421?day=1"
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    soup = BeautifulSoup(response.text, "html.parser")
    sun_soup = soup.find("div", class_="sunrise-sunset").find("div", class_="left").find_all("span",
                                                                                             class_="text-value")
    sunrise = sun_soup[0].text.split(':')
    hour = int(sunrise[0])
    minutes_float = float(sunrise[1])
    minutes = math.ceil(minutes_float / 10) * 10
    charts = []
    charts_time = []
    f = open('charts_today.csv', mode='w')
    for z in final_charts:
        if minutes == 60:
            minutes = 0
            hour += 1
        str_hour = str(hour)
        str_minutes = str(minutes)
        if minutes != 0:
            str_time = str_hour + ':' + str_minutes
        else:
            str_time = str_hour + ':' + str_minutes + str_minutes
        charts_time.append(str_time)
        f.write(str_time + ";" + z + '\n')
        minutes += 10
    f.close()
    charts.append(charts_time)
    charts.append(final_charts)


def charts_month(driver, value_month, month):
    if value_month == "last":
        month_int = int(month) - 1
        month = '0' + str(month_int)
    driver.get(
        'https://home.solarman.cn/cpro/epc/plantDetail/showCharts.json?plantId=1623212&type=2&date=2023%2F' + month + '&plantTimezoneId=39')
    charts_data = driver.page_source
    charts_split = charts_data.split('{')
    final_charts = []
    for x in range(3, len(charts_split) - 2):
        charts_line = charts_split[x].split(',')
        charts_value = charts_line[3]
        if charts_value == '':
            final_charts.append('0.00')
        else:
            final_charts.append(charts_value[9:len(charts_value)])
    charts_days = []
    day = 1
    f = open('charts_month_' + value_month + '.csv', mode='w')
    for z in final_charts:
        if day < 10:
            day_str = '0' + str(day)
        else:
            day_str = str(day)
        charts_days.append(day_str)
        f.write(day_str + ";" + z + '\n')
        day += 1
    f.close()


def download():
    driver = login()
    today = datetime.datetime.now()
    month = today.strftime("%m")
    day = today.strftime("%d")
    energy(driver, month, day)
    charts_today(driver, month, day)
    charts_month(driver, 'today', month)
    charts_month(driver, 'last', month)
    driver.close()


download()
