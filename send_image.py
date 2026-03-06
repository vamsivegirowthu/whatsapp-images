import os
import time
from datetime import datetime
from twilio.rest import Client

# Twilio credentials from Railway variables
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

# Image URLs
images = {
    "1": "https://demo.twilio.com/owl.png",
    "2": "https://images.unsplash.com/photo-1517849845537-4d257902454a",
    "3": "https://images.unsplash.com/photo-1546182990-dffeafbe841d"
}

# Select image
image_url = images["1"]

# Phone numbers
phone_numbers = [
    "+917032455410",
    "+918501830360"
]

# Schedule time → 10:20 AM
schedule_hour = 4
schedule_minute = 50

sent_today = False

print("Scheduler started...")

while True:

    now = datetime.now()

    print("Current time:", now.strftime("%H:%M:%S"))

    # Send message at 10:20 AM
    if now.hour == schedule_hour and now.minute == schedule_minute and not sent_today:

        print("Sending WhatsApp messages...")

        for phone in phone_numbers:
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                media_url=[image_url],
                body="Scheduled Reminder",
                to='whatsapp:' + phone
            )

            print("Sent to:", phone)

        sent_today = True

    # Reset next day
    if now.hour == 0 and now.minute == 1:
        sent_today = False

    time.sleep(20)
