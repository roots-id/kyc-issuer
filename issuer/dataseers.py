import requests
import os
import base64
from PIL import Image
import io



async def seersScan(personal_info, selfie:str, front:str):
    
    dataseers_api_key = os.environ["DATASEERS_API_KEY"]


    f = open("b64_temp.txt", "w")
    f.write(selfie)
    f.close()

    f = open("b64_temp.txt", "rb")
    b64_bytes = f.read()
    f.close()
    img = Image.open(io.BytesIO(base64.decodebytes(b64_bytes)))
    img.save('selfie_temp.jpg' )

    f = open("b64_temp.txt", "w")
    f.write(front)
    f.close()

    f = open("b64_temp.txt", "rb")
    b64_bytes = f.read()
    f.close()
    img = Image.open(io.BytesIO(base64.decodebytes(b64_bytes)))
    img.save('front_temp.jpg' )

    
    url = "https://demo.dataseers.ai/services/v2/seerscan"
    payload = {
        "first_name": personal_info["first_name"],
        "last_name": personal_info["last_name"],
        "email": personal_info["email"],
        "flow_id": "001714",
        "processor_id": "5187",
        "type": "DocOnly"
    }
    files = {
    "front": open('front_temp.jpg', 'rb'),
    "selfie": open('selfie_temp.jpg', 'rb'),

    }
    headers = {
        'api-key': dataseers_api_key}

    session = requests.Session()
    resp = session.post(url,headers=headers,data=payload, files=files)



    return resp.json()





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