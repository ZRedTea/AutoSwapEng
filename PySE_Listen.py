from PySE_General import *

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

    STAR = [0.5052, 0.5879]
    STARX = GetPos(x1, x2, STAR[0])
    STARY = GetPos(y1, y2, STAR[1])
    # pg.moveTo(Button1X,Button1Y)
    # PAUSE(5)
    # pg.moveTo(Button2X,Button2Y)
    # TM = 0
    Conti = True
    while Conti:
        GetScreen(x1,x2,y1,y2,'SE.jpg')
        List = GetOCR('SE.jpg')
        for keyword in List:
            if("温馨提示" in keyword[1][0]):
                ZClick(STARX,STARY)
            elif("当前卡包已完成" in keyword[1][0]):
                ZClick(Button3X, Button3Y)
                Conti = False
            elif("内容会慢慢呈现" in keyword[1][0] or "已播放" in keyword[1][0]):
                #pg.moveTo(Button1X,Button1Y)
                ZClick(Button1X,Button1Y)
            elif("点击按钮" in keyword[1][0]):
                #pg.moveTo(Button2X,Button2Y)
                ZClick(Button2X,Button2Y)
            elif("不能暂停" in keyword[1][0]):
                #pg.moveTo(Button2X,Button2Y)
                ZClick(Button2X,Button2Y)
            #TM += 1
        # if(TM >= 500):
        #     Conti = False