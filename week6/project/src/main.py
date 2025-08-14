from weather_api import get_weather
from email_sender import send_email
from log.log import setup_logger
import schedule
import time
import json
import logging
from dotenv import load_dotenv
from datetime import datetime

# env
load_dotenv()
setup_logger()
logging.info("Weather Notifier starting up...")

def job():
    """
    One scheduled job run: fetch weather and email recipients.

    Includes try/except to keep the scheduler running even if something fails.
    """
    logging.info(f"Job started at {datetime.now().isoformat()} — Fetching weather...")
    try:
        city, temp, condition = get_weather()
        if temp is None:
            logging.error(f"Could not fetch weather for {city}. See earlier logs.")
            return

        message = f"""Hi there!\nHere's the weather update for {city}:\nTemperature: {temp}°C\nCondition: {condition}\nHave a great day!"""

        with open("config.json") as f:
            config = json.load(f)
            recipients = config.get("recipients", [])
        for email in recipients:
            success = send_email(email, f"Weather Update for {city}", message)
            if success:
                logging.info(f"Email sent to {email}")
            else:
                logging.error(f"Failed to send email to {email}")
    except Exception as e:
        # try keeps risky code; except handles errors so automation doesn't crash.
        logging.error(f"Unexpected error in job: {e}")
    finally:
        logging.info("Job completed.")

#schedule time/ need to change schedule time
def run_notifier(interval_minutes: int = 1):
    """
    Start the scheduling loop for the weather notifier.
    The loop is simple and readable; logs show progress over time.
    """
    schedule.every(interval_minutes).minutes.do(job)
    logging.info(f"Scheduler started. Running every {interval_minutes} minute(s).")
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    run_notifier(interval_minutes=1)
