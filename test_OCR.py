import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from PIL import Image

image = Image.open('test_image.png')
text = pytesseract.image_to_string(image)

print("-------------OCR Result-------------")
print(text)
print("------------------------------------")
