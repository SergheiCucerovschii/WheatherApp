from http.client import HTTPSConnection
from json import loads


def menu(title, options):
    print(f'##### {title:^15} #####')
    for k in options:
        print(f'{k}. {options[k]}')
    print(f'##### {"Choose Option":^15} #####')
    selected = int(input('>>'))
    if selected not in options:
        print('Wrong option!')
    return selected


def loadData():
    key = "d54d475a90909b2e41a6011fa52a352f"
    city = input("Enter the city to see weather:")
    domain = "api.openweathermap.org"
    endpoint_current = f"/data/2.5/weather?q={city}&appid={key}&units=metric"

    connection = HTTPSConnection(domain)
    connection.request("GET", endpoint_current)
    response = connection.getresponse()
    data = loads(response.read())
    connection.close()
    return data


def process_dataTemp(data):
    temp = data['main']['temp']
    return temp


def process_dataWind(data):
    wind = data['wind']['speed']
    return wind


def process_dataWeather(data):
    weather = data['weather'][0]['description']
    return weather


def process_dataLocation(data):
    location = data['name']
    return location


def printData(temp, wind, weather, location):
    print(f"Temperature in {location}: {temp}°C")
    print(f"Wind speed  in {location}: {wind}m/s")
    print(f"Weather     in {location}: {weather}")


###############################################################

while True:
    result = menu("Main", {
        1: 'Weather in my town.',
        0: 'Exit'
    })
    if result == 1:
        data = loadData()
        if data['cod'] == 200:
            temp = process_dataTemp(data)
            wind = process_dataWind(data)
            weather = process_dataWeather(data)
            location = process_dataLocation(data)
            printData(temp, wind, weather, location)
        else:
            print("Error! City not found")
    elif result == 0:
        print("Thank you!")
        break

