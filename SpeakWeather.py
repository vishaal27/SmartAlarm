import datetime
import json
import time
import urllib.request
from espeak import espeak


def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return converted_time


def url_builder(city_id):
    user_api = '3ce8aff62271ce0fbe28063131cb2376'  # Obtain yours form: http://openweathermap.org/
    unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
    api = 'http://api.openweathermap.org/data/2.5/weather?id='     # Search for your city ID here: http://bulk.openweathermap.org/sample/city.list.json.gz

    full_api_url = api + str(city_id) + '&mode=json&units=' + unit + '&APPID=' + user_api
    return full_api_url


def data_fetch(full_api_url):
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    raw_api_dict = json.loads(output)
    url.close()
    return raw_api_dict


def data_organizer(raw_api_dict):
    data = dict(
        city=raw_api_dict.get('name'),
        country=raw_api_dict.get('sys').get('country'),
        temp=raw_api_dict.get('main').get('temp'),
        temp_max=raw_api_dict.get('main').get('temp_max'),
        temp_min=raw_api_dict.get('main').get('temp_min'),
        humidity=raw_api_dict.get('main').get('humidity'),
        pressure=raw_api_dict.get('main').get('pressure'),
        sky=raw_api_dict['weather'][0]['main'],
        sunrise=time_converter(raw_api_dict.get('sys').get('sunrise')),
        sunset=time_converter(raw_api_dict.get('sys').get('sunset')),
        wind=raw_api_dict.get('wind').get('speed'),
        wind_deg=raw_api_dict.get('deg'),
        dt=time_converter(raw_api_dict.get('dt')),
        cloudiness=raw_api_dict.get('clouds').get('all')
    )
    return data


def data_output(data):
    m_symbol = '\xb0' + 'C'
    print('---------------------------------------')
    print('Current weather in: {}, {}:'.format(data['city'], data['country']))
    print(data['temp'], m_symbol, data['sky'])
    print('Max: {}, Min: {}'.format(data['temp_max'], data['temp_min']))
    print('')
    print('Wind Speed: {}, Degree: {}'.format(data['wind'], data['wind_deg']))
    print('Humidity: {}'.format(data['humidity']))
    print('Cloud: {}'.format(data['cloudiness']))
    print('Pressure: {}'.format(data['pressure']))
    print('Sunrise at: {}'.format(data['sunrise']))
    print('Sunset at: {}'.format(data['sunset']))
    print('')
    print('Last update from the server: {}'.format(data['dt']))
    print('---------------------------------------')
    espeak.synth('Hello Vishaal.')
    time.sleep(2)
    espeak.synth(' The current weather conditions in Delhi are')
    time.sleep(2)
    temp=data['temp']
    espeak.synth('The current temperature is '+str(temp)+'degrees celsius')
    time.sleep(2)
    espeak.synth('The condition of the sky is '+data['sky'])
    time.sleep(2)
    espeak.synth('The maximum temperature in the day is '+str(data['temp_max'])+'degrees celsius')
    time.sleep(2)
    espeak.synth('The minimum temperature in the day is '+str(data['temp_min'])+'degrees celsius')
    time.sleep(2)
    espeak.synth('The relative humidity percentage is '+str(data['humidity']))
    time.sleep(2)
    time.sleep(2)
    time.sleep(2)

if __name__ == '__main__':
    	data_output(data_organizer(data_fetch(url_builder(1273294))))

#{'sky': 'Haze', 
#'pressure': 1016, 
#'sunrise': '06:31 AM',
 #'sunset': '06:29 PM',
  #'temp_max': 24,
   #'temp': 24,
    #'city': 'Delhi',
     #'wind': 4.6,
      #'temp_min': 24,
       #'cloudiness': 8,
        #'wind_deg': None,
#'dt': '06:00 PM', 
 #'country': 'IN',
 # 'humidity': 27