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

first = 41
last = 52

for li in range(first,last+1):
    while True:
        try:



            driver.find_element("xpath",'/html/body/div[1]/div/section[3]/div[2]/div/div[1]/div[2]/button[3]').click()

            break
        except:
            time.sleep(0.1)
            doubleagent.errorboy()
            continue

    while True:
        try:



            driver.find_element("xpath",'/html/body/div[31]/div[1]/div[1]')

            break
        except:
            time.sleep(0.1)
            doubleagent.errorboy()
            continue
    while True:
        try:



            driver.find_element("xpath",'/html/body/div[31]/div[2]/div[1]/div/div[2]/table/tbody/tr/td/input').send_keys(li)

            break
        except:
            time.sleep(0.1)
            doubleagent.errorboy()
            continue
    while True:
        try:



            driver.find_element("xpath",'/html/body/div[31]/div[2]/div[2]/button[2]').click()

            break
        except:
            time.sleep(0.1)
            doubleagent.errorboy()
            continue


