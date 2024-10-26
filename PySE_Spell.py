from pickle import FALSE

from scipy.stats import false_discovery_control

from PySE_General import *

def SwapSpell(x1,x2,y1,y2):
    KBX,KBY = [0 for _ in range(27)],[0 for _ in range(27)]
    kbx1, kbx2, kby1, kby2 = 0,0,0,0

    BX = [0.1081, 0.5959, 0.4008, 0.3048, 0.2577, 0.4016, 0.5048, 0.6008,
          0.7471, 0.6991, 0.7967, 0.8943, 0.7910, 0.6934, 0.8447, 0.9463,
          0.0609, 0.3601, 0.2056, 0.4536, 0.6487, 0.4983, 0.1593, 0.3032,
          0.5520, 0.2056]

    BYL = [2, 3, 3, 2, 1, 2, 2, 2, 1, 2, 2, 2, 3, 3, 1, 1, 1, 1, 2, 1, 1, 3, 1, 3, 1, 3]
    BY = [0.1675, 0.3832, 0.6091]

    CAPS = [0.0813, 0.6091]
    CONT = [0.8650, 0.8464]
    DELT = [0.9315, 0.6045]


    kbx1,kbx2,kby1,kby2 = GetKBPG()
    for i in range(0, 26):
        KBX[i] = GetPos(kbx1, kbx2, BX[i])
        KBY[i] = GetPos(kby1, kby2, BY[BYL[i] - 1])
    CAPSX = GetPos(kbx1, kbx2, CAPS[0])
    CAPSY = GetPos(kby1, kby2, CAPS[1])

    CONTX = GetPos(kbx1, kbx2, CONT[0])
    CONTY = GetPos(kby1, kby2, CONT[1])

    DELTX = GetPos(kbx1, kbx2, DELT[0])
    DELTY = GetPos(kby1, kby2, DELT[1])

    FINI = [0.5069, 0.8755]
    FINIX = GetPos(x1, x2, FINI[0])
    FINIY = GetPos(y1, y2, FINI[1])

    STAR = [0.5052, 0.5879]
    STARX = GetPos(x1, x2, STAR[0])
    STARY = GetPos(y1, y2, STAR[1])

    CAPON = False
    RUN = True
    while(RUN):
        GetScreen(x1,x2,y1,y2,'SE.jpg')
        List = GetOCR('SE.jpg')

        rad = True
        for keyword in List:
            print(keyword[1][0])
            if("温馨提示" in keyword[1][0]):
                ZClick(STARX,STARY)
            if("提示" in keyword[1][0]):
                rad = False
                need = keyword[1][0]
                print("检测到"+need)
            if("任务已完成" in keyword[1][0]):
                RUN = False
                pg.moveTo(FINIX, FINIY)
                pg.click()
        if(RUN):
            if(rad):
                for i in range(0,20):
                    pg.moveTo(KBX[0], KBY[0])
                    pg.click()
                pg.moveTo(CONTX, CONTY)
                pg.click()
            else:
                pg.moveTo(DELTX, DELTY)
                pg.click()
                for word in need:
                    word = ord(word)
                    print("ASCII码为")
                    print(word)
                    if(word in range(97,123)):
                        if(CAPON == True):
                            pg.moveTo(CAPSX,CAPSY)
                            pg.click()
                            CAPON = False
                        word -= 97
                        pg.moveTo(KBX[word], KBY[word])
                        pg.click()
                    if(word in range(65,91)):
                        if(CAPON == False):
                            pg.moveTo(CAPSX,CAPSY)
                            pg.click()
                            CAPON = True
                        word -= 65
                        pg.moveTo(KBX[word], KBY[word])
                        pg.click()
                pg.moveTo(CONTX, CONTY)
                pg.click()



