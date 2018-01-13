#!/usr/bin/python3
import pyowm
owm = pyowm.OWM('')
weather = owm.weather_at_place('Paris,FR').get_weather()
print("{0}, {1}°C".format(
        weather.get_status(), 
        weather.get_temperature(unit='celsius')['temp']
    )
)

