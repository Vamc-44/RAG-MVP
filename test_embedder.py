from embedder import embed_texts

sample_chunks = [
    {"text": "This is a test sentence."},
    {"text": "RAG systems chunk text and embed it."}
]

embeddings = embed_texts(sample_chunks)

print("Shape:", embeddings.shape)
print("First vector (first 5 dims):", embeddings[0][:5])
