import fitz  # PyMuPDF
p = "sample_files/VamshidharReddy_Ankenapalle_Resume.pdf"
doc = fitz.open(p)
#print("Number of pages:", doc.page_count)
print("pages:", len(doc))

for i, page in enumerate(doc, start=1):
    text = page.get_text("text")
    print(f"\n--- page {i} ---\n", (text[:400] + '...') if len(text) > 400 else text)
    

