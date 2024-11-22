import requests
import config

def send_message(message: str):
  payload = {
    "content": message
  }

  headers = {
    "Content-Type": "application/json"
  }

  requests.post(
    url=config.DISCORD_WEBHOOK_URL,
    headers=headers,
    json=payload,
    timeout=10
  )
