import time
from plyer import notification

def water_reminder():
    while True:
        notification.notify(title="💧Water Reminder for Dhruv kumar", message="Time to sip some!", timeout=10)
        time.sleep(3600)  # Remind every hour

water_reminder()