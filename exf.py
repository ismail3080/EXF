import requests
import json

# EdgeX Foundry server configuration
BASE_URL = "http://localhost:48080/api/v1"

# Get all devices
def get_devices():
    url = BASE_URL + "/device"
    response = requests.get(url)
    devices = response.json()
    return devices

# Get a specific device by name
def get_device(device_name):
    url = BASE_URL + "/device/name/" + device_name
    response = requests.get(url)
    device = response.json()
    return device

# Get all readings for a specific device
def get_device_readings(device_name):
    url = BASE_URL + "/reading/device/" + device_name
    response = requests.get(url)
    readings = response.json()
    return readings

# Create a new device
def create_device(device_name):
    url = BASE_URL + "/device"
    headers = {'Content-Type': 'application/json'}
    data = {
        "name": device_name,
        "description": "Sample device",
        "adminState": "UNLOCKED",
        "operatingState": "ENABLED"
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print("Device created successfully.")
    else:
        print("Failed to create device.")

# Main program
def main():
    # Get all devices
    devices = get_devices()
    print("Devices:")
    print(devices)

    # Get a specific device
    device_name = "MyDevice"
    device = get_device(device_name)
    print(f"\nDevice '{device_name}':")
    print(device)

    # Get device readings
    readings = get_device_readings(device_name)
    print(f"\nReadings for device '{device_name}':")
    print(readings)

    # Create a new device
    new_device_name = "NewDevice"
    create_device(new_device_name)

if __name__ == "main":
    main()