import numpy as np
import fitz  # PyMuPDF
import cv2  
from sentence_transformers import SentenceTransformer
import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

print("PyMuPDF version:", fitz.__doc__.splitlines()[0])
print("OpenCV version:", cv2.__version__)
print("sentence-transformers OK:", SentenceTransformer("all-mpnet-base-v2").get_sentence_embedding_dimension())
print("Tesseract cmd:", pytesseract.pytesseract.tesseract_cmd)