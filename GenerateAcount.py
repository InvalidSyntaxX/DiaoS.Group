from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import re
import time
import openpyxl
import configparser
import os
import pyperclip

#from NFTRecommendHttp import GetDriver


def ClickButton(driver, classname):
    try:
        elem = driver.find_element_by_class_name(classname)
        elem.click()
    except:
        ClickButton(driver, classname)

def ClickButtonXpath(driver, path):
    try:
        elem = driver.find_element_by_xpath(path)
        elem.click()
    except:
        ClickButtonXpath(driver, path)

option = webdriver.ChromeOptions()
option.add_argument("--user-data-dir="+r"C:\Users\iChaoNan\AppData\Local\Google\Chrome\User Data1")
driver = webdriver.Chrome(executable_path=r'E:\VS2015\NFTRecommend\env\Scripts\chromedriver.exe', chrome_options=option)
driver.get(r'chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#')
time.sleep(1)

# 填入密码
elem = driver.find_element_by_class_name('MuiInputBase-input.MuiInput-input')
elem.send_keys(r'**********')

# 进入账户
elem = driver.find_element_by_class_name('button.btn--rounded.btn-default')
elem.click()


file = open('MyETH.txt','w+')
try:
    for i in range(1, 100):
        # 点击账户头像
        ClickButton(driver, r'identicon__address-wrapper')

        # 创建账户
        ClickButtonXpath(driver, '//*[@id="app-content"]/div/div[3]/div[6]/div[2]')

        # 点击创建
        ClickButton(driver, r'button.btn--rounded.btn-primary.btn--large.new-account-create-form__button')

        # 点击复制
        ClickButton(driver, r'selected-account__address')

        # 写入文本
        ethAddress = pyperclip.paste()
        file.write(ethAddress + "\n")
finally:
    file.close()