from ingest import extract_text_from_pdf
from chunker import chunk_pages
from sentence_transformers import SentenceTransformer
from vector_store import FaissVectorStore

# 1️⃣ Extract text from PDF
pages = extract_text_from_pdf("sample_files/VamshidharReddy_Ankenapalle_Resume.pdf")
print(f"Extracted {len(pages)} pages")

# 2️⃣ Chunk text
chunks = chunk_pages(
    pages,
    method="char",
    chunk_size_chars=1000,
    overlap_chars=100
)

print(f"Created {len(chunks)} chunks")

# 3️⃣ Generate embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")
texts = [c["text"] for c in chunks]
embeddings = model.encode(texts, convert_to_numpy=True)

# 4️⃣ Store in FAISS
store = FaissVectorStore(dim=embeddings.shape[1])
store.add(embeddings, chunks)
store.save()

print("✅ FAISS index saved")

# 5️⃣ Test search
query = "machine learning experience"
q_emb = model.encode([query], convert_to_numpy=True)

results = store.search(q_emb, top_k=3)

for i, r in enumerate(results, 1):
    print(f"\n--- Result {i} ---")
    print(r["text"][:300])
