import paho.mqtt.client as mqtt
from random import randint
import json

# Random Items Data for Random Picking
product_names = ['Screws', 'Hammers', 'Pliers', 'Wrenches', 'Nuts', 'Bolts', 'Drills', 'Saws', 'Rivets', 'Chisels', 'Sockets', 'Tapes', 'Soldering Irons', 'Files', 'Tweezers', 'Gloves', 'Measuring Tapes', 'Cutting Discs', 'Welding Masks', 'Clamps']
product_ids = [4521, 8792, 1234, 5678, 9012, 3456, 7890, 2345, 6789, 8901, 7362, 5789, 9154, 2673, 8291, 5032, 1498, 3826, 6715, 2940]
rfid_tag_ids = ['RFID123456', 'RFID987654', 'RFID234567', 'RFID876543', 'RFID345678', 'RFID765432', 'RFID456789', 'RFID654321', 'RFID567890', 'RFID098765', 'RFID736251', 'RFID578912', 'RFID915437', 'RFID267385', 'RFID829146', 'RFID503299', 'RFID149865', 'RFID382634', 'RFID671599', 'RFID294087']
infos = ['High-quality screws for various applications.', 'Durable hammers with rubber grip handles.', 'Professional-grade pliers set with multiple types.', 'Versatile wrenches for mechanical work.', 'Assorted nuts for fastening purposes.', 'Sturdy bolts in different sizes and materials.', 'Powerful drills with adjustable speed.', 'Precise saws for woodworking projects.', 'Reliable rivets for heavy-duty connections.', 'Sharp chisels for carving and shaping.', 'Comprehensive socket set with various sizes.', 'Adhesive tapes for securing and marking.', 'Temperature-adjustable soldering irons for electronics work.', 'Assorted files for smoothing and shaping surfaces.', 'Precision tweezers for delicate tasks.', 'Protective gloves for safe handling.', 'Accurate measuring tapes for length measurement.', 'Durable cutting discs for metal and masonry.', 'Welding masks with adjustable shades for eye protection.', 'Strong clamps for holding workpieces.']
quantities = [25, 50, 10, 75, 30, 15, 60, 5, 40, 20, 35, 42, 18, 28, 10, 75, 50, 15, 23, 8]
item_flag = len(product_names)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print("Connection failed")


client = mqtt.Client()
client.on_connect = on_connect

broker_address = "mqtt.eclipseprojects.io"
client.connect(broker_address)

def send_item_data():
    index = randint(0, item_flag - 1)  # Corrected index generation
    item_data = {
        "product_name": product_names[index],
        "product_id": product_ids[index],
        "rfid_tag_id": rfid_tag_ids[index],
        "product_details": product_names[index],
        "description": infos[index],
        "quantity": quantities[index]
    }
    message = json.dumps(item_data)
    topic = "item"
    client.publish(topic, message)
    print(message)


while True:
    user_input = input("Press Enter to an scan item")
    if user_input == "":
        send_item_data()
    else:
        break
