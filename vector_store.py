import faiss
import numpy as np
import pickle

class FaissVectorStore:
    def __init__(self,dim:int):
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.metadata = []
       
    def add(self, embeddings: np.ndarray, metadatas: list):
        """
        Adds embeddings and their corresponding metadata to the Faiss index.

        Args:
            embeddings (np.ndarray): Array of shape (N, dim) containing the embeddings.
            metadatas (list): List of metadata dictionaries corresponding to each embedding.
        """
        self.index.add(embeddings)
        self.metadata.extend(metadatas)
    
    def search(self, query_embeddings: np.ndarray, top_k: int):
        """
        Searches the Faiss index for the top_k nearest neighbors of the query embeddings.

        Args:
            query_embeddings (np.ndarray): Array of shape (M, dim) containing the query embeddings.
            top_k (int): Number of nearest neighbors to retrieve.
        Returns:
            distances (np.ndarray): Array of shape (M, top_k) with distances to nearest neighbors.
            results (list): List of length M, each containing a list of top_k metadata dictionaries. 
            """
        distances, indices = self.index.search(query_embeddings, top_k)
        results = []
        for idx in indices[0]:
            if idx < len(self.metadata):
                results.append(self.metadata[idx])
        return results

    def save(self, index_path="faiss.index", meta_path="meta.pkl"):
        """
        Saves the Faiss index and metadata to disk.

        Args:
            index_path (str): Path to save the Faiss index.
            meta_path (str): Path to save the metadata.
        """
        faiss.write_index(self.index, index_path)
        with open(meta_path, "wb") as f:
            pickle.dump(self.metadata, f)
    
    def load(self, index_path="faiss.index", meta_path="meta.pkl"):
        """
        Loads the Faiss index and metadata from disk.

        Args:
            index_path (str): Path to load the Faiss index from.
            meta_path (str): Path to load the metadata from.
        """
        self.index = faiss.read_index(index_path)
        with open(meta_path, "rb") as f:
            self.metadata = pickle.load(f)