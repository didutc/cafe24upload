
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

group =  driver.find_elements_by_xpath('/html/body/div/div[2]/div/div[4]/div[3]/div[2]/table/tbody/tr')
item_list = []

for i,li in enumerate(group,start=1):
    driver.switch_to.window(driver.window_handles[0])
    kill =False
    while True:
        try:

            groupname = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[4]/div[3]/div[2]/table/tbody/tr['+str(i)+']/td[2]/div').text

            driver.find_element_by_xpath('/html/body/div/div[2]/div/div[4]/div[3]/div[2]/table/tbody/tr['+str(i)+']/td[2]/div/a').click()

            break
        except:

            doubleagent.errorboy()
            continue
    while True:
        try:
            items = driver.find_elements_by_xpath('/html/body/div/div[2]/div[1]/div/div[5]/div[6]/div[2]/table/tbody/tr')
            if items == []:
                doubleagent.errorboy()
                continue
            break
        except:
            doubleagent.errorboy()
            continue
    counter = 0
    for li in items:
        productnum = li.text
        productnum = productnum.split('\n')[2]
        item_list.append(productnum)
        if '판매중지' in li.text:
            counter = counter +1
    if len(items) == counter:
        kill = True

    driver.get('https://ad.esmplus.com/cpc/bidmng/bidmanagement')
    while True:
        try:
            delgoup =  driver.find_elements_by_xpath('/html/body/div/div[2]/div/div[4]/div[3]/div[2]/table/tbody/tr')
            if '광고주의 ID를 선택한 후 조회해 주세요.' == delgoup[0].text:
                
                continue
            break
        except:
            doubleagent.errorboy()
            continue

    if kill==True:

        for i,li in enumerate(delgoup,start=1):
            groupname2 = li.text
            groupname2 = groupname2.split('\n')[0]
            print(groupname2)
            print(groupname)
            if groupname == groupname2:
                
                while True:
                    try:
                        driver.find_element_by_xpath('/html/body/div/div[2]/div/div[4]/div[3]/div[2]/table/tbody/tr['+str(i)+']/td[1]/div/label/input').click()
                        driver.execute_script("window.scrollTo(0, 0)")
                        driver.find_element_by_xpath('/html/body/div/div[2]/div/div[4]/div[1]/div[2]/button[3]/span').click()
                        print(77)
                        break
                    except:
                        doubleagent.errorboy()
                        continue 
                break
            print('passed4')

        while True:
            try:
                da = Alert(driver)
                da.accept()
                break
            except:
                time.sleep(1)

        while True:
            try:
                da = Alert(driver)
                da.accept()
                break
            except:
                time.sleep(1)

data = pd.DataFrame({
    '상품번호': item_list,})


data.to_csv("지마켓광고등록상품.csv", mode='w',index = False , encoding='utf-8-sig')


# # try:
# #     subprocess.Popen(
# #         'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/Chrome_debug_temp"')
# #     input()
# #     chrome_options = Options()
# #     chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# #     chrome_driver = "chromedriver.exe"
# #     driver = webdriver.Chrome(chrome_driver, options=chrome_options)

# # except Exception as ex:
# #     print(ex)
# #     doubleagent.seleupdate(str(ex))




# seta = '피부재생'
# seta = seta.split(',')
# if isinstance(seta,list) == False:
#     seta = doubleagent.s2l(seta)

# dock = 0
# chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# chrome_driver = "chromedriver.exe"
# driver = webdriver.Chrome(chrome_driver, options=chrome_options)
# driver.switch_to.window(driver.window_handles[0])


# select = Select(driver.find_element_by_xpath(
#     '/html/body/div[2]/div[3]/div[2]/div[4]/div[1]/div[2]/select[2]'))
# select.select_by_visible_text("100개씩 보기")
# num = 1
# while True:
#     if dock == 10:

#         break
#     time.sleep(0.3)
#     driver.find_element_by_xpath(
#             '/html/body/div[2]/div[3]/div[2]/div[4]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[6]/div/a').click()
#     driver.switch_to.window(driver.window_handles[-1])
#     driver.find_element_by_xpath(
#             '/html/body/form[1]/div[7]/a[3]/span').click()
#     time.sleep(4)
#     try:
#         t=driver.find_element_by_xpath(
#                 '/html/body/form[1]/div[3]/div[7]/div[2]/div[22]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').get_attribute('value')
#         t = t.split(' ')
#         itemname = t
#         a_sub_b = [x for x in t if x not in seta]
#         a_sub_b = ' '.join(a_sub_b)
#         print(a_sub_b)
        
#         if not len(t) == len(a_sub_b):
#             driver.find_element_by_xpath(
#                         '/html/body/form[1]/div[3]/div[7]/div[2]/div[22]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').clear()
#             driver.find_element_by_xpath(
#             '/html/body/form[1]/div[3]/div[7]/div[2]/div[22]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').send_keys(a_sub_b)      
#     except:
#         driver.find_element_by_xpath(
#                     '/html/body/form[1]/div[3]/div[7]/div[2]/div[22]/div[1]/div[2]/table/tbody/tr[1]/td[1]/label/span').click()
#         t=driver.find_element_by_xpath(
#                 '/html/body/form[1]/div[3]/div[7]/div[2]/div[22]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').get_attribute('value')
#         t = t.split(' ')
#         a_sub_b = [x for x in t if x not in seta]
#         a_sub_b = ' '.join(a_sub_b)
#         print(a_sub_b)
        
#         if not len(t) == len(a_sub_b):
#             driver.find_element_by_xpath(
#                         '/html/body/form[1]/div[3]/div[7]/div[2]/div[22]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').clear()
#             driver.find_element_by_xpath(
#             '/html/body/form[1]/div[3]/div[7]/div[2]/div[22]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').send_keys(a_sub_b)            
#     driver.execute_script('document.getElementsByClassName("fToggle fMarketBasic")[11].click();')
#     while True:
#         try:
#             elem = driver.find_elements_by_xpath(
#                 '/html/body/form[1]/div[3]/div[7]/div[2]/div[22]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[1]')
#             break
#         except:
#             time.sleep(0.3)       
            
#     t=driver.find_element_by_xpath(
#                 '/html/body/form[1]/div[3]/div[7]/div[2]/div[22]/div[1]/div[2]/table/tbody/tr[12]/td[2]/div[2]/input').get_attribute('value')

#     t = t.split(',')

#     print(t)


  
#     total = []
#     while True:
#         for i,li in enumerate(itemname):
#             if i == 0:
#                 flag = li
#                 total.append(li)
#                 continue
#             flag = flag + li    
#             total.append(flag)
#         itemname = itemname[1:]
#         if len(itemname) == 0:
#             break  
#     filterer = []
#     a_sub_b = [x for x in t if x not in total]
#     a_sub_b = [x for x in a_sub_b if x not in seta]
#     a_sub_b = a_sub_b[:10]
#     a_sub_b = ','.join(a_sub_b)
#     print(a_sub_b)
#     try:
#         driver.find_element_by_xpath(
#                     '/html/body/form[1]/div[3]/div[7]/div[2]/div[22]/div[1]/div[2]/table/tbody/tr[12]/td[2]/div[2]/input').clear()
#     except:
#         driver.execute_script('document.getElementsByClassName("fToggle fMarketBasic")[11].click();')
#         driver.find_element_by_xpath(
#                     '/html/body/form[1]/div[3]/div[7]/div[2]/div[22]/div[1]/div[2]/table/tbody/tr[12]/td[2]/div[2]/input').clear()
#     driver.find_element_by_xpath(
#     '/html/body/form[1]/div[3]/div[7]/div[2]/div[22]/div[1]/div[2]/table/tbody/tr[12]/td[2]/div[2]/input').send_keys(a_sub_b)

#     driver.find_element_by_xpath(
#     '/html/body/form[1]/div[7]/a[6]').click()

#     da = Alert(driver)
#     while True:
#         try:
#             da.accept()
#             break
#         except:
#             time.sleep(1)    
#     driver.switch_to.window(driver.window_handles[0])
#     dock = dock+1

