import json
import requests

# ---- AJUSTADO A LA RED DEL GRUPO 07 (puerto 58002) ----
api_url = "http://localhost:58002/api/v1/network-device"

# IMPORTANTE: pegar aqui el serviceTicket que devuelve 01_get-ticket.py
headers = {"X-Auth-Token": "PEGAR_TOKEN_DEL_SCRIPT_01"}

resp = requests.get(api_url, headers=headers)

print("Request status: ", resp.status_code)

response_json = resp.json()
print()
print()
print(response_json)
print()
print()
networkDevices = response_json["response"]

for networkDevice in networkDevices:
    print(networkDevice["hostname"], "\t", networkDevice["platformId"], "\t", networkDevice["managementIpAddress"])
