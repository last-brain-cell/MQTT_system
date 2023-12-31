# MQTT RFID Data Collection and Processing

This repository contains Python scripts for collecting and processing RFID data using MQTT (Message Queuing Telemetry Transport) protocol. The collected data can be stored in both MongoDB and CSV files for further analysis and usage.

## Features

- Collects RFID data (location and item information) through MQTT messages.
- Stores the collected data in both MongoDB and CSV files.
- Provides random sample data for demonstration purposes.

## Requirements

- Python 3.6 or higher [Python Installation]()
- Dependencies: pandas, pymongo, paho-mqtt
- MQTT broker (used: mqtt.eclipseprojects.io)
- MQTT broker website link [eclipseprojects](https://mqtt.eclipseprojects.io/)

## Installation

Certainly! Here are instructions you can include in your README file to guide users on installing Python 3.6 or higher on both Mac OS and Windows:

---

# Installing Python

This project requires Python 3.6 or higher to run. Follow the instructions below to install Python on both Mac OS and Windows.

## Mac OS

Follow these steps to install Python on Mac OS:

1. **Check if Python is Installed:**
   - Open a terminal window.
   - Check if Python is already installed by running:
     ```
     python3 --version
     ```
   - If Python is not installed, you will see a message like "Python not found."

2. **Install Homebrew (Optional):**
   - If you don't have Homebrew installed, you can install it. Homebrew is a package manager that makes it easy to install various software packages, including Python.
   - To install Homebrew, open a terminal and run the following command:
     ```
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
     ```

3. **Install Python:**
   - Use Homebrew to install Python:
     ```
     brew install python@3.11
     ```

4. **Verify Installation:**
   - After installation, verify that Python is installed correctly by running:
     ```
     python3 --version
     ```

## Windows

Follow these steps to install Python on Windows:

1. **Download Python Installer:**
   - Visit the official Python website at [python.org](https://www.python.org/downloads/windows/) to download the latest Python installer for Windows.

2. **Run the Installer:**
   - Double-click the downloaded installer (e.g., `python-3.11-amd64.exe`) to run it.

3. **Configure Python Installation:**
   - Check the box that says "Add Python [version] to PATH" during installation. This step is crucial for accessing Python from the command prompt.

4. **Complete Installation:**
   - Follow the installation prompts, and Python will be installed on your Windows system.

5. **Verify Installation:**
   - After installation, open a Command Prompt and verify that Python is installed correctly by running:
     ```
     python --version
     ```

## Verify Python Installation

You can verify that Python is correctly installed by checking the version using the commands mentioned above. If you see the Python version displayed without errors, you have successfully installed Python.

## Installing Python Dependencies

Please note that Python versions and installation steps might change over time. It's recommended to refer to the official Python documentation for the most up-to-date instructions:

- [Python Downloads](https://www.python.org/downloads/)
- [Installing Python on Mac](https://docs.python.org/3/using/mac.html)
- [Installing Python on Windows](https://docs.python.org/3/using/windows.html)

Make sure to adapt these instructions to any specific changes in the Python installation process.

## Project Setup

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

Certainly! Below are instructions you can include in your README file to guide users on setting up and configuring a local MongoDB database on both Mac OS and Windows:

---

# Setting Up and Configuring a Local MongoDB Database

To store and manage RFID data, this project uses MongoDB, a popular NoSQL database. Here are instructions on how to set up and configure a local MongoDB database on both Mac OS and Windows.

## Mac OS

Follow these steps to set up MongoDB on Mac OS:

1. **Install MongoDB:**
   - Open a terminal window.
   - Use the following command to install MongoDB using Homebrew:
     ```
     brew tap mongodb/brew
     brew install mongodb-community@5.0
     ```

2. **Start MongoDB:**
   - Run the following command to start the MongoDB service:
     ```
     brew services start mongodb/brew/mongodb-community
     ```

3. **Access MongoDB:**
   - MongoDB will be running on `localhost:27017`.
   - You can access the MongoDB shell by running:
     ```
     mongo
     ```

## Windows

Follow these steps to set up MongoDB on Windows:

**This is a direct installation link for installing MongoDB as well as MongoDB compass - [Click to install](https://fastdl.mongodb.org/osx/mongodb-macos-arm64-7.0.1.tgz)**

1. **Download and Install MongoDB:**
   - Download the MongoDB installer for Windows from the official website.
   - Run the installer and follow the installation prompts.
   - Make sure to choose the option to install MongoDB as a service.

2. **Configure MongoDB Path:**
   - After installation, add the MongoDB binaries directory to your system's PATH environment variable. This step is essential for using MongoDB commands from the command prompt.
   - The default installation path is typically: `C:\Program Files\MongoDB\Server\[version]\bin`.

3. **Start MongoDB:**
   - Open a Command Prompt as Administrator.
   - Start the MongoDB service by running:
     ```
     net start MongoDB
     ```

4. **Access MongoDB:**
   - MongoDB will be running on `localhost:27017`.
   - To access the MongoDB shell, open a Command Prompt and run:
     ```
     mongo
     ```

## Verify MongoDB Installation

You can verify that MongoDB is correctly installed by accessing the MongoDB shell. Open a terminal or Command Prompt and run `mongo`. If the MongoDB shell starts without errors, you have successfully installed MongoDB.

## Configure Project to Use Local MongoDB

In the `subscribe_process_publish.py` script, the local MongoDB connection URL is already set to `"mongodb://127.0.0.1:27017/"`. Make sure this matches your MongoDB configuration.

---

Please note that MongoDB versions and installation steps might change over time. It's recommended to refer to the official MongoDB documentation for the most up-to-date instructions:

- [Install MongoDB on Mac OS](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)
- [Install MongoDB on Windows](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/)

Make sure to adapt these instructions to any specific changes in the MongoDB installation process.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project was inspired by the need for efficient RFID data collection and processing using MQTT.

---

Please replace placeholders like `your-username`, add any additional information, and customize the README according to your project's specifics.
