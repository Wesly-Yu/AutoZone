#coding=utf-8
from PIL import Image
import cv2
import numpy as np
import sys
sys.path.append('/seglink/util')

def detect_words(img):
    imag = cv2.imread('test1.jpg',1)
    # 转换为灰度图
    gray = cv2.cvtColor(imag,cv2.COLOR_BGR2GRAY)
    sobel = cv2.Sobel(gray,cv2.CV_8U,1,0,ksize =3)
    #Sobel 边缘检测二值化 类似PS中的图像颜色反转
    ret,binary=cv2.threshold(sobel,0,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY)
    # 膨胀，腐蚀
    element1= cv2.getStructuringElement(cv2.MORPH_RECT,(30,9))
    element2 =cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (24,6))
    #膨胀一次，去掉细节，类似ps中的羽化
    dilation = cv2.dilate(binary,element2,iterations=1)
    #腐蚀一次，去掉细节
    erosion = cv2.erode(dilation,element1,iterations =1)
    #再次膨胀，让轮廓明显一些
    dilation2 = cv2.dilate(erosion,element2,iterations =2)
    # 查找轮廓和筛选文字区域
    region=[]
    binary,contours,hierarchy=cv2.findContours(dilation2,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours)):
        cnt = contours[i]
        #计算轮廓面积，筛选掉面积小的
        area = cv2.contourArea(cnt)
        if (area<1000):
            continue
        #找到最小的矩阵
        rect = cv2.minAreaRect(cnt)
        print(rect)
        # box是四个点的坐标
        box=cv2.boxPoints(rect)
        box = np.int0(box)
        #计算高度和宽度
        height = abs(box[0][1]-box[2][1])
        width = abs(box[0][0]-box[2][0])
        #根据文字特征 筛选那些太细的矩形，留下大一点的
        if (height>width*1.3):
            continue
        region.append(box)
    for box in region:
        cv2.drawContours(img,[box],0,(0,255,0),2)
    cv2.imshow('imge',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




if __name__ == '__main__':
    img = '/image/screenshot/test1.jpg'
    detect_words(img)