#First install pytesseract
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
#This is for Windows and shows where I store my library.
#this may not be needed for you but it was for me
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\schma\AppData\Local\Tesseract-OCR\tesseract.exe'
print(pytesseract.image_to_string(Image.open('test.jpg')))#Prints English String
print(pytesseract.image_to_string(Image.open('test2.jpg'),lang ='jpn_vert'))#Prints Japanese String
print(pytesseract.image_to_data(Image.open('test2.jpg'),lang ='jpn'))
#Prints Data of the image
