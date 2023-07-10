import requests
import io
import os
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

image_bytes = query({
    "inputs": "a photo of an Beard Muscled Ape",
})

# You can access the image with PIL.Image for example
image = Image.open(io.BytesIO(image_bytes))

# Save the image to a file
image.save('output_image.jpg', 'JPEG')
