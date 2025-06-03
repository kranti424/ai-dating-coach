from fastapi import FastAPI, BackgroundTasks
from twilio.rest import Client
import os

app = FastAPI()
twilio_client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

def send_sms_async(to: str, body: str):
    twilio_client.messages.create(
        body=body,
        from_=os.getenv("TWILIO_NUMBER"),
        to=to
    )

@app.post("/notify")
async def notify_user(phone: str, message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_sms_async, phone, message)
    return {"status": "Notification queued"}