import io
import os

from google.cloud import vision
client = vision.ImageAnnotatorClient()
filename = os.path.abspath("./demo-img.jpg")

with io.open(filename, "rb") as image_file:
    content = image_file.read()

image = vision.Image(content=content)
response = client.label_detection(image=image)  
labels = response.label_annotations

print("Labels : ")    
for label in labels:
    print(label.description)