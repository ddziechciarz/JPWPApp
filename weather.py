import requests
import datetime
from bs4 import BeautifulSoup


def weather_today(url):
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
    f = open('data/weather_tod.csv', mode='w')
    for y in data:
        text = y
        f.write(text + '\n')
    f.close()
    return cloudiness[0:len(cloudiness) - 1]


weather_today('https://www.accuweather.com/pl/pl/krakow/274455/daily-weather-forecast/274455?day=1')

