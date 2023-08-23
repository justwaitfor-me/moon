import requests
import json

webhook_url = "https://ptb.discord.com/api/webhooks/1143094729567916064/OF9Nk3s0MvdT4lkCjeduIGbbSVi3n_DsT8RURtUR6y9e7x1tLfk0AIcIjL893nvCPQu9"

options = [
    {
        "label": "Option 1",
        "value": "option1"
    },
    {
        "label": "Option 2",
        "value": "option2"
    },
    {
        "label": "Option 3",
        "value": "option3"
    }
]

dropdown_menu = {
    "type": 1,
    "components": [
        {
            "type": 3,
            "custom_id": "dropdown",
            "options": options
        }
    ]
}

payload = {
    "content": "Select an option:",
    "components": [dropdown_menu]
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

print(response.status_code)