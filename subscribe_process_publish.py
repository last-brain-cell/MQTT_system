import paho.mqtt.client as mqtt
import json
from pymongo import MongoClient
import pandas as pd

location_received = False
db_client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")

def process(message):
    data = json.loads(message)

    if "topic" in data and data["topic"] == "location":
        location_data = {
            "level": data.get("level", ""),
            "shelf": data.get("shelf", ""),
            "zone": data.get("zone", ""),
            "rfid_tag_id": data.get("rfid_tag_id", "")
        }
        # append_to_database(location_data)
        append_to_csv(location_data)

    elif "topic" in data and data["topic"] == "item":
        item_data = {
            "product_name": data.get("product_name", ""),
            "product_id": data.get("product_id", ""),
            "rfid_tag_id": data.get("rfid_tag_id", ""),
            "info": data.get("info", ""),
            "quantity": data.get("quantity", 0)
        }
        # append_to_database(item_data)
        append_to_csv(item_data)


def append_to_database(data):
    try:
        db = db_client["naad's_db"]
        collection = db["rfid_data"]

        collection.insert_one(data)

        db_client.close()

    except Exception as e:
        print(e)


def append_to_csv(data):
    fieldnames = list(data.keys())
    try:
        df = pd.read_csv("mqtt_version/arch/data.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=fieldnames)

    df = df.append(data, ignore_index=True)
    try:
        df.to_csv("mqtt_version/arch/data.csv", index=False)
        print("Data appended to CSV successfully.")
    except Exception as e:
        print("Error while writing to CSV:", e)

def on_connect(client, userdata, flags, rc):
    global location_received
    if rc == 0:
        print("Connected to MQTT broker\nlistening for info...")
        # if location_received:
        #     client.subscribe('item')
        #     print("Subscribed to 'item' topic")
        # else:
        #     location_received = True
        #     client.subscribe("location")
        #     client.subscribe('item')
        #     print("Subscribed to 'location' topic")
        client.subscribe("location")
        client.subscribe('item')
    else:
        print("Connection failed")

def on_message(client, userdata, message):
    payload = message.payload.decode('utf-8')
    process(payload)
    print("Received message: ", payload)


mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("data")
client.on_connect = on_connect
client.on_message = on_message

client.connect(mqttBroker)
client.loop_forever()
