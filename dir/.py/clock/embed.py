import requests
import json

def delete_all_messages(webhook_url, channel_id):
    # Nachrichten abrufen
    response = requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages",
                            headers={"Authorization": f"Bot YOUR_BOT_TOKEN"})
    messages = response.json()
    headers = {
        'Content-Type': 'application/json'
    }

    # Nachrichten löschen
    for message in messages:
        message_id = message["id"]
        requests.delete(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}", headers)

# Beispielaufruf
webhook_url = "https://ptb.discord.com/api/webhooks/1143160822282076190/zXI3Ky_bQ5YR-2kFk4HlkMFltFbz7ERORRMyuoEyfFF76-pjUo2CTnAmZnTyE_ZiAqX3"
channel_id = "1143160790862532690"
delete_all_messages(webhook_url, channel_id)