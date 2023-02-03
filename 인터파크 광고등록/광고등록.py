from tokenize import group
from selenium.webdriver.common.alert import Alert
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
import doubleagent
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from inspect import currentframe, getframeinfo
import pandas as pd

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
driver.switch_to.window(driver.window_handles[0])




group = 52
count = 1

while count < 101:

    df= pd.read_csv('인터파크 광고등록/item.csv')
    df = df.values.tolist()
    df = doubleagent.ll2l(df)


    while True:
        try:



            driver.find_element("xpath",'/html/body/div[1]/div/section[3]/div/div/div[1]/div/section/div/div[1]/div/div/input').send_keys(df[0])

            break
        except:
            time.sleep(0.1)

            continue
    driver.find_element("xpath",'/html/body/div[1]/div/section[3]/div/div/div[1]/div/section/div/div[3]/div/div/button').click()        
    while True:
        try:



            driver.find_element("xpath",'/html/body/div[1]/div/section[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/table/tbody/tr/td[3]/div/button').click()

            break
        except:
            time.sleep(0.1)

            continue
    while True:
        try:



            driver.find_element("xpath",'/html/body/div[1]/div/section[3]/div/div/div[3]/div/div[1]/div/table/tbody/tr[1]/td/span/span[1]/span/span[1]').click()

            break
        except:
            time.sleep(0.1)     

            continue
    while True:
        try:



            t = driver.find_elements("xpath",'/html/body/span/span/span[2]/ul/li')
            for i,li in enumerate(t,start=1):
                if str(group) == li.text:
                    break
            driver.find_element("xpath",'/html/body/span/span/span[2]/ul/li['+str(i)+']').click()

        except Exception as e: 
            print('finished')
            e = str(e)
            if 'not interactable' in e:
                print('ok')
            print(e+"all")
            input()
            continue
        break
    driver.find_element("xpath",'/html/body/div[1]/div/section[3]/div/div/div[3]/div/div[1]/div/table/tbody/tr[2]/td/div/div/input').send_keys(300)
    driver.find_element("xpath",'/html/body/div[1]/div/section[3]/div/div/div[3]/div/div[2]/button').click()
    while True:
        try:




            driver.find_element("xpath",'/html/body/div[13]/div[2]/div[2]/button').click()
            break
        except:
            time.sleep(0.1)

            continue

    driver.get('https://sellerad.interpark.com/ufaCnpMng/adMng/adMng02')
    df =df[1:]
    df = pd.DataFrame({'상품번호': df})
    df.to_csv("인터파크 광고등록/item.csv", mode='w',index = False , encoding='utf-8-sig')
    count = count+1
    if count == 100:
        break
# df = pd.DataFrame({'상품번호': df})
# df.to_csv("인터파크 광고등록/filtered.csv", mode='w',index = False , encoding='utf-8-sig')