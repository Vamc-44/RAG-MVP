# embedder.py

from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List, Dict

# Load the model once (fast)
_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def embed_texts(chunks: List[Dict]) -> np.ndarray:
    """
    Accepts: list of chunk dictionaries 
             (each having key: "text")

    Returns: np.ndarray of shape (N, 384)
    """
    texts = [c["text"] for c in chunks]
    embeddings = _model.encode(texts, show_progress_bar=True)
    return np.array(embeddings)
