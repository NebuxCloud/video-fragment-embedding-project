import torch
import glob
import os
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

# Load the CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def get_image_embeddings(image_path):
    # Load and process the image
    image = Image.open(image_path)
    inputs = processor(images=image, return_tensors="pt")

    # Calculate image embeddings
    with torch.no_grad():
        embeddings = model.get_image_features(**inputs)

    return embeddings

def get_text_embedding(text):
    # Process the text to get its embedding
    inputs = processor(text=[text], return_tensors="pt")

    # Calculate text embeddings
    with torch.no_grad():
        text_embedding = model.get_text_features(**inputs)

    return text_embedding

# Get the user's text query
text_query = input("Enter the text to search for: ").strip()
text_embedding = get_text_embedding(text_query)

# Dictionary to store similarities for each image
similarities_by_image = {}

# Iterate over all image embedding files
for embedding_path in glob.glob("data/*/*.pt"):
    # Load the image embeddings
    image_embedding = torch.load(embedding_path)

    # Calculate similarity between text and image embeddings
    similarity = torch.nn.functional.cosine_similarity(text_embedding, image_embedding).item()

    # Store the similarity with the full image path
    image_path = embedding_path.replace(".pt", ".png")
    similarities_by_image[image_path] = similarity

# Sort images by similarity in descending order
sorted_images = sorted(similarities_by_image.items(), key=lambda x: x[1], reverse=True)

# Print the most similar images
print("\nTop matching images:")
for image_path, similarity in sorted_images[:10]:  # Shows the top 10 most similar images
    print(f"{image_path}: Similarity {similarity}")
