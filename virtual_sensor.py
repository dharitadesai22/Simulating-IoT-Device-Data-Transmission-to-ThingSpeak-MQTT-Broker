import random  # Import the random module to generate random numbers

class VirtualIoTSensor:
    def __init__(self):
        # Initialize sensor value ranges: 
        # Temperature range in Celsius, Humidity range in percentage, CO2 range in ppm (parts per million)
        self.temperatureRange = (-50, 50)  # Temperature can vary from -50 to 50 degrees Celsius
        self.humidityRange = (0, 100)      # Humidity can vary from 0 to 100 percent
        self.co2Range = (300, 2000)        # CO2 concentration can vary from 300 to 2000 ppm

    def generateSensorValues(self):
        # Generate random sensor values within the specified ranges
        temperature = random.uniform(*self.temperatureRange)  # Generate a random temperature
        humidity = random.uniform(*self.humidityRange)        # Generate a random humidity
        co2 = random.uniform(*self.co2Range)                  # Generate a random CO2 concentration
        return temperature, humidity, co2  # Return the generated values as a tuple