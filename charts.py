import requests
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import math
from bs4 import BeautifulSoup
from login_pass import *

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
time.sleep(15)

driver.get('https://home.solarman.cn/cpro/epc/plantDetail/showCharts.json?plantId=1623212&type=1&date=2023%2F04%2F11&plantTimezoneId=39')
charts_data = driver.page_source
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
f = open('charts.csv', mode='w')
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
    f.write(str_time+";"+z + '\n')
    minutes += 10
f.close()
