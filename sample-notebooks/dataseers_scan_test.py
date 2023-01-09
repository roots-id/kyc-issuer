import requests
import os
from pprint import pprint as pp
import base64
from PIL import Image
import io
import bytes

dataseers_api_key = os.environ["DATASEERS_API_KEY"]

url = "https://demo.dataseers.ai/services/v2/seerscan"
payload = {
    "first_name": "Rodolfo",
    "last_name": "Miranda",
    "email": "rodolfo.miranda@gmail.com",
#     "contact_number": "3054874445",
# #      "ssn": "123123",
#     "address_1": "2105 NW 102nd Ave",
#     "city": "Doral",
#     "state": "FL",
#     "zip": "33172",
    "flow_id": "001714",
    "processor_id": "5187",
    "type": "DocOnly"
}




# selfie = base64.b64encode(open('/Users/rodo/Desktop/dni.jpg', 'rb').read())
# base64_utf8_str = base64.b64encode(selfie).decode('utf-8')
# b64_bytes = base64.b64decode(base64_utf8_str)
# b64_buffer = io.BufferedReader(io.BytesIO(b64_bytes))
# img4 = Image.open(io.BytesIO(base64.decodebytes(b64_bytes)))
# img4.save('/Users/rodo/Desktop/dni3.jpg' )


# selfie = base64.b64encode(open('/Users/rodo/Desktop/dni.jpg', 'rb').read())
# base64_utf8_str = base64.b64encode(selfie).decode('utf-8')
# f = open("/Users/rodo/Desktop/b64_real.txt", "w")
# f.write(base64_utf8_str)
# f.close()


# print(type(base64_utf8_str))

# print(type(b64_bytes))

# print(type(b64_buffer))
#img3 = io.BufferedReader(io.BytesIO(dataurl))
# img3 = Image.open(b64_buffer, formats=["JPEG"],mode="r")
# img3 = Image.open('/Users/rodo/Desktop/dni.jpg')
# img3.save('/Users/rodo/Desktop/dni2.jpg' )


f = open("/Users/rodo/Desktop/b64.txt", "rb")
b64_bytes = f.read()
print(b64_bytes[1:5000])
# print(type(b64str))
# print(b64_bytes[1:5000])
# b64_bytes = base64.urlsafe_b64decode(b64str)
# print(b64_bytes[1:5000])
b64_buffer = io.BufferedReader(io.BytesIO(b64_bytes))


img4 = Image.open(io.BytesIO(base64.decodebytes(b64_bytes)))
img4.save('/Users/rodo/Desktop/dni3.jpg' )


# f2 = open("/Users/rodo/Desktop/b64.txt", "r")
# b64_str2 = f2.read()
# bg4_bytes2 = bytearray.fromhex(b64_str2)
# print(bg4_bytes2[1:5000])


# exit(1)



files = {
    "front": open('/Users/rodo/Desktop/dni3.jpg', 'rb'),
    "selfie": open('/Users/rodo/Desktop/dni3.jpg', 'rb')

}
headers = {
    'api-key': dataseers_api_key}

session = requests.Session()
resp = session.post(url,headers=headers,data=payload, files=files)
print(resp.text)
print(resp.status_code)
pp(resp.json()["result"])
print("-------------------------------------")
pp(resp.json()["failure_reasons"])
print("-------------------------------------")

pp(resp.json()["verification_summary"])
print("-------------------------------------")

pp(resp.json()["document_summary"])
print("-------------------------------------")

pp(resp.json()["image_metrics_result"])
print("-------------------------------------")


# selfie = encoded_string = base64.b64encode(open('/Users/rodo/Desktop/dataseers.png', 'rb').read())
# # img1 = base64.decodebytes(selfie)


# picture = open('/Users/rodo/Desktop/dataseers.png', 'rb')
# print(picture.read())

# base64.decodebytes(selfie)