import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

class ImageProcessing:
  def __init__(self, image_path):
    self.image_path = image_path 
  
  def get_text(self):
    custom_config = r'--oem 3 --psm 6'
    image = cv2.imread(self.image_path)
    text = pytesseract.image_to_string(image, config=custom_config)
    return text

