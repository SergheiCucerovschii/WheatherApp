from http.client import HTTPSConnection
from json import loads

key = "eef9a6e3a696817d913d2df9e2ba51ba"
city = input("What location you want?").capitalize()
domain = "api.openweathermap.org"
endpoint_current = f"/data/2.5/weather?q={city}&appid={key}&units=metric&lang=ru"

def menu(title, options):
    print(f'##### {title:^15} #####')
    for k in options:
        print(f'{k}. {options[k]}')
    print(f'##### {"Choose Option":^15} #####')
    selected = int(input('>>'))
    if selected not in options:
        print('Wrong option!')
    return selected

def connection():
    connection = HTTPSConnection(domain)
    connection.request("GET", endpoint_current)
    response = connection.getresponse()
    data = loads(response.read())
    connection.close()
    return data

def temperature(connection):
    temp = connection()['main']['temp']
    print(f"TEMPERATURE in {connection()['name']}: {temp}℃")

def wind(connection):
    wind = connection()['wind']['speed']
    print(f"WIND SPEED in {connection()['name']}: {wind}m/s")

def weather(connection):
    weather = connection()['weather'][0]['description']
    print(f"WEATHER in {connection()['name']}: {weather}")


while True:
    result = menu('Weather App', {
        1: 'Temperature',
        2: 'Weather',
        3: 'Wind ',
        0: 'Exit'
    })

    if result == 1:
        data = connection()
        data = temperature(connection)

    if result == 2:
        data = connection()
        data = weather(connection)
    if result == 3:
        data = connection()
        data = wind(connection)
    if result == 0:
        print("Thank you!")
