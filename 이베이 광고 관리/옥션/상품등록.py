
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
import doubleagent
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
driver.switch_to.window(driver.window_handles[0])

groupcount  = 150
while True:

    data = doubleagent.picklereader('actionfinal.pkl')
    print(len(data))
    if len(data) == 0:
        break




    driver.get('https://ad.esmplus.com/cpc/bid')
    driver.find_element_by_xpath('/html/body/div/div[2]/div/div/ul/li[2]/div/label').click()
    driver.find_element_by_xpath('/html/body/div/div[2]/div/div/ul/li[2]/a/span').click()

    
    while True:
        try:
            driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div[3]/div/button/span').click()
            break
        except:
            time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div[3]/div/div[2]/div/dl/dd/span[1]/input').send_keys('A간편'+str(groupcount))
    driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div[3]/div/div[2]/div/div/button[1]/span').click()
    try:
        da = Alert(driver)
        da.accept()
    except:
        time.sleep(1)
    try:
        da = Alert(driver)
        da.accept()
    except:
        time.sleep(1)
    
    driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div[4]/div/table/tbody/tr[2]/td/div/div[1]/div[2]/input').click()
    driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div[4]/div/table/tbody/tr[2]/td/div/div[2]/div[2]/input').click()
    driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div[4]/div/table/tbody/tr[2]/td/div/div[2]/div[3]/input').click()
    driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div[4]/div/table/tbody/tr[2]/td/div/div[2]/div[4]/input').click()
    input()

    for i ,li in enumerate(data,start=1):

        if i > 1:
            t =driver.find_elements_by_xpath(
                '/html/body/div/div[2]/div[1]/div/div[7]/div[4]/div[2]/table/tbody/tr')
            if len(t) == 1:
                pass
            else:
                time.sleep(1)        
        driver.find_element_by_xpath(
                    '/html/body/div/div[2]/div[1]/div/div[7]/div[1]/div[1]/dl[1]/dd/div/input').clear()

        driver.find_element_by_xpath(
                    '/html/body/div/div[2]/div[1]/div/div[7]/div[1]/div[1]/dl[1]/dd/div/input').send_keys(li)   
        driver.find_element_by_xpath(
                '/html/body/div/div[2]/div[1]/div/div[7]/div[1]/div[2]/button[1]/span').click()  
        while True:
            try:
                driver.find_element_by_xpath(
                        '/html/body/div/div[2]/div[1]/div/div[7]/div[4]/div[2]/table/tbody/tr/td[9]/div/button').click()  
                break
            except:
                time.sleep(1)

        if i == 20:
            break
    driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[7]/div[7]/a').click()  

    data = data[20:]

    doubleagent.picklemaker('actionfinal.pkl',data)
    try:
        da = Alert(driver)
        da.accept()
    except:
        time.sleep(1)
    try:
        da = Alert(driver)
        da.accept()
    except:
        time.sleep(1)
    while True:
        try:
            driver.find_element_by_xpath(
                    '/html/body/div/div[2]/div/div[1]/div/strong')
            break
        except:
            time.sleep(1)
    groupcount=groupcount+1