# Import necessary libraries
import paho.mqtt.publish as publish  # MQTT publishing library
from virtual_sensor import VirtualIoTSensor  # Simulated IoT sensor
import time  # Time library for sleep
import datetime  # Datetime library for timestamping

class IoTDataPublisher:
    """Class to publish IoT sensor data to a ThingSpeak channel via MQTT."""
    
    def __init__(self, channel_id, client_id, username, password):
        """Initializes the IoTDataPublisher with MQTT broker settings and credentials."""
        self.mqtt_host = "mqtt3.thingspeak.com"  # Hostname of the ThingSpeak MQTT broker
        self.transport = "websockets"  # Transport protocol for MQTT
        self.port = 80  # Port for MQTT communication
        self.topic = f"channels/{channel_id}/publish"  # MQTT topic for publishing data
        self.client_id = client_id  # MQTT client ID
        self.auth = {'username': username, 'password': password}  # MQTT authentication credentials
        self.sensor = VirtualIoTSensor()  # Initialize the virtual IoT sensor

    def publish_data(self):
        """Generates sensor values, constructs a payload, and publishes it to the MQTT broker."""
        temperature, humidity, co2 = self.sensor.generateSensorValues()  # Generate sensor values
        payload = self._format_payload(temperature, humidity, co2)  # Construct payload string
        # Print a log message with the current timestamp, payload, and MQTT client ID
        print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Writing Payload= {payload} to host= {self.mqtt_host} clientID= {self.client_id}")
        # Publish the payload to the MQTT broker
        publish.single(self.topic, payload, hostname=self.mqtt_host, transport=self.transport, port=self.port, client_id=self.client_id, auth=self.auth)

    @staticmethod
    def _format_payload(temperature, humidity, co2):
        """Formats the sensor values into a string payload for MQTT publication."""
        return f"field1={temperature}&field2={humidity}&field3={co2}"  # Return formatted payload

# Configuration section - Replace with your actual MQTT credentials and channel ID
MQTT_CHANNEL_ID = "ENTER YOUR CHANNEL ID"
MQTT_CLIENT_ID = "ENTER YOUR CLIENT ID"
MQTT_USERNAME = "ENTER YOUR CLIENT USERNAME"
MQTT_PASSWORD = "ENTER YOUR CLIENT PASSWORD"

if __name__ == "__main__":
    # Main script execution:
    # Create an instance of IoTDataPublisher with the provided credentials
    publisher = IoTDataPublisher(MQTT_CHANNEL_ID, MQTT_CLIENT_ID, MQTT_USERNAME, MQTT_PASSWORD)
    while True:  # Infinite loop to continuously publish data
        publisher.publish_data()  # Publish sensor data to MQTT broker
        time.sleep(5)  # Wait for 5 seconds before the next publish
