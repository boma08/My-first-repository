device_list = []

def create_device():
    #saves the details of a new device in a dictionary. Returns the device details dictionary
    device_description = input("What kind of device do you want to monitor: ").strip().title().replace(" ","_")
    manufacturer = input("Enter name of manufacturer of the device: ").strip().title()
    ip_address = input("Whats the IP address of the device? ").strip()
    device_location = input("Enter the location of the device eg. Reception: ").strip().title()
    service = "stopped"
    device_status = "offline"

    device_details = {
        "manufacturer": manufacturer,
        "description": device_description,
        "ip address": ip_address,
        "location": device_location,
        "status": device_status,
        "service": service,
    }
    return device_details

def add_device():
    #adds the device details dictionary to the device list
    device_list.append(create_device())






