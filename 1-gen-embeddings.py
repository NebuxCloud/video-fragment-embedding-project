import requests
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import torch
import glob
import os

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def get_image_embeddings(image_path):
    # Load image from the URL
    image = Image.open(image_path)

    # Process the image without text input
    inputs = processor(images=image, return_tensors="pt")

    # Calculate image embeddings
    with torch.no_grad():
        embeddings = model.get_image_features(**inputs)

    return embeddings

# Get all pngs from data/*/*.png
# For each png, get the image embeddings
# Save the embeddings in a file
for image_path in glob.glob("data/*/*.png"):
    # If the image has already been processed, skip it
    if os.path.exists(image_path.replace(".png", ".pt")):
        continue
    image_embeddings = get_image_embeddings(image_path)
    output_path = image_path.replace(".png", ".pt")
    torch.save(image_embeddings, output_path)
    print(f"Saved image embeddings to {output_path}")
