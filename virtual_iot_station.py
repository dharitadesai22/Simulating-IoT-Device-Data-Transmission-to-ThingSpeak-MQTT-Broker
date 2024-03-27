import random

'''
  Helper class to generate random sensor data
'''

class VirtualIoTStation:
    def __init__(self):
        self.temperature_range = (-50, 50)
        self.humidity_range = (0, 100)
        self.co2_range = (300, 2000)

    def generate_sensor_values(self):
        temperature = random.uniform(*self.temperature_range)
        humidity = random.uniform(*self.humidity_range)
        co2 = random.uniform(*self.co2_range)
        return temperature, humidity, co2