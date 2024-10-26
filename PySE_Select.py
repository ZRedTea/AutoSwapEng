from PySE_General import *

def SwapSelect(x1,x2,y1,y2):
    TYPE = ['v.&n.','adj.','adv.','vt.','vi.','n.','v.']
    NO = [',',';','；','，']

    PWORD = [0.1698, 0.9150, 0.3056, 0.4053]
    PWORDX1 = int(GetPos(x1, x2, PWORD[0]))
    PWORDX2 = int(GetPos(x1, x2, PWORD[1]))
    PWORDY1 = int(GetPos(y1, y2, PWORD[2]))
    PWORDY2 = int(GetPos(y1, y2, PWORD[3]))

    KWORD = [0.1005,0.9098,0.2877,0.3805]
    KWORDX1 = int(GetPos(x1, x2, KWORD[0]))
    KWORDX2 = int(GetPos(x1, x2, KWORD[1]))
    KWORDY1 = int(GetPos(y1, y2, KWORD[2]))
    KWORDY2 = int(GetPos(y1, y2, KWORD[3]))

    PCHIN = [0.1421, 0.9081, 0.4891, 0.7788]
    PCHINX1 = int(GetPos(x1, x2, PCHIN[0]))
    PCHINX2 = int(GetPos(x1, x2, PCHIN[1]))
    PCHINY1 = int(GetPos(y1, y2, PCHIN[2]))
    PCHINY2 = int(GetPos(y1, y2, PCHIN[3]))

    PTEST = [0.0935, 0.9029, 0.3785, 0.4497]
    PTESTX1 = int(GetPos(x1, x2, PTEST[0]))
    PTESTX2 = int(GetPos(x1, x2, PTEST[1]))
    PTESTY1 = int(GetPos(y1, y2, PTEST[2]))
    PTESTY2 = int(GetPos(y1, y2, PTEST[3]))

    PSELC = [0.0883, 0.9150, 0.4865, 0.8316]
    PSELCX1 = int(GetPos(x1, x2, PSELC[0]))
    PSELCX2 = int(GetPos(x1, x2, PSELC[1]))
    PSELCY1 = int(GetPos(y1, y2, PSELC[2]))
    PSELCY2 = int(GetPos(y1, y2, PSELC[3]))

    SLIDE = [0.5060,0.8257,0.2772]
    SLIDEX = GetPos(x1,x2,SLIDE[0])
    SLIDEY1 = GetPos(y1,y2,SLIDE[1])
    SLIDEY2 = GetPos(y1,y2,SLIDE[2])

    CLICK = [0.5060,0.3006]
    CLICKX = GetPos(x1,x2,CLICK[0])
    CLICKY = GetPos(y1,y2,CLICK[1])

    FINI = [0.5069, 0.8755]
    FINIX = GetPos(x1, x2, FINI[0])
    FINIY = GetPos(y1, y2, FINI[1])

    SELEC = [0.5060,0.5284,0.5938,0.6633,0.7353]
    SELECY = [0 for _ in range(10)]
    SELECX = GetPos(x1,x2,SELEC[0])
    for i in range(1,5):
        SELECY[i] = GetPos(y1,y2,SELEC[i])

    GETWORDNR = [['' for _ in range(100)] for _ in range(100)]
    GETWORDCD = [[0 for _ in range(100)] for _ in range(100)]
    GETWORDSX = ['' for _ in range(100)]
    GETWORDSZ = [0 for _ in range(100)]
    SELWORDNR = [['' for _ in range(100)] for _ in range(100)]
    SELWORDCD = [[0 for _ in range(100)] for _ in range(100)]
    SELWORDSZ = [0 for _ in range(100)]

    RUN = True
    n = 0
    times = 0
    while(RUN):
        GetScreen(x1,x2,y1,y2,'SE.jpg')
        SE = GetOCR('SE.jpg')
        for kse in SE:
            kse = kse[1][0]
            if("恭喜你完成卡包学习" in kse):
                ZClick(FINIX,FINIY)
                return
            if("遇到错词不要怕" in kse):
                ZClick(FINIX,FINIY)


        SEL = True
        ZClick(CLICKX,CLICKY)
        # time.sleep(0.2)
        GetScreen(PTESTX1,PTESTX2,PTESTY1,PTESTY2,'TEST.jpg')
        testx = GetOCR('TEST.jpg')
        if(testx != None):
            SEL = False
        if(SEL == False):
            GetScreen(PWORDX1, PWORDX2, PWORDY1, PWORDY2, 'WORD.jpg')
            wordx = GetOCR('WORD.jpg')
            GETWORDSX[n] = wordx[0][1][0]
            GETWORDSZ[n] = 0
            GetScreen(PCHINX1, PCHINX2, PCHINY1, PCHINY2, 'CHIN.jpg')
            chinxx = GetOCR('CHIN.jpg')
            chin = ''
            m = 0
            test = ['' for _ in range(50)]

            for chinx in chinxx:
                chinx = chinx[1][0]
                temp = ''
                for each in chinx:
                    if (ord(each) in range(65, 91)):
                        jo = chr(ord(each) + 32)
                    else:
                        jo = each
                    temp += jo

                chinx = temp
                i = 0
                while (i < len(chinx)):
                    p = 1
                    if (i + 1 < len(chinx)):
                        test[2] = chinx[i] + chinx[i + 1]
                        # print("2=")
                        # print(test[2])
                        if (test[2] in TYPE):
                            p = 2
                    if (i + 2 < len(chinx)):
                        test[3] = chinx[i] + chinx[i + 1] + chinx[i + 2]
                        # print("3=")
                        # print(test[3])
                        if (test[3] in TYPE):
                            p = 3
                    if (i + 3 < len(chinx)):
                        test[4] = chinx[i] + chinx[i + 1] + chinx[i + 2] + chinx[i + 3]
                        # print("4=")
                        # print(test[4])
                        if (test[4] in TYPE):
                            p = 4
                    if (i + 4 < len(chinx)):
                        test[5] = chinx[i] + chinx[i + 1] + chinx[i + 2] + chinx[i + 3] + chinx[i + 4]
                        if (test[5] in TYPE):
                            p = 5
                    if (p != 1):
                        GETWORDSZ[n] = GETWORDSZ[n] + 1
                        GETWORDNR[n][GETWORDSZ[n]] += test[p]
                        GETWORDCD[n][GETWORDSZ[n]] = p
                    else:
                        GETWORDNR[n][GETWORDSZ[n]] += chinx[i]
                    i += p
            n += 1
        else:
            GetScreen(PSELCX1, PSELCX2, PSELCY1, PSELCY2, 'SELECT.jpg')
            selex = GetOCR('SELECT.jpg')
            GetScreen(KWORDX1, KWORDX2, KWORDY1, KWORDY2, 'WORD.jpg')
            wordx = GetOCR('WORD.jpg')
            word = wordx[0][1][0]
            witchSele = 0
            for sele in selex:
                sele = sele[1][0]
                temp = ''
                for each in sele:
                    if (ord(each) in range(65, 91)):
                        jo = chr(ord(each) + 32)
                    else:
                        jo = each
                    temp += jo

                sele = temp
                i = 2
                test = ['' for _ in range(10)]
                witchSele += 1
                while (i < len(sele)):
                    p = 1
                    if (i + 1 < len(sele)):
                        test[2] = sele[i] + sele[i + 1]
                        # print("2=")
                        # print(test[2])
                        if (test[2] in TYPE):
                            p = 2
                    if (i + 2 < len(sele)):
                        test[3] = sele[i] + sele[i + 1] + sele[i + 2]
                        # print("3=")
                        # print(test[3])
                        if (test[3] in TYPE):
                            p = 3
                    if (i + 3 < len(sele)):
                        test[4] = sele[i] + sele[i + 1] + sele[i + 2] + sele[i + 3]
                        # print("4=")
                        # print(test[4])
                        if (test[4] in TYPE):
                            p = 4
                    if (i + 4 < len(sele)):
                        test[5] = sele[i] + sele[i + 1] + sele[i + 2] + sele[i + 3] + sele[i + 4]
                        if (test[5] in TYPE):
                            p = 5
                    if (p != 1):
                        SELWORDSZ[witchSele] = SELWORDSZ[witchSele] + 1
                        SELWORDNR[witchSele][SELWORDSZ[witchSele]] += test[p]
                        SELWORDCD[witchSele][SELWORDSZ[witchSele]] = p
                    else:
                        SELWORDNR[witchSele][SELWORDSZ[witchSele]] += sele[i]
                    i += p

            similar = [0 for _ in range(10)]
            for i in range(1,5):
                simi = 0
                bj = 0
                for j in range(1,SELWORDSZ[i]+1):

                    thisw = 0
                    for x in range(0,n+1):
                        if(GETWORDSX[x] == word):
                            thisw = x

                    for k in range(1,GETWORDSZ[thisw]+1):
                        if(GETWORDCD[thisw][k] != SELWORDCD[i][j]):
                            simi = 0
                            similar[i] += simi
                            bj+=1
                        else:
                            GETWORDNR[thisw][k] = GETWORDNR[thisw][k][GETWORDCD[thisw][k]:]
                            SELWORDNR[i][j] = SELWORDNR[i][j][SELWORDCD[i][j]:]

                            print(GETWORDNR[thisw][k])
                            print(SELWORDNR[i][j])
                            temp1 = ['' for _ in range(20)]
                            temp2 = ['' for _ in range(20)]
                            tmp1 = 0
                            tmp2 = 0
                            for x in GETWORDNR[thisw][k]:
                                print("x为",x)
                                if(x in NO):
                                    tmp1 += 1
                                    print("词数+1")
                                else:
                                    temp1[tmp1] += x
                                    # print("temp1为",temp1)
                            for y in SELWORDNR[i][j]:
                                print("y为",y)
                                if(y in NO):
                                    tmp2 += 1
                                    print("词数+1")
                                else:
                                    temp2[tmp2] += y

                                    # print("temp2为",temp2)
                            # print("前词词数为",tmp1)
                            # print("后词词数为",tmp2)
                            for x in range(0,tmp1+1):
                                for y in range(0,tmp2+1):
                                    print(temp1[x],temp2[y])

                                    simi = fuzz.ratio(temp1[x],temp2[y])
                                    print("此相似度为",simi)
                                    similar[i] += simi
                                    if(simi >= 98):
                                        similar[i] += 1000
                                    bj+=1


                bj+=1
                similar[i] /= bj
                print("匹配度为",similar[i])

            max = 1
            for i in range(2,5):
                print(similar[i],similar[max])
                if(similar[i] > similar[max]):
                    print("改变")
                    max = i
            print("最大匹配度为",max)
            print("点击坐标为",SELECX,SELECY[max])
            ZClick(SELECX,SELECY[max])
        pg.moveTo(SLIDEX,SLIDEY1)
        pg.dragTo(SLIDEX,SLIDEY2,duration=0.2)
        time.sleep(0.6)




