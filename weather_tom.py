import requests
from bs4 import BeautifulSoup

def wheather(url, day):
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
    cloudiness = cloudiness_soup[len(cloudiness_soup)-1].text

    sun_soup = soup.find("div", class_="sunrise-sunset").find("div", class_="left").find_all("span", class_="text-value")
    sunrise = sun_soup[0].text
    sunset = sun_soup[1].text

    dane = ['nazwa;wartosc', "Temperatura;"+temperature, "Predkosc wiatru;"+wind, "Zachmurzenie;"+cloudiness, "wschod;"+sunrise, "zachod;"+sunset]
    f = open('weather_day'+day+'.csv', mode='w')
    for y in dane:
        text = y
        f.write(text+'\n')
    print("wschod: ", sunrise)
    print("zachod: ", sunset)
    print("Temperatura: ",  temperature)
    print("Predkosc wiatru: ", wind)
    print("Zachmurzenie: ", cloudiness)
    f.close()

for x in range (2,9):
    url = "https://www.accuweather.com/pl/pl/wojnarowa/274421/daily-weather-forecast/274421?day="+str(x)
    print(url)
    print(x)
    wheather(url, str(x))
