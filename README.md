# (VFEP) Video Fragment Embedding Project

This project is focused on calculating embeddings for video fragments to identify if a specific fragment belongs to a particular video. The main objective is to ensure accurate video fragment detection by comparing image embeddings extracted from video segments. The process is organized by numbered scripts to ensure proper execution order, and the environment is managed by a Conda environment configuration file (`environment.yml`).

---

## Setup

1. **Install Conda**: Make sure you have Conda installed. If not, you can download it from [Anaconda's official website](https://www.anaconda.com/products/distribution).

2. **Create the environment**: Use the provided `environment.yml` file to create the environment:

   ```bash
   conda env create -f environment.yml
   ```

3. **Activate the environment**: Activate the environment to start using it:

   ```bash
   conda activate embedding-test
   ```

## Execution order

1. **0-gen-dataset.py**: Download videos from YouTube and extract frames to create the dataset.
2. **1-gen-embeddings.py**: Extract embeddings from the dataset frames.
3. **2-test.py**: Configure one fragment, from one video, and test how well the embeddings can identify the video that fragment belongs to.
4. **3-test-text.py**: Search something in image by text.
