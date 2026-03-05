import os
import time
from datetime import datetime
from twilio.rest import Client

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

# 3 image URLs
images = {
    "1": "https://demo.twilio.com/owl.png",
    "2": "https://images.unsplash.com/photo-1517849845537-4d257902454a",  # dog
    "3": "https://images.unsplash.com/photo-1546182990-dffeafbe841d"       # lion
}

# Select image
image_url = images["1"]

# Multiple phone numbers
phone_numbers = [
    "+917032455410",
    "+918501830360"
]

# Schedule time (5:43 PM = 17:43)
schedule_time = "23:30"

print("Waiting for scheduled time...")

while True:
    current_time = datetime.now().strftime("%H:%M")

    if current_time == schedule_time:

        for phone in phone_numbers:
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                media_url=[image_url],
                body="Scheduled Reminder",
                to='whatsapp:' + phone
            )

            print("Sent to:", phone)

        break

    time.sleep(20)



    

