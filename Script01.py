import pytesseract as ocr
from PIL import Image

#Implementação do pytesseract para detecção de texto.

img = Image.open('MagicalAnde720pNetflix_0015.jpg').crop((0,720,1920,1080)) #end da imagem e o crop
sample = ocr.image_to_data(img,lang='eng+por') # detecção de texto em eng e pt
#sample = ocr.image_to_data(Image.open('image-black.jpeg'),lang='por')
#sample = pytesseract.image_to_string(Image.open('2019-12-17-v2.jpg'),lang='por' or 'eng')
#sample = pytesseract.image_to_pdf_or_hocr(Image.open('2019-12-17-v2.jpg'), extension='pdf')
if (sample == ""):
    print("Sem valores!")
else:
    print(sample)