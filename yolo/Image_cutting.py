#coding=utf-8
from PIL import Image
import cv2
import numpy as np
import sys


def preprocess(gray):
    sobel = cv2.Sobel(gray,cv2.CV_8U,1,0,ksize =3)  #sober算子，x方向求梯度
    # Sobel 边缘检测二值化 类似PS中的图像颜色反转
    ret, binary = cv2.threshold(sobel, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
    # 膨胀，腐蚀
    element1 = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 9))
    element2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (24, 6))
    # 膨胀一次，去掉细节，类似ps中的羽化
    dilation = cv2.dilate(binary, element2, iterations=1)
    # 腐蚀一次，去掉细节
    erosion = cv2.erode(dilation, element1, iterations=1)
    # 再次膨胀，让轮廓明显一些
    dilation2 = cv2.dilate(erosion, element2, iterations=2)
    cv2.imwrite("binary.png",binary)
    cv2.imwrite("dilation.png",dilation)
    cv2.imwrite("erosion.png",erosion)
    cv2.imwrite("dilation2.png",dilation2)
    return dilation2


def findTextRegion(dilation2):
    region = []
    binary, contours, hierarchy = cv2.findContours(dilation2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
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
    return region
def detect_image(img):
    imag = cv2.imread('test1.jpg',1)
    # 转换为灰度图
    gray = cv2.cvtColor(imag,cv2.COLOR_BGR2GRAY)
    dilation = preprocess(gray)
    region = findTextRegion(dilation)
    for box in region:
        cv2.drawContours(img,[box],0,(0,255,0),2)
    cv2.namedWindow('img',cv2.WINDOW_NORMAL)
    cv2.imshow('img',img)
    cv2.imwrite('contours.png',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#
# def text_detect(img):
#     # 模型路径
#     checkpoint_path = r'E:/EAST-master/east_icdar2015_resnet_v1_50_rbox/'
#
#     # 模型参数
#     input_images = tf.placeholder(tf.float32, shape=[None, None, None, 3], name='input_images')
#     global_step = tf.get_variable('global_step', [], initializer=tf.constant_initializer(0), trainable=False)
#
#     f_score, f_geometry = model.model(input_images, is_training=False)
#
#     variable_averages = tf.train.ExponentialMovingAverage(0.997, global_step)
#     saver = tf.train.Saver(variable_averages.variables_to_restore())
#
#     sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True))
#
#     # 加载模型
#     ckpt_state = tf.train.get_checkpoint_state(checkpoint_path)
#     model_path = os.path.join(checkpoint_path, os.path.basename(ckpt_state.model_checkpoint_path))
#     saver.restore(sess, model_path)
#
#     # 预测文本框
#     im_resized, (ratio_h, ratio_w) = resize_image(img)
#     score, geometry = sess.run(
#         [f_score, f_geometry],
#         feed_dict={input_images: [im_resized[:, :, ::-1]]})
#
#     boxes, _ = detect(score_map=score, geo_map=geometry,
#                       timer=collections.OrderedDict([('net', 0), ('restore', 0), ('nms', 0)]))
#
#     if boxes is not None:
#         scores = boxes[:, 8].reshape(-1)
#         boxes = boxes[:, :8].reshape((-1, 4, 2))
#         boxes[:, :, 0] /= ratio_w
#         boxes[:, :, 1] /= ratio_h
#
#     text_lines = []
#     if boxes is not None:
#         text_lines = []
#         for box, score in zip(boxes, scores):
#             box = sort_poly(box.astype(np.int32))
#             if np.linalg.norm(box[0] - box[1]) < 5 or np.linalg.norm(box[3] - box[0]) < 5:
#                 continue
#             tl = collections.OrderedDict(zip(
#                 ['x0', 'y0', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3'],
#                 map(float, box.flatten())))
#             tl['score'] = float(score)
#             text_lines.append(tl)
#     ret = {
#         'text_lines': text_lines,
#     }
#     return ret




if __name__ == '__main__':
    imgpath = r'D:\AutoZone\yolo\test4.jpg'
    img=cv2.imread(imgpath)
    detect_image(img)