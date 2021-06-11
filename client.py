from __future__ import print_function
import requests
import json
import cv2

addr = 'http://192.168.8.105:5000' #Ip address of my kali vm and destination port
test_url = addr + '/api/test'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

img = cv2.imread('image.jpg')
# encode image as jpeg
_, img_encoded = cv2.imencode('.jpg', img)
# send http request with image and received response
response = requests.post(test_url, data=img_encoded.tobytes(), headers=headers)
# decode response
print(json.loads(response.text))

