
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
item_list =[5975009245,5975003745,5975001962]

for data in item_list:
    driver.get('https://sell.smartstore.naver.com/#/products/origin-list')
    time.sleep(3)

    while True:
        try:
            driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div/ui-view[1]/div[2]/form/div[1]/div/ul/li[1]/div/div/div[2]/textarea').clear()
            driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div/ui-view[1]/div[2]/form/div[1]/div/ul/li[1]/div/div/div[2]/textarea').send_keys(data)
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


    while True:
        try:
            driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[15]/div[2]/div[1]/div/div/a').click()
            break
        except:
            driver.execute_script("window.scrollTo(0, 3500)")
            time.sleep(1)
    inputy = driver.find_elements_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[15]/div[2]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label')
    selector = '해당 없음'
    selector = selector.split(',')
    counter = 1
    counter_list = []
    for li in inputy:

        li_text = li.text
        print(selector)
        if li_text in selector:
            li.click()
            counter_list.append(counter)

        counter = counter +1        

    # print(counter_list)
    driver.execute_script("window.scrollTo(0, 3800)")
    driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[15]/div[2]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]').click()
    driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[15]/div[2]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[2]/div/div[9]').click()

    driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[15]/div[2]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div[1]/div/div/div[1]').click()
    driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[15]/div[2]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[2]/div/div[3]').click()
    while True:
        try:
            driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[15]/div[2]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div[2]/div[1]/div/input').clear()
            driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[15]/div[2]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div[2]/div[1]/div/input').send_keys(800)
            break
        except:

            time.sleep(1)


    driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[15]/div[2]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]').click()
    driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[15]/div[2]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[2]/div/div[20]').click()

    용량 = 2#개월 
    용량 = 27+용량 - 1
    driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[15]/div[2]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div/div/div[1]').click()
    driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[15]/div[2]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div/div/div[2]/div/div['+str(용량)+']').click()




    driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[15]/div[2]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[5]/td/div/div/div/div/div[1]').click()
    driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[15]/div[2]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[5]/td/div/div/div/div/div[2]/div/div[5]').click()

    driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[15]/div[2]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[6]/td/div/div/div/div/div[1]').click()
    driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[15]/div[2]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[6]/td/div/div/div/div/div[2]/div/div[2]').click()

    driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[15]/div[2]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[7]/td/div/div/div/div/div[1]').click()
    driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[15]/div[2]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[7]/td/div/div/div/div/div[2]/div/div[2]').click()

    driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[15]/div[2]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[8]/td/div/div/div/div/div[1]').click()
    driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[15]/div[2]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[8]/td/div/div/div/div/div[2]/div/div[2]').click()



    driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[3]/div[2]/div[1]/button[2]/span[1]').click()
    input()
    while True:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/button[2]').click()
            break
        except:
            time.sleep(1)
    print(1)