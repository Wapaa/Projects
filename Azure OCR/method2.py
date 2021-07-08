import requests
import subprocess
import sys
from io import BytesIO


api_url=endpoint+'/vision/v3.0/ocr'

header = {'Ocp-Apim-Subscription-Key': Subscription_key,
          'Content-Type': 'application/octet-stream'}
          
params = {'language': 'en'}

try:
    
    path_to_file = "/home/wafaa/images/image.jpg"

   # Read file
    with open(path_to_file, 'rb') as f:
         data = f.read()
 

    r = requests.post(api_url,
                      params=params,
                      headers=header,
                      data=data)

    r.raise_for_status()

    data = r.json()
    print(data)

except Exception as e:
    print('Error occurred: {}'.format(e), file=sys.stderr)
    
    
