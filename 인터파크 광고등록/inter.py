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



flag = 1
itemflag =1
while True:
    
    if flag == 17:
        break

    driver.get('https://sellerad.interpark.com/ufaCnpMng/adMng/adMng02')
    while True:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/section[3]/div/div/div[1]/div/section/div/div[3]/div/div/button').click()
            break
        except:
            time.sleep(1)
    while True:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/section[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/div/button').click()
            break
        except:
            time.sleep(1)

    while True:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/section[3]/div/div/div[3]/div/div[1]/div/table/tbody/tr[1]/td/span/span[1]/span/span[1]').click()
            break
        except:
            time.sleep(1)
    group = driver.find_elements_by_xpath('/html/body/span/span/span[2]/ul/li')
    for i,li in enumerate(group,start=1):
        if str(flag) == li.text:
            target = i
            break
    driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li['+str(target)+']').click()

    while True:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/section[3]/div/div/div[3]/div/div[1]/div/table/tbody/tr[2]/td/div/div/input').send_keys(90)
            break
        except:
            time.sleep(1)


    while True:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/section[3]/div/div/div[3]/div/div[2]/button').click()
            break
        except:
            time.sleep(1)
    itemflag = itemflag + 1
    if itemflag == 101:
       itemflag = 1
       flag=flag+1