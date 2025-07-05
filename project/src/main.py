from weather_api import get_weather
from email_sender import send_email
from log.log import setup_logger
import schedule
import time
import json
import logging
from dotenv import load_dotenv

# env
load_dotenv()
setup_logger()

def job():
    try:
        city, temp, condition = get_weather()
        if temp is None:
            logging.error(f"Failed to fetch info for {city}")
            return
        
        message = f"""Hi there!\nHere’s the weather update for {city}:\nTemperature: {temp}°C\nCondition: {condition}\nHave a great day!"""

        with open("config.json") as f:
            config = json.load(f)
            recipients = config.get("recipients", [])
        for email in recipients:
            send_email(email, f"Weather Update for {city}", message)
            logging.info(f"Email sent to {email}")
    except Exception as e:
        logging.error(f"Error occurred: {e}")

#schedule time/ need to change schedule time
schedule.every(1).minutes.do(job)

print("successfully run.")

while True:
    schedule.run_pending()
    time.sleep(60)
