#First install pytesseract
import io
import re
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
#This is for Windows and shows where I store my library.
#this may not be needed for you but it was for me
expression = re.compile("^[0-3]?[0-9]/[0-3]?[0-9]/(?:[0-9]{2})?[0-9]{2}$")
expression2 = re.compile("^[0-3]?[0-9]/(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)/(?:[0-9]{2})?[0-9]{2}$")

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\schma\AppData\Local\Tesseract-OCR\tesseract.exe'
test = pytesseract.image_to_string(Image.open('r5.jpg'))#Prints English String
list = re.split('\s',test)
for x in list:
    #print(x)
    if(re.match(expression,x)):
        print(x)
    if(re.match(expression2,x)):
        print(x)
#print(pytesseract.image_to_string(Image.open('test2.jpg'),lang ='jpn_vert'))#Prints Japanese String
print(pytesseract.image_to_data(Image.open('test2.jpg'),lang ='jpn'))
#Prints Data of the image
with io.open("output2.txt", "w", encoding="utf-8") as f:
    f.write(pytesseract.image_to_data(Image.open('test2.jpg'),lang ='jpn_vert'))
