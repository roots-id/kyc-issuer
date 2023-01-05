import requests
import os
from pprint import pprint as pp

dataseers_api_key = os.environ["DATASEERS_API_KEY"]

url = "https://demo.dataseers.ai/services/v2/seerscan"
payload = {
    "first_name": "Rodolfo",
    "last_name": "Miranda",
    "contact_number": "3054874445",
#      "ssn": "123123",
    "address_1": "2105 NW 102nd Ave",
    "city": "Doral",
    "state": "FL",
    "zip": "33172",
    "flow_id": "001714",
    "processor_id": "5187",
    "type": "DocOnly"
}

files = {
    "selfie": open('/Users/rodo/Desktop/dni.jpg', 'rb'),
    "front": open('/Users/rodo/Desktop/dni.jpg', 'rb')
}
headers = {
    'api-key': dataseers_api_key}

session = requests.Session()
resp = session.post(url,headers=headers,data=payload, files=files)
print(resp.status_code)
pp(resp.json()["result"])
pp(resp.json()["failure_reasons"])
pp(resp.json()["verification_summary"])
pp(resp.json()["document_summary"])
pp(resp.json()["image_metrics_result"])


# picture = open('/Users/rodo/Desktop/dni.jpg', 'rb')
# print(picture.read())