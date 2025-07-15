# searcher.py
import faiss
import json
import numpy as np

def search_career_match(query_embedding, k=1):
    index = faiss.read_index("roadmap_index_local.faiss")

    with open("career_roadmaps_full.json", "r") as f:
        roadmap_data = json.load(f)

    D, I = index.search(np.array([query_embedding]), k=k)
    results = [roadmap_data[i] for i in I[0]]
    return results[0]  # top match
