from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import os
import time

'''
Authenticate
Authenticates your credentials and creates a client.
'''


computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))


# Get image path
read_image_path = os.path.join ("/home/wafaa/image", "image.jpg")
# Open the image
read_image = open(read_image_path, "rb")

# Call API with URL and raw response (allows you to get the operation location)
read_response = computervision_client.read_in_stream(read_image,  raw=True)

# Get the operation location (URL with an ID at the end) from the response
read_operation_location = read_response.headers["Operation-Location"]
# Grab the ID from the URL
operation_id = read_operation_location.split("/")[-1]

# Call the "GET" API and wait for it to retrieve the results 
while True:
    read_result = computervision_client.get_read_result(operation_id)
    if read_result.status not in ['notStarted', 'running']:
        break
    time.sleep(1)
print(read_result.analyze_result.read_results[0].lines[0].text)
