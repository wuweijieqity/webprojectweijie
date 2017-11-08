import os
import cv2
from PIL import Image, ImageDraw


def detectByClf(image_name, clf):
    img = cv2.imread(image_name)
    smiles_cascade = cv2.CascadeClassifier(clf)
    # 如果img维度为3，表示非灰度图，先转化为灰度图gray，如果不为3，即2，原图就是灰度图

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    print(
    "start detecting...")
    zones = smiles_cascade.detectMultiScale(gray, 1.3, 5)
    result = []
    for (x, y, width, height) in zones:
        result.append((x, y, x + width, y + height))
    print
    "end detecting."
    return result


# 将检测到的区域保存到outpath目录中
def saveDetected(image_name, clf, outpath="/Users/weijiewu/Desktop/dsplab/project/output"):
    if not os.path.exists(outpath):
        os.mkdir(outpath)
    detected = detectByClf(image_name, clf)
    if detected:
        print(
        "start save detected...")
        if outpath == "/Users/weijiewu/Desktop/dsplab/project":
            outdir = outpath + "/" + image_name.split('.')[0] + "_faces"
        else:
            outdir = outpath
        if not os.path.exists(outdir):
            os.mkdir(outdir)
        count = 0
        for (x1, y1, x2, y2) in detected:
            # 将人脸保存在outdir目录下。
            file_name = os.path.join(outdir, str(count) + ".jpg")
            # Image模块：Image.open获取图像句柄
            # crop剪切图像(剪切的区域就是detectFaces返回的坐标)，save保存。
            Image.open(image_name).crop((x1, y1, x2, y2)).save(file_name)
            count += 1
        print
        "end saved."
    else:
        print
        "Not detected!"


# 在原图像上绘制检测到的区域
def drawDetected(image_name, clf, outfile):
    detected = detectByClf(image_name, clf)
    if detected:
        print
        "start drawing detected..."
        img = Image.open(image_name)
        draw_instance = ImageDraw.Draw(img)
        for (x1, y1, x2, y2) in detected:
            draw_instance.rectangle((x1, y1, x2, y2), outline=(255, 0, 0))
        img.save(outfile)
        print
        "end drawing."
    else:
        print
        "Not detected!"


def main():
    # CentOS系统clf的路径在/usr/share/OpenCV/haarcascades/下
    # 这里我将其拷贝到本目录
    clf_face = "/Users/weijiewu/Desktop/dsplab/project/haarcascades/haarcascade_frontalface_default.xml"  # face
    clf_mouth = "/Users/weijiewu/Desktop/dsplab/project/haarcascades/haarcascade_mcs_mouth.xml"  # mouth
    # clf_eye = "haarcascades/haarcascade_eye.xml" #eye
    clf_smile = "/Users/weijiewu/Desktop/dsplab/project/haarcascades/haarcascade_smile.xml" #smile

    picture = "group.jpg"  # 输入图像
    pic_front = "draw_" + picture.split(".")[0]
    outface = pic_front + "_face.jpg"
    outmouth = pic_front + "_mouth.jpg"
    # outeye = pic_front + "_eye.jpg"
    outsmile = pic_front + "_smile.jpg"

    # 开始检测并绘制检测区域
    drawDetected(picture, clf_face, outface)
    drawDetected(picture, clf_mouth, outmouth)
    # drawDetected(picture,  clf_eye, outeye)
    drawDetected(picture, clf_smile, outsmile)
    # 保存检测到的脸部
    saveDetected(picture, clf_face)


if __name__ == '__main__':
    main()