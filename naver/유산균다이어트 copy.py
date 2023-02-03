
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
from selenium.webdriver.support.select import Select

try:

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    driver.switch_to.window(driver.window_handles[0])
except Exception as ex:
    print(ex)
    doubleagent.seleupdate(str(ex))
item_list =[5975300523,5975298825]


time.sleep(3)

while True:
    try:
        driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[15]/div[2]/div[1]/div/div/a').click()
        break
    except:
        driver.execute_script("window.scrollTo(0, 4000)")
        time.sleep(1)
        
# driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[15]/div[2]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]').click()

# driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[15]/div[2]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[2]/div/div[20]').click()




# driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[3]/div[2]/div[1]/button[2]/span[1]').click()