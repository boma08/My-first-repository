import requests
import datetime as dt

response = requests.get(url="http://api.open-notify.org/iss-now.json")  # returns the request code, not the actual data
print(response)
print(response.status_code)

if response.status_code == 404:
    raise Exception("That resource does not exist.")
elif response.status_code == 401:
    raise Exception("You are not authorised to access this data")

# the Request module can be used instead to generate exceptions when a get request returns an error with
# the exact HTTP Error code and meaning

response.raise_for_status()
data = response.json()  # returns a dictionary whose content is the actual data from the get request
# which can be manipulated as below
print(data)
print(data["iss_position"])
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
print(response.json()["timestamp"])

iss_position = (longitude, latitude)  # creates a tuple
print(iss_position)

parameters = {
    "lat": latitude,
    "lng": longitude,
    "formatted": 0
}
response_2 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response_2.raise_for_status()
data_2 = response_2.json() # returns a dictionary
print(data_2)
sunrise = data_2["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data_2["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

print(dt.datetime.now().hour)
