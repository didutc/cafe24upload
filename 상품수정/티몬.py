
from selenium.webdriver.common.alert import Alert
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
import doubleagent
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
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




seta = '심혈관에좋은음식,뇌경색에좋은음식'
seta = seta.split(',')
if isinstance(seta,list) == False:
    seta = doubleagent.s2l(seta)

dock = 0
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
driver.switch_to.window(driver.window_handles[0])


select = Select(driver.find_element_by_xpath(
    '/html/body/div[2]/div[3]/div[2]/div[4]/div[1]/div[2]/select[2]'))
select.select_by_visible_text("100개씩 보기")
num = 1
while True:
    if dock == 10:

        break
    time.sleep(0.3)
    driver.find_element_by_xpath(
            '/html/body/div[2]/div[3]/div[2]/div[4]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[6]/div/a').click()
    driver.switch_to.window(driver.window_handles[-1])
    driver.find_element_by_xpath(
            '/html/body/form[1]/div[7]/a[3]/span').click()
    time.sleep(4)
    try:
        t=driver.find_element_by_xpath(
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[21]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').get_attribute('value')
        t = t.split(' ')
        itemname = t
        a_sub_b = [x for x in t if x not in seta]
        a_sub_b = ' '.join(a_sub_b)
        print(a_sub_b)
        
        if not len(t) == len(a_sub_b):
            driver.find_element_by_xpath(
                        '/html/body/form[1]/div[3]/div[7]/div[2]/div[21]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').clear()
            driver.find_element_by_xpath(
            '/html/body/form[1]/div[3]/div[7]/div[2]/div[21]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').send_keys(a_sub_b)      
    except:
        driver.find_element_by_xpath(
                    '/html/body/form[1]/div[3]/div[7]/div[2]/div[21]/div[1]/div[2]/table/tbody/tr[1]/td[1]/label/span').click()
        t=driver.find_element_by_xpath(
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[21]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').get_attribute('value')
        t = t.split(' ')
        a_sub_b = [x for x in t if x not in seta]
        a_sub_b = ' '.join(a_sub_b)
        print(a_sub_b)
        
        if not len(t) == len(a_sub_b):
            driver.find_element_by_xpath(
                        '/html/body/form[1]/div[3]/div[7]/div[2]/div[21]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').clear()
            driver.find_element_by_xpath(
            '/html/body/form[1]/div[3]/div[7]/div[2]/div[21]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').send_keys(a_sub_b)            
    driver.execute_script('document.getElementsByClassName("fToggle fMarketBasic")[9].click();')
    while True:
        try:
            elem = driver.find_elements_by_xpath(
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[21]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[1]')
            break
        except:
            time.sleep(0.3)       
            
    t=driver.find_element_by_xpath(
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[21]/div[1]/div[2]/table/tbody/tr[10]/td[2]/div[2]/input').get_attribute('value')

    keywordlist = t.split(',')


    total = []
    while True:
        for i,li in enumerate(itemname):
            if i == 0:
                flag = li
                total.append(li)
                continue
            flag = flag + li    
            total.append(flag)
        itemname = itemname[1:]
        if len(itemname) == 0:
            break  
    filterer = []
    a_sub_b = [x for x in keywordlist if x not in total]
    a_sub_b = [x for x in a_sub_b if x not in seta]
    a_sub_b = ','.join(a_sub_b)
    print(a_sub_b)
    try:
        driver.find_element_by_xpath(
                    '/html/body/form[1]/div[3]/div[7]/div[2]/div[21]/div[1]/div[2]/table/tbody/tr[10]/td[2]/div[2]/input').clear()
    except:
        driver.execute_script('document.getElementsByClassName("fToggle fMarketBasic")[9].click();')
        driver.find_element_by_xpath(
                    '/html/body/form[1]/div[3]/div[7]/div[2]/div[21]/div[1]/div[2]/table/tbody/tr[10]/td[2]/div[2]/input').clear()
    driver.find_element_by_xpath(
    '/html/body/form[1]/div[3]/div[7]/div[2]/div[21]/div[1]/div[2]/table/tbody/tr[10]/td[2]/div[2]/input').send_keys(a_sub_b)

    driver.find_element_by_xpath(
    '/html/body/form[1]/div[7]/a[6]').click()

    da = Alert(driver)
    while True:
        try:
            da.accept()
            break
        except:
            time.sleep(1)    
    driver.switch_to.window(driver.window_handles[0])
    dock = dock+1
