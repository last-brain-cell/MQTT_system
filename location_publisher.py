import paho.mqtt.client as mqtt
from random import choice
import json

# Random Location Data for Random Picking
levels = [1, 2]
shelves = list(range(1, 21))
zones = ['Zone A', 'Zone B', 'Zone C', 'Zone D']

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print("Connection failed")

def send_location_data():
    level = choice(levels)
    shelf = choice(shelves)
    zone = choice(zones)
    location_data = {
        "level": level,
        "shelf": shelf,
        "zone": zone
    }
    message = json.dumps(location_data)
    topic = "location"
    client.publish(topic, message)
    print(message)


client = mqtt.Client()
client.on_connect = on_connect

broker_address = "mqtt.eclipseprojects.io"
client.connect(broker_address)

while True:
    user_input = input("Press Enter to an scan location")
    if user_input == "":
        send_location_data()
    else:
        break
