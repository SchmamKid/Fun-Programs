try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\schma\AppData\Local\Tesseract-OCR\tesseract.exe'
print(pytesseract.image_to_string(Image.open('test.jpg')))
print(pytesseract.image_to_string(Image.open('test2.jpg'),lang ='jpn_vert'))
print(pytesseract.image_to_data(Image.open('test2.jpg'),lang ='jpn'))
