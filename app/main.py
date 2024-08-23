import requests
import certifi
import json
#url = "https://iicapi.mic.gov.in/api/getApprovedInstitute?per_page=13186"
url="https://iic.mic.gov.in/council-detail/IC202431360"
payload = {}
headers = {    'User-Agent': 'Chrome/92.0.4515.107'}

response = requests.request("GET", url, headers=headers, data=payload,verify=False)

print(response.text)
