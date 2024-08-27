import os
import smtplib
import time

email_1 = "tiboma08@gmail.com"
password_1 = "nfvg wtar froi kmte"
email_2 = "tiboma08@yahoo.com"

destination_ip = ""
location = ""
description = ""
service = "stopped"
status = "offline"
unreachable_count = 0

def update_config():
    global destination_ip
    global location
    global description
    global service
    global status

    description = input("Enter the description of the device: ")
    destination_ip = input("Enter the destination IP address: ")
    location = input("Enter device location: ")
    create_bat_file()


update_config()

def create_bat_file():
    with open(f"{description}.bat", "w") as file:
        file.writelines(f"ping {destination_ip} -n 10 > {description}.txt")


os.startfile(f"{description}.bat")
time.sleep(15)
offline = True
online = False
with open(f"{description}.txt", "r") as file:
    data = file.readlines()
    for _ in data:
        if "unreachable" in _:
            unreachable_count += 1
    print(unreachable_count)

if unreachable_count > 3:
    offline = True
    online = False
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email_1, password=password_1)
        connection.sendmail(
            from_addr=email_1,
            to_addrs=email_2,
            msg=f"Subject: Attention!!! Device offline\n\n{description} at {location} with IP: {destination_ip} is offline"
        )
elif unreachable_count == 0:
    offline = False
    online = True
    status = "online"




