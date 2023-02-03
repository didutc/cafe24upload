
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
start = 352
end = 372

while True:
    try:



        trs = driver.find_elements('xpath','/html/body/div/div[2]/div/div[7]/div[3]/div[2]/table/tbody/tr')

        break
    except:

        doubleagent.errorboy()
        continue
tg = []
for li in trs:
    tt = li.get_attribute('innerHTML')
    try:
        tnumber=tt.split('G간편')[1].split('<')[0]

        if start <= int(tnumber) <= end:
            javanum = tt.split("""onclick="PageMove.SmartAdGroupManagement(""")[1].split(')')[0]
            tg.append(javanum)
    except:
        doubleagent.errorboy()
        pass
for li in tg:
    driver.execute_script('''PageMove.SmartAdGroupManagement('''+str(li)+''')''')



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


    while True:
        try:
            da = Alert(driver)
            da.accept()
            break
        except:
            time.sleep(1)
    driver.get('https://ad.esmplus.com/cpc/bidmng/bidmanagement')
    print(tnumber)

