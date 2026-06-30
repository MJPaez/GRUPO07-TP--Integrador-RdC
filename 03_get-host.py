import json
import requests

# ---- AJUSTADO A LA RED DEL GRUPO 07 (puerto 58002) ----
api_url = "http://localhost:58002/api/v1/host"

# IMPORTANTE: pegar aqui el serviceTicket que devuelve 01_get-ticket.py
headers = {"X-Auth-Token": "PEGAR_TOKEN_DEL_SCRIPT_01"}

resp = requests.get(api_url, headers=headers, verify=False)

print("Request status: ", resp.status_code)

response_json = resp.json()
print(response_json)
print()
print()
hosts = response_json["response"]

for host in hosts:
    print(host["hostName"], "\t", host["hostIp"], "\t", host["hostMac"], "\t", host["connectedInterfaceName"])
