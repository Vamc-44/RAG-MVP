from clean_text import clean_text
from chunker import chunk_pages

pages = [{"file_name":"demo.pdf","page_number":1,"content":"This is a short demo paragraph. " * 120}]
pages[0]["content"] = clean_text(pages[0]["content"])
chunks = chunk_pages(pages, method="char", chunk_size_chars=1000, overlap_chars=100)
print("Created", len(chunks), "chunks. Example chunk id:", chunks[0]["id"])
print(chunks[0]["text"][:400])
