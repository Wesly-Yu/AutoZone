#coding:utf-8
import pytesseract
from PIL import Image,ImageFilter

tessdata_dir_config = '--tessdata-dir "E://Program Files//Tesseract-OCR//tessdata"'
im = Image.open('E:\code4.png')
# 转化为灰度图像
# im = im.filter(ImageFilter.SHARPEN)
im = im.convert('L')  # 转化为灰度图像
threshold = 200
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
ime = im.point(table, '1')
ime.save('E:\che4.png')
code = pytesseract.image_to_string(ime,config=tessdata_dir_config)
print(code)