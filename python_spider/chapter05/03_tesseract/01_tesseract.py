import pytesseract  # 导入pytesseract库
from PIL import Image  # 导入 Image 库

# 指定 tesseract.exe 所在路径
pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-OCR\tesseract.exe"

image = Image.open("a.png")  # 打开英文图片
text = pytesseract.image_to_string(image=image)
print(text)
print(">>" * 10)
image = Image.open("b.png")  # 打开中文图片
text = pytesseract.image_to_string(image=image, lang='chi_sim')
print(text)