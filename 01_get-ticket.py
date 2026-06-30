import json
import requests

# ---- AJUSTADO A LA RED DEL GRUPO 07 (puerto 58002) ----
api_url = "http://localhost:58002/api/v1/ticket"

headers = {
    "content-type": "application/json"
}
# ---- AJUSTADO AL USERNAME/ PASSWORD DEL GRUPO 07 ----
body_json = {
    "username": "admin",
    "password": "cisco123"
}

resp = requests.post(api_url, json.dumps(body_json), headers=headers)

print("Ticket request status: ", resp.status_code)
response_json = resp.json()
print (response_json)
serviceTicket = response_json["response"]["serviceTicket"]

print("The service ticket number is: ", serviceTicket) 
