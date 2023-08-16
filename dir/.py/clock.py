import datetime
import pytz
import requests
import json
import os
import time
from keepalive import keep_alive


integer = {
    "01": "1110001 1010001 1010001 1010001 1110001",
    "02": "1110111 1010001 1010111 1010100 1110111",
    "03": "1110111 1010001 1010111 1010001 1110111",
    "04": "1110101 1010101 1010111 1010001 1110001",
    "05": "1110111 1010100 1010111 1010001 1110111",
    "06": "1110111 1010100 1010111 1010101 1110111",
    "07": "1110111 1010001 1010001 1010001 1110001",
    "08": "1110111 1010101 1010111 1010101 1110111",
    "09": "1110111 1010101 1010111 1010001 1110111",
    "10": "0010111 0010101 0010101 0010101 0010111",
    "11": "0010001 0010001 0010001 0010001 0010001",
    "12": "0010111 0010001 0010111 0010100 0010111",
    "13": "0010111 0010001 0010111 0010001 0010111",
    "14": "0010101 0010101 0010111 0010001 0010001",
    "15": "0010111 0010100 0010111 0010001 0010111",
    "16": "0010111 0010100 0010111 0010101 0010111",
    "17": "0010111 0010001 0010001 0010001 0010001",
    "18": "0010111 0010101 0010111 0010101 0010111",
    "19": "0010111 0010101 0010111 0010001 0010111",
    "20": "1110111 0010101 1110101 1000101 1110111",
    "21": "1110001 0010001 1110001 1000001 1110001",
    "22": "1110111 0010001 1110111 1000100 1110111",
    "23": "1110111 0010001 1110111 1000001 1110111",
    "24": "1110101 0010101 1110111 1000001 1110001",
    "25": "1110111 0010100 1010111 1010001 1110111",
    "26": "1110111 0010100 1010111 1010101 1110111",
    "27": "1110111 0010001 1010001 1010001 1110001",
    "28": "1110111 0010101 1010111 1010101 1110111",
    "29": "1110111 0010101 1010111 1010001 1110111",
    "30": "0010111 0010101 0010101 0010101 0010111",
    "31": "0010001 0010001 0010001 0010001 0010001",
    "32": "0010111 0010001 0010111 0010100 0010111",
    "33": "0010111 0010001 0010111 0010001 0010111",
    "34": "0010101 0010101 0010111 0010001 0010001",
    "35": "0010111 0010100 0010111 0010001 0010111",
    "36": "0010111 0010100 0010111 0010101 0010111",
    "37": "0010111 0010001 0010001 0010001 0010001",
    "38": "0010111 0010101 0010111 0010101 0010111",
    "39": "0010111 0010101 0010111 0010001 0010111",
    "40": "1110111 0010101 1110101 1000101 1110111",
    "41": "1110001 0010001 1110001 1000001 1110001",
    "42": "1110111 0010001 1110111 1000100 1110111",
    "43": "1110111 0010001 1110111 1000001 1110111",
    "44": "1110101 0010101 1110111 1000001 1110001",
    "45": "1110111 0010100 1010111 1010001 1110111",
    "46": "1110111 0010100 1010111 1010101 1110111",
    "47": "1110111 0010001 1010001 1010001 1110001",
    "48": "1110111 0010101 1010111 1010101 1110111",
    "49": "1110111 0010101 1010111 1010001 1110111",
    "50": "0010111 0010101 0010101 0010101 0010111",
    "51": "0010001 0010001 0010001 0010001 0010001",
    "52": "0010111 0010001 0010111 0010100 0010111",
    "53": "0010111 0010001 0010111 0010001 0010111",
    "54": "0010101 0010101 0010111 0010001 0010001",
    "55": "0010111 0010100 0010111 0010001 0010111",
    "56": "0010111 0010100 0010111 0010101 0010111",
    "57": "0010111 0010001 0010001 0010001 0010001",
    "58": "0010111 0010101 0010111 0010101 0010111",
    "59": "0010111 0010101 0010111 0010001 0010111",
    "60": "1110111 0010101 1110101 1000101 1110111"
}

webhook_url = my_secret = os.environ['URL']
message_id = "1141466319162708041"

def split_variable(string):
    lines = string.split("\n")
    return lines

def update_webhook_message(url, message_id, new_content):
    webhook_url = f"{url}/messages/{message_id}"
    data = {
        "content": new_content
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.patch(webhook_url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        print("Webhook message updated successfully.")
    else:
        print("Failed to update webhook message.")

def get_clock():
    result = ""
    tz = pytz.timezone('Europe/Berlin') # Zeitzone Berlin
    berlin_now = datetime.datetime.now(tz) # aktuelle Zeit in Berlin
    m = berlin_now.strftime("%M") # Minuten
    h = berlin_now.strftime("%H") # Stunden
    print(h+":"+m)

    h = integer[str(h)]
    h = h.replace(" ", "\n")
    h = h.replace("1", "⬜")
    h = h.replace("0", "⬛")
    h = split_variable(h)

    m = integer[str(m)]
    m = m.replace(" ", "\n")
    m = m.replace("1", "⬜")
    m = m.replace("0", "⬛")
    m = split_variable(m)

    for i in range(0, 5):
        hour = h[i]
        minute = m[i]
        result += f"{hour}    {minute}\n"

    print(result)
    return(result + "**JustWait 2023**")

#timrzone = ['Europe/Paris', 'Africa/Kampala', 'Asia/Colombo', 'Asia/Riyadm', 'Africa/Luanda', 'Europe/Vienna', 'Asia/Calcutta', 'Asia/Dubai','Europe/London']

while True:
  update_webhook_message(webhook_url, message_id, get_clock())
  time.sleep(60)

keep_alive()