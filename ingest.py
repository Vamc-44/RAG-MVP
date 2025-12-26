import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import cv2
import numpy as np
import os


# ------------------------
#  PDF TEXT EXTRACTION
# ------------------------
def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    pages = []

    for i, page in enumerate(doc):
        text = page.get_text()

        # If text is empty (scanned PDF), fallback to OCR
        if not text.strip():
            pix = page.get_pixmap(dpi=200)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            text = pytesseract.image_to_string(img)

        pages.append({
            "file_name": os.path.basename(file_path),
            "page_number": i + 1,
            "content": text.strip()
        })

    return pages


# ------------------------
#  IMAGE OCR EXTRACTION
# ------------------------
def extract_text_from_image(file_path):
    # Load with OpenCV
    img = cv2.imread(file_path)
    if img is None:
        raise ValueError("Image not found or unreadable.")

    # Convert BGR → RGB
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # OCR
    text = pytesseract.image_to_string(rgb)
    return text


# ------------------------
#  UNIVERSAL EXTRACTOR
# ------------------------
def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext in [".pdf"]:
        return extract_text_from_pdf(file_path)

    if ext in [".png", ".jpg", ".jpeg"]:
        return extract_text_from_image(file_path)

    raise ValueError(f"Unsupported file type: {ext}")


if __name__ == "__main__":
    file_path = "sample_files/VamshidharReddy_Ankenapalle_Resume.pdf"  # change this
    
    text = extract_text(file_path)
    print("\n=== Extracted Text (First 500 chars) ===\n")
    print(text[:500])
