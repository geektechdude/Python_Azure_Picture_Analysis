# geektechstuff

# Python libraries to import
import requests
import matplotlib.pyplot as plt
import json
from PIL import Image
from io import BytesIO

# Requires an active Azure API / Subscription Key
subscription_key = "ENTER SUBSCRIPTION KEY HERE"
assert subscription_key
# Make sure to use the region that matches where your Azure API / Subscription Key is from
endpoint = "https://uksouth.api.cognitive.microsoft.com"
url = endpoint+"/vision/v1.0/analyze?"


def image_analysis():
    image_url = input('Please enter URL of image: ')

    headers = {'Ocp-Apim-Subscription-Key': subscription_key }
    params  = {'visualFeatures': 'Categories,Description,Color'}
    data    = {'url': image_url}
    response = requests.post(url, headers=headers, params=params, json=data)
    response.raise_for_status()
    analysis = response.json()
    image_caption = analysis["description"]["captions"][0]["text"].capitalize()

    # Display the image and overlays it with the caption.
    image = Image.open(BytesIO(requests.get(image_url).content))
    plt.imshow(image)
    plt.axis("off")
    _ = plt.title(image_caption, size="x-large", y=-0.1)

    return(plt.show())
