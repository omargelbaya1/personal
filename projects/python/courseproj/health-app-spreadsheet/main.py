#CURRENTLY, RUN THIS CODE THROUGH THE TERMINAL E.G. PYTHON3 MAIN.PY, the play button isnt working right now!






import requests
import datetime as dt
import os


APP_ID=os.environ["APP_ID"]
API_KEY=os.environ["API_KEY"]
TOKEN=os.environ["TOKEN"]


headers={
"x-app-id": APP_ID,
"x-app-key": API_KEY
}

response=requests.get("https://app.100daysofpython.dev/healthz",headers=headers)

exercise_input=input("Tell me which exercise you did today")

parameters={
  "query": exercise_input,
  "weight_kg": 140,
  "height_cm": 183,
  "age": 28,
  "gender": "male"
}



calorie_burned=requests.post("https://app.100daysofpython.dev/v1/nutrition/natural/exercise",headers=headers,json=parameters)
calorie_burned.raise_for_status()

data= calorie_burned.json()


current_day=dt.datetime.now().strftime("%d/%m/%Y")
current_time=dt.datetime.now().strftime("%H:%M:%S")
name_of_exercise=data["exercises"][0]["name"]
duration=data["exercises"][0]["duration_min"]
calories=data["exercises"][0]["nf_calories"]





#it will not work if you put [] array brackets around the parameters_sheety parameters.
parameters_sheety={
  "workout":
    {
      "date":current_day,
      "time": current_time,
      "exercise": name_of_exercise,
      "duration": duration,
      "calories": calories,
      "id": 3
    }

}

headers={

"Authorization":f"Basic {TOKEN}"
}



sheety_response=requests.post("https://api.sheety.co/f878894ca96eedd8055b5a328db0a5d3/myWorkouts/workouts",json=parameters_sheety,headers=headers)
sheety_response.raise_for_status()
print(sheety_response.text)
print(sheety_response.json())


# sheety_get=requests.get("https://api.sheety.co/f878894ca96eedd8055b5a328db0a5d3/myWorkouts/workouts")
# sheety_get.raise_for_status()
# print(sheety_get.json())
# print(sheety_get.text)
