import torch
import glob
from statistics import median

def load_embeddings(file_path):
    return torch.load(file_path)

def compare_embeddings(embedding1, embedding2):
    return torch.nn.functional.cosine_similarity(embedding1, embedding2)

name = "coldplay_viva_la_vida"
fragment = 24

print(f"Comparing fragment {fragment} of video {name} with all other fragments...")
fragment_path = f"data/{name}/fragment_{fragment}.pt"
fragment_embedding = load_embeddings(fragment_path)

distances_by_video = {}

for embedding_path in glob.glob("data/*/*.pt"):
    if embedding_path == fragment_path:
        print("Skipping the same video...")
        continue
    # extract name
    name = embedding_path.split("/")[1]

    embedding = load_embeddings(embedding_path)

    similarity = compare_embeddings(fragment_embedding, embedding)

    if name not in distances_by_video:
        distances_by_video[name] = []

    distances_by_video[name].append(similarity.item())

# Calculate average, maximum, minimum, and median similarity for each video
results = []
for name, similarities in distances_by_video.items():
    avg_similarity = sum(similarities) / len(similarities)
    max_similarity = max(similarities)
    min_similarity = min(similarities)
    median_similarity = median(similarities)

    results.append((name, avg_similarity, max_similarity, min_similarity, median_similarity))

# Sort results by maximum similarity in descending order
sorted_results = sorted(results, key=lambda x: x[2], reverse=True)

# Print only the top 2 matching videos
print("\nTop 2 matching videos:")
for name, avg_similarity, max_similarity, min_similarity, median_similarity in sorted_results[:2]:
    print(f"Video: {name}")
    print(f"Average similarity: {avg_similarity}")
    print(f"Max similarity: {max_similarity}")
    print(f"Min similarity: {min_similarity}")
    print(f"Median similarity: {median_similarity}")
    print()
