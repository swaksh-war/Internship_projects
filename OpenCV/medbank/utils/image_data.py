import matplotlib.pyplot as plt
import cv2
import pytesseract
from PIL import Image

def ExtractDetails(image_path):
    text = pytesseract.image_to_string(Image.open(image_path), lang = 'eng')
    print(text)
    text = text.replace('\n', " ")
    text = text.replace('  '," ")
    regex_expdate = re.compile('EXP.\d{2}[-/]\d{4}')

    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    plt.axis('off')

    if len(regex_expdate.findall(text)) == 0:
        print(f'Blurry Image for tesseract please upload a new one')
    else:
        text = regex_expdate.findall(text)
        print(text)