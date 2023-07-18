import requests
from fastapi import FastAPI
import json
import os

app = FastAPI()

#global vars
AZURE_IP = "52.136.121.3"
CLOUDFLARE_KEY = os.getenv('CLOUDFLARE_API_KEY')
CLOUDFLARE_KEY = "Bearer " + CLOUDFLARE_KEY

@app.post("/lucianp2dr")
def lucian2dr():
    cloudflare_update_ip(AZURE_IP)
    return {"Status": "ok"}

def cloudflare_update_ip(ip):
    url = "https://api.cloudflare.com/client/v4/zones/8f612a45af1f3d85a05811bff7029e38/dns_records/59d336301fdcea0e55ffdcaabb1aba18"

    payload={
        "content": ip,
        "name": "lucianp.com",
        "type": "A"
    }
    headers = {
        'Authorization': CLOUDFLARE_KEY,
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=json.dumps(payload))

    print(response.text)
