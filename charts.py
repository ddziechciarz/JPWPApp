import requests
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import math
import datetime
from bs4 import BeautifulSoup
from login_pass import *

def login():
    driver = webdriver.Chrome()
    driver.get("https://home.solarman.cn/main.html")
    time.sleep(10)
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # wprowadzenie danych użytkownika
    username_field.send_keys(LOGIN_SOLARMAN)
    password_field.send_keys(PASSWORD_SOLARMAN)

    # zatwierdzenie formularza
    password_field.send_keys(Keys.RETURN)
    time.sleep(20)
    return driver

def energy():
    driver = login()
    today = datetime.datetime.now()
    month = today.strftime("%m")
    day = today.strftime("%d")
    driver.get('https://home.solarman.cn/cpro/epc/plantDetail/showCharts.json?plantId=1623212&type=1&date=2023%2F' + month + '%2F' + day + '&plantTimezoneId=39')
    charts_data = driver.page_source
    charts_split = charts_data.split('{')
    charts_line = charts_split[len(charts_split)-1].split(',')
    charts_value = charts_line[2]
    energy = charts_value[9:len(charts_value)]
    return energy

def energy_prediction():
    driver = login()
    today = datetime.datetime.now()
    month = today.strftime("%m")
    day = today.strftime("%d")
    day_int = int(day) - 1
    day = '0' + str(day_int)
    driver.get('https://home.solarman.cn/cpro/epc/plantDetail/showCharts.json?plantId=1623212&type=1&date=2023%2F' + month + '%2F' + day + '&plantTimezoneId=39')
    charts_data = driver.page_source
    charts_split = charts_data.split('{')
    charts_line = charts_split[len(charts_split)-1].split(',')
    charts_value = charts_line[2]
    energy = charts_value[9:len(charts_value)]
    return energy

def charts_today():
    driver = login()
    today = datetime.datetime.now()
    month = today.strftime("%m")
    day = today.strftime("%d")
    driver.get('https://home.solarman.cn/cpro/epc/plantDetail/showCharts.json?plantId=1623212&type=1&date=2023%2F'+month+'%2F'+day+'&plantTimezoneId=39')
    charts_data = driver.page_source
    print(charts_data)
    charts_split = charts_data.split('{')
    final_charts = []
    for x in range(3, len(charts_split)-1):
        charts_line = charts_split[x].split(',')
        charts_value = charts_line[3]
        if x == len(charts_split)-2:
            final_charts.append(charts_value[8:len(charts_value) - 2])
            break
        final_charts.append(charts_value[8:len(charts_value) - 1])
    url = "https://www.accuweather.com/pl/pl/wojnarowa/274421/daily-weather-forecast/274421?day=1"
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    soup = BeautifulSoup(response.text, "html.parser")
    sun_soup = soup.find("div", class_="sunrise-sunset").find("div", class_="left").find_all("span", class_="text-value")
    sunrise = sun_soup[0].text.split(':')
    hour = int(sunrise[0])
    minutes_float = float(sunrise[1])
    minutes = math.ceil(minutes_float/10)*10
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
        f.write(str_time+";"+z + '\n')
        minutes += 10
    f.close()
    charts.append(charts_time)
    charts.append(final_charts)
    driver.close()
    return charts

def charts_month_today():
    driver = login()
    time.sleep(20)
    today = datetime.datetime.now()
    month = today.strftime("%m")
    driver.get('https://home.solarman.cn/cpro/epc/plantDetail/showCharts.json?plantId=1623212&type=2&date=2023%2F'+month+'&plantTimezoneId=39')
    charts_data = driver.page_source
    charts_split = charts_data.split('{')
    final_charts = []
    for x in range(3, len(charts_split)-2):
        charts_line = charts_split[x].split(',')
        charts_value = charts_line[3]
        if charts_value == '':
            final_charts.append('0.00')
        else:
            final_charts.append(charts_value[9:len(charts_value)])
    charts = []
    charts_days = []
    day = 1
    f = open('charts_month_today.csv', mode='w')
    for z in final_charts:
        if day < 10:
            day_str = '0' + str(day)
        else:
            day_str = str(day)
        charts_days.append(day_str)
        f.write(day_str+";"+z + '\n')
        day += 1
    f.close()
    charts.append(charts_days)
    charts.append(final_charts)
    driver.close()
    return charts


def charts_month_last():
    driver = login()
    today = datetime.datetime.now()
    month = today.strftime("%m")
    month_int = int(month) - 1
    month = '0' + str(month_int)
    driver.get('https://home.solarman.cn/cpro/epc/plantDetail/showCharts.json?plantId=1623212&type=2&date=2023%2F'+month+'&plantTimezoneId=39')
    charts_data = driver.page_source
    charts_split = charts_data.split('{')
    final_charts = []
    for x in range(3, len(charts_split)-2):
        charts_line = charts_split[x].split(',')
        charts_value = charts_line[3]
        if charts_value == '':
            final_charts.append('0.00')
        else:
            final_charts.append(charts_value[9:len(charts_value)])
    charts = []
    charts_days = []
    day = 1
    f = open('charts_month_last.csv', mode='w')
    for z in final_charts:
        if day < 10:
            day_str = '0' + str(day)
        else:
            day_str = str(day)
        charts_days.append(day_str)
        f.write(day_str+";"+z + '\n')
        day += 1
    f.close()
    charts.append(charts_days)
    charts.append(final_charts)
    driver.close()
    return charts


#print(energy_prediction())

#data_charts = charts_today()
#for ch in range(0, len(data_charts[0])):
#    print(data_charts[0][ch])
#    print(data_charts[1][ch])
