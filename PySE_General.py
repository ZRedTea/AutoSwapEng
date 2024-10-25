import time
from paddleocr import PaddleOCR as OCR
import pyscreenshot as ImageGrab
import pyautogui as pg

pg.PAUSE = 0.05

def PAUSE(x):
    for i in range(0,x):
        print(x-i)
        time.sleep(1)

def GetOCR(path):
    ocr = OCR(use_angle_cls = True, lang = "ch")
    img_SE = path
    result = ocr.ocr(img_SE, cls=True)
    result = result[0]
    return result


def OutXY(x1,x2,y1,y2):
    print(x1,x2)
    print(y1,y2)

def GetScreen(x1,x2,y1,y2,path):
    img = ImageGrab.grab(bbox=(x1,y1,x2,y2))
    img.save(path)

def GetPos(a,b,c):
    return ((b-a)*c+a)

def ZClick(x,y):
    pg.moveTo(x,y)
    pg.click()

def GetXY(x1,x2,y1,y2):
    x1,x2 = input("请输入最左端和最右端的坐标值")
    y1,y2 = input("请输入最上端和最下端的坐标值")

def GetXYPG():
    print("请将鼠标移至翻转外语界面左上角")
    PAUSE(3)
    x1,y1 = pg.position()
    print("请将鼠标移至翻转外语界面右下角")
    PAUSE(3)
    x2,y2 = pg.position()
    return x1,x2,y1,y2

def GetKBPG():
    print("请将鼠标移至翻转外语键盘左上角")
    PAUSE(3)
    kbx1, kby1 = pg.position()
    print("请将鼠标移至翻转外语键盘右下角")
    PAUSE(3)
    kbx2, kby2 = pg.position()
    return kbx1,kbx2,kby1,kby2