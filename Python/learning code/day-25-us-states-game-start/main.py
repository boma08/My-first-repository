import requests

parameter = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get("https://opentdb.com/api_config.php", params=parameter)
response.raise_for_status()
data = response.json()
print(data)

