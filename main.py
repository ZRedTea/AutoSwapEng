from scipy.constants import Btu_IT

from PySE_General import *
from PySE_Spell import SwapSpell
from PySE_Listen import SwapListen

def main():
    x1,x2,y1,y2 = GetXYPG()
    OutXY(x1,x2,y1,y2)
    GetScreen(x1,x2,y1,y2)
    #keyboardtest(x1,x2,y1,y2)
    SwapSpell(x1,x2,y1,y2)
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
