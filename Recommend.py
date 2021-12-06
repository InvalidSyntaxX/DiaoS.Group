'''python 3.7 环境运行'''


from pymouse import *
from pykeyboard import *
import pyperclip
import re
import time

k = PyKeyboard()
m = PyMouse()


def OpenPrivateWindow():
    k.press_key(k.control_key)
    k.press_key(k.shift_key)
    k.tap_key('n')
    time.sleep(0.1)
    k.release_key(k.shift_key)
    k.release_key(k.control_key)
    time.sleep(1)

def ClosePrivateWindow():
    k.press_key(k.control_key)
    k.tap_key('w')
    k.release_key(k.control_key)

def MoveToProperPos():
    # 必须先获取焦点
    m.click(436, 708)
    m.scroll(-7,None,None)
    time.sleep(1)
    m.click(436, 708)

def PressSubmit():
    # 按下提交键
    time.sleep(1)
    m.click(916, 702)
    time.sleep(2)

def PressLink():
    # 按下复制链接
    time.sleep(1)
    m.click(516, 692)
    time.sleep(1)

def CopyAndPast(text):
    pyperclip.copy(text)
    k.press_key(k.control_key)
    k.tap_key('v')
    k.release_key(k.control_key)

def Paste():
    time.sleep(0.5)
    k.press_key(k.control_key)
    k.tap_key('v')
    k.release_key(k.control_key)
    time.sleep(0.5)

recommendAcountsFile = open('RecETH.txt', 'r')
recommendAcounts = recommendAcountsFile.readlines()
linesCount = 84220

myAcountsFile = open('myeth.txt', 'r')
myAcounts = myAcountsFile.readlines()
j = 1
for acount in myAcounts:

    # 流量器焦点
    m.click(688, 23)

    # 打开私密窗口
    OpenPrivateWindow()

    # 账户拷贝到内存
    CopyAndPast("https://nftsea.one/")

    # 访问
    k.tap_key(k.enter_key)

    # 等待打开网页
    time.sleep(4)

    # 移动到正确位置 
    MoveToProperPos()

    CopyAndPast(acount)

    # 按下提交键
    PressSubmit()

    # 按下邀请链接
    PressLink()

    print("正在处理第%s个地址" % j)
    j = j + 1

    recommendLink = pyperclip.paste()
    ClosePrivateWindow()

    for i in range(1, 80):
        # 打开私密窗口
        time.sleep(1)
        OpenPrivateWindow()

        CopyAndPast(recommendLink)
        # 访问
        k.tap_key(k.enter_key)

        time.sleep(4)
        MoveToProperPos()

        print("正在推荐第%s个地址" % linesCount)

        linesCount = linesCount - 1
        recommendETH = recommendAcounts[linesCount]
        pyperclip.copy(recommendETH)
        # 填入邀请链接
        Paste()

        # 按下提交键
        PressSubmit()

        ClosePrivateWindow()
        time.sleep(1)







