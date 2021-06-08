import pytesseract
from urllib import request
from PIL import Image
import time

# 指定 tesseract.exe 所在路径
pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-OCR\tesseract.exe"

while True:
    filename = "captcha.png"
    captcha_url = "http://47.106.134.39/include/vdimgck.php?"
    request.urlretrieve(captcha_url, "captcha.png")
    image = Image.open(filename)
    text = pytesseract.image_to_string(image)
    print(text)
    time.sleep(2.5)

# 并不是所有都能识别出来

