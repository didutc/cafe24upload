
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
q = 2

while True:
    try:



        driver.find_element('xpath','/html/body/div/div[2]/div/ul/li[2]/a').click()

        break
    except:

        doubleagent.errorboy()
        continue
driver.execute_script('''function getElementByXpath(path) {
    x = document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;

    x.onclick();

}

getElementByXpath("/html/body/div/div[2]/div/div[7]/div[4]/a['''+str(q+2)+''']");''')
while True:
    try:



        group =  driver.find_elements('xpath','/html/body/div/div[2]/div/div[7]/div[3]/div[2]/table/tbody/tr')
        if len(group) == 0:
            continue

        break
    except:

        doubleagent.errorboy()
        continue


for i,li in enumerate(group,start=1):

    while True:
        try:
            driver.execute_script('''function getElementByXpath(path) {
                x = document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;

                x.onclick();

            }

            getElementByXpath("/html/body/div/div[2]/div/div[7]/div[4]/a['''+str(q+2)+''']");''')
            break
        except:

            doubleagent.errorboy()
            continue
    while True:
        try:
            driver.execute_script('''function getElementByXpath(path) {
                x = document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;

                x.onclick();

            }
            
            getElementByXpath("/html/body/div/div[2]/div/div[7]/div[3]/div[2]/table/tbody/tr['''+str(i)+''']/td[2]/div/a");''')
            break
        except:

            doubleagent.errorboy()
            
            continue

    while True:
        try:

            driver.find_element('xpath','/html/body/div/div[2]/div[1]/div/div[2]/div/table/tbody/tr[1]/td[1]/div/button/span').click()

            break
        except:

            doubleagent.errorboy()
            
            continue


    while True:
        try:

            driver.find_element('xpath','/html/body/div/div[2]/div[1]/div/div[3]/div/div[1]/div/table/tbody/tr/td[2]/div/button/span').click()

            break
        except:

            doubleagent.errorboy()
            
            continue
    while True:
        try:

            driver.execute_script('''function getElementByXpath(path) {
                x = document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                x.setAttribute('value','3000');
            }
            
            getElementByXpath("/html/body/div/div[2]/div[1]/div/div[3]/div/div[1]/div/table/tbody/tr/td[2]/div/div/div/div[1]/table/tbody/tr[1]/td[2]/div/div[2]/span[1]/label/input");''')
            driver.execute_script('''function getElementByXpath(path) {
                x = document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                x.setAttribute('value','3000');
            }
            
            getElementByXpath("/html/body/div/div[2]/div[1]/div/div[3]/div/div[1]/div/table/tbody/tr/td[2]/div/div/div/div[1]/table/tbody/tr[2]/td[2]/div/div[2]/span[1]/label/input");''')
            break
        except:

            doubleagent.errorboy()
            
            continue

    while True:
        try:

            driver.find_element('xpath','/html/body/div/div[2]/div[1]/div/div[3]/div/div[1]/div/table/tbody/tr/td[2]/div/div/div/div[2]/button[1]/span').click()

            break
        except:

            doubleagent.errorboy()
            
            continue
    da = Alert(driver)

    while True:


        try:
            da.accept()
            break
        except:

            time.sleep(1)

    driver.get('https://ad.esmplus.com/cpc/bidmng/bidmanagement')