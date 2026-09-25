import requests
from PIL import Image
from io import BytesIO

def download_image(image_url):
    response = requests.get(image_url, timeout=10)

    if response.status_code != 200:
      raise Exception("Could not download image")
      image = Image.open(BytesIO(response.content))

    return image
      

