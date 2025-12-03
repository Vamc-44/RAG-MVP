import pytesseract

# If Tesseract is not in PATH, specify the path manually:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

print(pytesseract.get_tesseract_version())
print(pytesseract.get_languages(config=''))