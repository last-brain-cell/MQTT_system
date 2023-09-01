import paho.mqtt.client as mqtt
import json
from pymongo import MongoClient
import pandas as pd

location_received = False
current_location = None  # currently scanned location

db_client = MongoClient("mongodb://127.0.0.1:27017/")  # if this doesn't work comment this one and uncomment the one below
# db_client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")

def process(message):
    data = json.loads(message)

    item_data = {
        "product_name": data.get("product_name", ""),
        "product_id": data.get("product_id", 0),
        "rfid_tag_id": data.get("rfid_tag_id", ""),
        "product_details": data.get("product_details", ""),
        "description": data.get("description", ""),
        "quantity": data.get("quantity", 0)
    }

    if item_data["product_name"] != '' and current_location:
        item_data.update(current_location)
        append_to_database(item_data)
        # append_to_csv(item_data)
        print("Item appended to database and CSV:", item_data)


def append_to_database(data):
    db = db_client["Product_Management"]
    # db = db_client["naad's_db"]
    collection = db["products"]
    # collection = db["rfid_data"]

    collection.insert_one(data)
    print("Appended to database")


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
        print("Connected to MQTT broker\nScan a location before scanning an item\nlistening for info...")
        if location_received:
            client.subscribe('item')
            print("Subscribed to 'item' topic")
        else:
            location_received = True
            client.subscribe("location")
            print("Subscribed to 'location' topic")
    else:
        print("Connection failed")


def on_message(client, userdata, message):
    global location_received, current_location

    payload = message.payload.decode('utf-8')
    data = json.loads(payload)

    if message.topic == "location":
        current_location = {
            "level": data.get("level", 0),
            "rack": data.get("rack", 0),
            "zone": data.get("zone", 0),
        }
        location_received = True
        print("Location received: ", current_location)
        client.subscribe('item')
        print("Subscribed to 'item' topic")
    elif message.topic == "item" and location_received:
        item_data = {
            "product_name": data.get("product_name", ""),
            "product_id": data.get("product_id", 0),
            "rfid_tag_id": data.get("rfid_tag_id", ""),
            "product_details": data.get("product_details", ""),
            "description": data.get("description", ""),
            "quantity": data.get("quantity", 0)
        }
        if item_data["product_name"] != '':
            if current_location:
                item_data.update(current_location)
                append_to_database(item_data)
                # append_to_csv(item_data)
                print("Item appended to database and CSV:", item_data)
            else:
                print("No location scanned yet. Item data ignored.")
    else:
        print("Invalid message or location not received yet.")


mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("data")
client.on_connect = on_connect
client.on_message = on_message  # message listener

client.connect(mqttBroker)
client.loop_forever()
db_client.close()
