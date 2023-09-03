import paho.mqtt.client as mqtt
from random import choice
import json

# Random Location Data for Random Picking
levels = [1, 2, 3]
# levels = [3]
zones = [1, 4]
# zones = [1]

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print("Connection failed")

def send_location_data():
    zone = choice(zones)
    if zone == 1:
        shelf = choice(list(range(1, 9)))
    else:
        shelf = choice(list(range(1, 5)))
    level = choice(levels)

    location_data = {
        "level": level,
        "rack": shelf,
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
