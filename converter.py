#image library pillow and OCR tool tesseract
from PIL import Image
import pytesseract
class imageProcessing:
    def getImage():
        myImage = 'train_5.eps' # insert the eps file to be processed here,it should be in the same path as the python file
        image_eps = myImage
        im = Image.open(image_eps)
        fig = im.convert('RGBA')
        image_png = 'train_1.png'  # define the output file name
        fig.save(image_png, lossless=True)
        img = Image.open('train_1.png')  # the file to be processed
        print(pytesseract.image_to_string(img, config='--psm 6'))

imageProcessing.getImage()
