import requests
from datetime import datetime
import smtplib
import sched, time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_no = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

diff_lat= abs(MY_LAT-iss_latitude)
diff_long=abs(MY_LONG-iss_longitude)
def somthing(scheduler):
    scheduler.enter(60, 1, somthing, (scheduler,) )
    if diff_lat<=5 and diff_long <=5 and (time_now>=sunset_no or time_now<=sunrise):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login("MY_EMAIL", "MY_PASSWORD")
            connection.sendmail(
                from_addr="MY_EMAIL",
                to_addrs="MY_EMAIL",
                msg="Subject:Monday Motivation lookup"
            )
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


my_scheduler = sched.scheduler(time.time, time.sleep)
my_scheduler.enter(60, 1, somthing, (my_scheduler,))
my_scheduler.run()


