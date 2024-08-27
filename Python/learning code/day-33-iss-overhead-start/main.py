import requests
from datetime import datetime
import smtplib
import time

email_1 = "tiboma08@gmail.com"
password_1 = "nfvg wtar froi kmte"
email_2 = "tiboma08@yahoo.com"

MY_LAT = 51.762718 # Your latitude
MY_LONG = -0.224710 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    # If the ISS is close to my current position
    if iss_latitude < MY_LAT + 5 and iss_latitude > MY_LAT - 5 and MY_LONG + 5 > iss_longitude > MY_LONG - 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour_now = time_now.hour

    # and it is currently dark
    if sunset <= hour_now <= sunrise:
        return True
# Then send me an email to tell me to look up.


while True:
    time.sleep(60)  # code will run in the background every 60 seconds
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email_1, password=password_1)
            connection.sendmail(
                from_addr=email_1,
                to_addrs=email_2,
                msg="Subject: ISS within sight!!\n\nGo out, look to the skies for a glimpse of the ISS..."
            )




