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

    # pg.moveTo(Button1X,Button1Y)
    # PAUSE(5)
    # pg.moveTo(Button2X,Button2Y)
    # TM = 0
    Conti = True
    while Conti:
        GetScreen(x1,x2,y1,y2)
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