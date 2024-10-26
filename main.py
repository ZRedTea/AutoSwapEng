import sys
import pip
import importlib

ASE_VERSION = "RELEASE 1.0"

def install_module(module_name: str):
    try:
        importlib.import_module(module_name)
    except ImportError:
        args = ['install','-i','https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple',module_name]
        print(f'{module_name} 安装中')
        pip.main(args)
        print(f'{module_name} 安装成功')

def install_modules(module_list: list):
    for module_name in module_list:
        install_module(module_name)

if __name__ == "__main__":
    modules_to_install = ["pyautogui","PaddlePaddle","PaddleOCR","setuptools","pyscreenshot","fuzzywuzzy"]
    install_modules(modules_to_install)
    from PySE_General import *
    from PySE_Select import SwapSelect
    from PySE_Spell import SwapSpell
    from PySE_Listen import SwapListen
    x1, x2, y1, y2 = -1, -1, -1, -1
    while True:
        print("")
        print("""欢迎使用AutoSwapEng
——————菜单——————
1.选择翻转外语窗口位置
2.开始翻转外语
3.使用教程
4.关于
5.退出""")
        MainChoice = input("请输入:")
        if (MainChoice == "1"):
            print("")
            print("""请根据提示以此将鼠标移至翻转外语窗口的左上角和右下角
你有三秒钟的时间移动鼠标""")
            x1, x2, y1, y2 = GetXYPG()
            temp = input("输入任何字符来返回主菜单")
        elif (MainChoice == "2"):
            if (x1 == -1):
                print("")
                print("请先选择翻转外语窗口位置")
            else:
                print("")
                print("""——————翻转外语菜单——————
1.单词——选择
2.单词——拼写
3.听力
4.退出
(此菜单以后将会取消并改为自动操作)""")
                ViceChoice = input("请输入:")
                if (ViceChoice == "1"):
                    SwapSelect(x1, x2, y1, y2)
                elif (ViceChoice == "2"):
                    SwapSpell(x1, x2, y1, y2)
                elif (ViceChoice == "3"):
                    SwapListen(x1, x2, y1, y2)
                elif (ViceChoice == "4"):
                    print("返回主菜单")
                else:
                    print("未找到该操作")
            temp = input("输入任何字符来返回主菜单")
        elif (MainChoice == "3"):
            print("")
            print("""提示：本脚本为Windows端脚本，如果您需要安卓/IOS端脚本，请另寻他处
在使用此脚本前，请确保您能在电脑桌面上调出翻转外语窗口
一般我们推荐您使用Escrcpy来将手机屏幕映射至电脑上来操作""")
            print("")
            print("""在开始翻转外语之前，请确保您已经使用"选择翻转外语窗口位置"来确定翻转外语的窗口坐标
在确定完翻转外语的窗口坐标之后，请打开翻转外语菜单
然后，在点入您想做的某一项的界面后，在本脚本中选择相应的选项
然后您就可以静等脚本自动完成了""")
            print("")
            print("""有两点要注意的是 
1.拼写脚本需要您再选择一次翻转外语拼写中键盘的位置，与选择窗口位置的操作相同
2.选择脚本出现选择错误的情况是正常的，静等即可，无须担心
  这个可能是个BUG，在未来版本中应会修复""")
            print("")
            temp = input("输入任何字符来返回主菜单")
        elif (MainChoice == "4"):
            print("""本项目由ZRedTea开发，源代码版权归ZRedTea所有
本项目使用MIT开源协议

AutoSwapEng是一款使用Python编写的翻转外语自动化脚本
开发立项于2024年10月23日，初版开发完成于2024年10月26日
本项目开发原因主要还是因为作者真的懒得手写翻转外语了
于是稍微找了些资料写了这个脚本项目来自动化翻转外语

版本信息:""", ASE_VERSION)
            print("")
            temp = input("输入任何字符来返回主菜单")
        elif (MainChoice == "5"):
            sys.exit()