import requests
from datetime import datetime as dt
import os

APP_ID = "87b6ea63"
API_KEY = "56d26572754d5024787e940b08d21d77"


GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 170
AGE = 34

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/685feef5323451066545525cbf4d0c75/copyOfMyWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = dt.now().strftime("%d/%m/%Y")
now_time = dt.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    # Bearer Token Authentication
    bearer_headers = {
        "Authorization": "Bearer jbbefs9998jlbslkfhslfbg"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(sheet_response.text)