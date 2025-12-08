import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ingest import extract_text_from_pdf
from chunker import chunk_pages

PDF_PATH = "E:\RAG-MVP\sample_files\VamshidharReddy_Ankenapalle_Resume.pdf"

# --- FIX START ---
raw_pages = extract_text_from_pdf(PDF_PATH)

pages = []
for i, text in enumerate(raw_pages, start=1):
    pages.append({
        "file_name": os.path.basename(PDF_PATH),
        "page_number": i,
        "content": text
    })
# --- FIX END ---

print(f"Extracted {len(pages)} pages")

chunks = chunk_pages(
    pages,
    method="char",
    chunk_size_chars=2000,
    overlap_chars=200
)

print(f"Generated {len(chunks)} chunks\n")

for c in chunks[:3]:
    print("-" * 80)
    print("Chunk ID:", c["id"])
    print("Page:", c["page"])
    print("Chars:", len(c["text"]))
    print(c["text"][:300], "...")
