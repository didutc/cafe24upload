
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
## # # # # # # # # # # # # # # # # # # # # # # # #  

# # # # # # # # # # # # # # # # # # # # # # # # # 
f = open("coupangkeyword.txt", 'r', -1, "utf-8")
coupangkeyword = f.read()
f.close()
coupangkeyword=coupangkeyword.split('\n')
while True:
    f = open("coupangitem.txt", 'r', -1, "utf-8")
    coupangitem = f.read()
    f.close()
    coupangitem=coupangitem.split('\n')
    driver.get('https://wing.coupang.com/tenants/seller-web/vendor-inventory/modify?vendorInventoryId='+str(coupangitem[0]))


    keyword = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/section/section/div[2]/div[2]/div/div[3]/div/div/div[2]/input').get_attribute('value').split(' ')
    print(keyword)
  
    while True:
        try:

            element2 = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/section/section/div[2]/div[8]/div/div/div/button').click()
            break
        except:

            driver.execute_script("window.scrollTo(0, 3500)")
            time.sleep(1)
    flag = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div/section/section/div[2]/div[8]/div/div/div[2]/div/div/div/div[2]/div[2]/ul/li")
    for li in enumerate(flag):
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/section/section/div[2]/div[8]/div/div/div[2]/div/div/div/div[2]/div[2]/ul/li[1]/button").click()






    unoverlap=doubleagent.sublist(coupangkeyword,keyword)
    unoverlap = doubleagent.mix(unoverlap)
    unoverlap = list(dict.fromkeys(unoverlap))
    if len(unoverlap)>20:
        flag = 20 - len(unoverlap)
        unoverlap = unoverlap[:flag]
    
    unoverlap=','.join(unoverlap)
    print(unoverlap)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/section/section/div[2]/div[8]/div/div/div[2]/div/div/div/div[2]/div[1]/input').send_keys(unoverlap )
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/section/section/div[2]/div[8]/div/div/div[2]/div/div/div/div[2]/div[1]/button').click()
    driver.execute_script("window.scrollTo(0, 4000)")    


    while True:
        try:

            driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/section/section/div[2]/footer/div/div/div[2]/button').click()
            break
        except:
            time.sleep(1)


    while True:
        try:
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[6]/button[2]').click()
            break
        except:
            time.sleep(1)
    coupangitem=coupangitem[1:]
    coupangitem = '\n'.join(coupangitem)
    f = open("coupangitem.txt", 'w', -1, "utf-8")
    f.write(coupangitem)
    f.close()

