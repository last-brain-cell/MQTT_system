# MQTT RFID Data Collection and Processing

This repository contains Python scripts for collecting and processing RFID data using MQTT (Message Queuing Telemetry Transport) protocol. The collected data can be stored in both MongoDB and CSV files for further analysis and usage.

## Features

- Collects RFID data (location and item information) through MQTT messages.
- Stores the collected data in both MongoDB and CSV files.
- Provides random sample data for demonstration purposes.

## Requirements

- Python 3.6 or higher
- Dependencies: pandas, pymongo, paho-mqtt
- MQTT broker (used: mqtt.eclipseprojects.io)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/MQTT_system.git
   cd mqtt-rfid-data-processing
   ```

2. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the `item_publisher.py` script to simulate sending item-related RFID data:

   ```bash
   python item_publisher.py
   ```

   This script sends randomized item data through MQTT messages to the broker.

2. Run the `location_publisher.py` script to simulate sending location-related RFID data:

   ```bash
   python location_publisher.py
   ```

   This script sends randomized location data through MQTT messages to the broker.

3. Run the `subscribe_process_publish.py` script to subscribe to MQTT topics, process received data, and store it in both MongoDB and CSV files:

   ```bash
   python subscribe_process_publish.py
   ```

   This script subscribes to "item" and "location" topics, processes received data, and stores it in the specified MongoDB collection and CSV file.

## Configuration

- Modify the MQTT broker address and other parameters in the scripts if needed.
- Adjust the simulated sample data to match your real-world RFID data.

## License

This project is licensed under the MIT License - see the [LICENSE] file for details.

## Acknowledgements

This project was inspired by the need for efficient RFID data collection and processing using MQTT.

---

Please replace placeholders like `your-username`, add any additional information, and customize the README according to your project's specifics.
