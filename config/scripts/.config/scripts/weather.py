#!/usr/bin/python3
import pyowm
icons = {
    '04n' : ' ',
    '04d' : ' ' , 
    '01d' : ' ',
    '01n' : ' ',
    '02d' : ' ',
    '02n' : ' ' ,
    '03d' : ' ',
    '03n' : ' ',
    '09d' : '',
    '09n' : '',
    '10d' : '',
    '10n' : '',
    '11d' : '',
    '11n' : '',
    '13d' : ' ',
    '13n' : ' ',
    '50d' : '',
    '50n' : ''
}
try:
    owm = pyowm.OWM('0889e27988b659f5771cd0aabfd7379d')
    weather = owm.weather_at_place('Paris,FR').get_weather()
    print("{0} {1:0.1f}°C".format(
            icons[weather.get_weather_icon_name()],
            float(weather.get_temperature(unit='celsius')['temp'])
        )
    )
except pyowm.exceptions.api_call_error.APICallError:
    print("X -.--°C")

