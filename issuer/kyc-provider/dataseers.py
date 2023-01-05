import requests
import os


async def seersScan(personal_info, selfie, front, flow_id, processor_id, type):
    
    dataseers_api_key = os.environ["DATASEERS_API_KEY"]
    
    url = "https://demo.dataseers.ai/services/v2/seerscan"
    payload = {
        "first_name": personal_info["first_name"],
        "last_name": personal_info["last_name"],
        "contact_number": personal_info["contact_number"],
        "ssn": personal_info["ssn"],
        "address_1": personal_info["address_1"],
        "city": personal_info["city"],
        "state": personal_info["state"],
        "zip": personal_info["zip"],
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
    print(resp.json())





#     curl --location --request POST 'https://demo.dataseers.ai/services/v2/seerscan' \
# --header 'api-key: jysZx7BEi' \
# --form 'first_name="Fernando"' \
# --form 'last_name="Perez"' \
# --form 'contact_number="1061234508"' \
# --form 'ssn="526974860"' \
# --form 'address_1=1657 187TH ST"' \
# --form 'city="Doral"' \
# --form 'state="FL"' \
# --form 'zip="33172"' \
# --form 'front=@"dni.jpg"' \
# --form 'selfie=@"dni.jpg"' \
# --form 'flow_id="001714"' \
# --form 'processor_id="5187"' \
# --form 'type=DocOnly'