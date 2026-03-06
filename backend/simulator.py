import requests
import random
import time

API = "http://127.0.0.1:8000/ingest"

events = [
    "speeding",
    "harsh_braking",
    "drowsiness",
    "normal"
]

print("Starting Dashcam Simulator...")

while True:

    payload = {
        "driver_id": "DRIVER_001",
        "event_type": random.choice(events),
        "value": random.uniform(60,110)
    }

    try:
        requests.post(API, json=payload)
        print("Event Sent:", payload)
    except:
        print("Backend not running")

    time.sleep(random.uniform(2,3))