import requests
import json

while True:
    url = "http://192.168.1.6/api/products"

    payload = json.dumps([
    {
        "title": "Awesome Socks",
        "sku": "SCK-4517",
        "barcodes": 7410852096327,
        "description": "Varias coisas sobre o item.....",
        "attributes": [
        {
            "name": "color",
            "value": "red"
        },
        {
            "name": "size",
            "value": "37-42"
        }
        ],
        "price": 89.99
    }
    ])
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)