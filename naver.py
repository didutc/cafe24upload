
from bs4 import element
from selenium.webdriver.common.alert import Alert
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
import doubleagent
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# try:
#     subprocess.Popen(
#         'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/Chrome_debug_temp"')
#     input()
#     chrome_options = Options()
#     chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#     chrome_driver = "chromedriver.exe"
#     driver = webdriver.Chrome(chrome_driver, options=chrome_options)

# except Exception as ex:
#     print(ex)
#     doubleagent.seleupdate(str(ex))

try:

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    driver.switch_to.window(driver.window_handles[0])
except Exception as ex:
    print(ex)
    doubleagent.seleupdate(str(ex))
driver.get('https://sell.smartstore.naver.com/#/products/origin-list')
time.sleep(3)
while True:
    try:
        driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div/ui-view[1]/div[2]/form/div[1]/div/ul/li[1]/div/div/div[2]/textarea').send_keys('5954807953')
        break
    except:
        time.sleep(1)
while True:
    try:
        driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div/ui-view[1]/div[2]/form/div[2]/div/button[1]').click()
        break
    except:
        time.sleep(1)
while True:
    try:
        driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div/ui-view[2]/div[1]/div[2]/div[3]/div/div/div/div/div[3]/div[1]/div/div[2]/span/button').click()
        break
    except:
        time.sleep(1)



        