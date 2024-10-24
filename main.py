import time

import pyscreenshot as ImageGrab
import pyautogui as pg
from paddleocr import PaddleOCR as OCR
from scipy.constants import Btu_IT

pg.PAUSE = 1


BX = [0.1081,0.5959,0.4008,0.3048]
# img = ImageGrab.grab(bbox=(0,0,500,500))
# img.save('tmp.jpg')
#
# ocr = OCR(use_angle_cls=True, lang="ch")
# img_tmp = 'tmp.jpg'
# img2 = img
# result = ocr.ocr(img_tmp, cls=True)
# for idx in range(len(result)):
#     res = result[idx]
#     for line in res:
#         print(line)

def PAUSE(x):
    for i in range(0,x):
        print(x-i)
        time.sleep(1)

def GetPos(a,b,c):
    return ((b-a)*c+a)

def GetOCR():
    ocr = OCR(use_angle_cls = True, lang = "ch")
    img_SE = 'SE.jpg'
    result = ocr.ocr(img_SE, cls=True)
    result = result[0]
    return result

def GetXY():
    global x1,x2,y1,y2
    x1,x2 = input("请输入最左端和最右端的坐标值")
    y1,y2 = input("请输入最上端和最下端的坐标值")

def GetXYPG():
    global x1,x2,y1,y2
    print("请将鼠标移至翻转外语界面左上角")
    PAUSE(3)
    x1,y1 = pg.position()
    print("请将鼠标移至翻转外语界面右下角")
    PAUSE(3)
    x2,y2 = pg.position()

def GetKBPG():
    global kbx1,kbx2,kby1,kby2
    print("请将鼠标移至翻转外语键盘左上角")
    PAUSE(3)
    kbx1, kby1 = pg.position()
    print("请将鼠标移至翻转外语键盘右下角")
    PAUSE(3)
    kbx2, kby2 = pg.position()


def OutXY():
    print(x1,x2)
    print(y1,y2)

def GetScreen():
    global x1,x2,y1,y2
    img = ImageGrab.grab(bbox=(x1,y1,x2,y2))
    img.save('SE.jpg')

def SwapSpell():
    global KBX,KBY
    global x1,x2,y1,y2
    global kbx1,kbx2,kby1,kby2

    L1Y = GetPos(kby1,kby2,0.1675)
    L2Y = GetPos(kby1,kby2,0.3832)
    L3Y = GetPos(kby1,kby2,0.6091)

    KBX[1] = GetPos(kbx1,kbx2,0.1081) #A
    KBY[1] = L2Y




def SwapListen(x1,x2,y1,y2):
    #点击前：耐心听1遍原句，内容会慢慢呈现
    #点击后：播放当中不能暂停
    #完成后：点击按钮，开始录音
    Button1X = (x2-x1)*0.2811 + x1
    print(Button1X)
    Button1Y = (y2-y1)*0.8427 + y1
    print(Button1Y)

    Button2X = (x2-x1)*0.9376 + x1
    print(Button2X)
    Button2Y = (y2-y1)*0.9826 + y1
    print(Button2Y)

    Button3X = (x2-x1)*0.3504 + x1
    print(Button3X)
    Button3Y = (y2-y1)*0.9517 + y1
    print(Button3Y)

    # pg.moveTo(Button1X,Button1Y)
    # PAUSE(5)
    # pg.moveTo(Button2X,Button2Y)
    # TM = 0
    Conti = True
    while Conti:
        GetScreen()
        List = GetOCR()
        for keyword in List:
            if("当前卡包已完成" in keyword[1][0]):
                pg.click(Button3X, Button3Y)
                Conti = False
            elif("内容会慢慢呈现" in keyword[1][0] or "已播放" in keyword[1][0]):
                #pg.moveTo(Button1X,Button1Y)
                pg.click(Button1X,Button1Y)
            elif("点击按钮" in keyword[1][0]):
                #pg.moveTo(Button2X,Button2Y)
                pg.click(Button2X,Button2Y)
            elif("不能暂停" in keyword[1][0]):
                #pg.moveTo(Button2X,Button2Y)
                pg.click(Button2X,Button2Y)
            time.sleep(0.2)
            #TM += 1
        # if(TM >= 500):
        #     Conti = False


def main():
    GetXYPG()
    OutXY()
    GetScreen()
    SwapListen(x1,x2,y1,y2)
    # Get = GetOCR()
    # for each in Get:
    #     print(each[1][0])
    #     if("点击按钮" in each[1][0]):
    #         print("Get!")


main()


#def GetImage():
#    img = ImageGrab.grab()
#    return img

#pg.drag(yOffset=-1000, duration=0.25, button='left')
