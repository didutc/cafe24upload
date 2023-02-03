
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

#     chrome_options = Options()
#     chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#     chrome_driver = "chromedriver.exe"
#     driver = webdriver.Chrome(chrome_driver, options=chrome_options)

# except Exception as ex:
#     doubleagent.errorboy()



try:
    lastchild = False
    target = 'P0000SSP'
    firstcurrent = True
    counter = 0
    dock =4
    seta = '기타영양제'
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    driver.switch_to.window(driver.window_handles[0])


except Exception as ex:

    doubleagent.errorboy()

select = Select(driver.find_element("xpath",'/html/body/div[2]/div[3]/div[2]/div[3]/div[1]/div[2]/select'))
select.select_by_visible_text("10개씩 보기")
time.sleep(0.3)
tr_lst = driver.find_elements("xpath",
    '/html/body/div[2]/div[3]/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/table/tbody/tr')
findernext = False
targeti = False
nectar = False
num_list = []
for li in tr_lst:
    tr = li.text
    tr = tr.split('\n')[0]
    num_list.append(tr)
num_list=num_list[:dock]


for num in num_list:
    while True:

        try:
            tr_lst = driver.find_elements("xpath",
            '/html/body/div[2]/div[3]/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/table/tbody/tr')
            if len(tr_lst) ==0:
                continue
            for i,li in enumerate(tr_lst,start=1):
                tr = li.text

                tr = tr.split('\n')[0]

                if num == tr:
                    print('ok')
                    break

            break

        except:
            dacounter1 = dacounter1+1
            time.sleep(0.3)




    driver.find_element("xpath",'/html/body/div[2]/div[3]/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/table/tbody/tr['+str(i)+']/td[3]/div/a[1]/span').click()





# 여기서부터는 내일부터 시나리오는 맨 마직막 상품을 업로드 하면 다음페이지에 없으니 이것을 참조하는 루틴을 짜자
# 판명하는것은

    driver.switch_to.window(driver.window_handles[-1])
    driver.maximize_window()
    da = Alert(driver)
    dacounter1 = 0
    while True:
        if dacounter1 == 2:
            break
        try:
            da.accept()
            break
        except:
            dacounter1 = dacounter1+1
            time.sleep(1)

    elem = driver.find_element("xpath",
        '/html/body/form[1]/div[2]/div[4]/div[3]/div[3]/div[1]/span[1]/button[2]').click()
        
    elem = driver.find_element("xpath",
        '/html/body/form[1]/div[2]/div[4]/div[3]/div[3]/div[2]/div[2]/input').click()
    elem = driver.find_elements("xpath",
        '/html/body/form[1]/div[2]/div[4]/div[3]/div[3]/div[2]/div[2]/div/ul/li')

    while True:
        try:
            for li in range(0, len(elem)-1):
                text = driver.find_element("xpath",

                    '/html/body/form[1]/div[2]/div[4]/div[3]/div[3]/div[2]/div[2]/div/ul/li['+str(li+2)+']/a/strong').text
                if seta == text:
                    setan = str(li+2)
            break
        except:
            time.sleep(1)
    driver.find_element("xpath",

        '/html/body/form[1]/div[2]/div[4]/div[3]/div[3]/div[2]/div[2]/div/ul/li['+setan+']').click()
    da = Alert(driver)
    dacounter1 = 0
    while True:
        if dacounter1 == 2:
            break
        try:
            da.accept()
            break
        except:
            time.sleep(1)
            dacounter1 = dacounter1+1
    driver.find_element("xpath",
        '/html/body/form[1]/div[7]/a[3]').click()
    elem = driver.find_elements("xpath",
        '/html/body/form[1]/div[3]/div[7]/div[1]/div/ul/li')
    error_list = []
    for i, li in enumerate(elem):

        if '경고' in li.text:
            q = li.text.split('\n')
            error_list.append([q[0], i+1])
    countt = 0

    while True:

        if countt == 3:
            break
        if len(error_list) == 0:
            error_list = []
            time.sleep(1)
            elem = driver.find_elements("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[1]/div/ul/li')
            countt = countt + 1

        for i, li in enumerate(elem):

            if '경고' in li.text:
                q = li.text.split('\n')
                error_list.append([q[0], i+1])
        if len(error_list) != 0:
            break
    # [['1', 'G마켓(didutc)'], ['2', '옥션(didutc)'], ['3', '11번가(didutc)'], ['5', '인터파크(didutc2)'], ['9', '위메프(didutc)'], ['11', '티몬(didutc)'], ['12', '롯데ON(didutc1)']]
    for li in error_list:
        print(li)
        if li[0] == 'G마켓(didutc)':
               
            test = driver.find_element("xpath",
  
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').get_attribute('value')
            while True:
                if len(test.encode('euc-kr')) > 50:
                    test = test.split(' ')[:-1]
                    test = ' '.join(test)

                else:
                    break
            driver.find_element("xpath",
 
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').clear()

            test = driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').send_keys(test)
        if li[0] == '옥션(didutc)':
            driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[1]/div/ul/li['+str(li[1])+']/div/span').click()

            while True:
                try:
                    test = driver.find_element("xpath",
                        '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input')
                    break
                except:
                    time.sleep(1)
            test = driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').get_attribute('value')
            while True:
                if len(test.encode('euc-kr')) > 50:
                    test = test.split(' ')[:-1]
                    test = ' '.join(test)

                else:
                    break
            driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').clear()

            test = driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').send_keys(test)

        if li[0] == '11번가(didutc)':
            driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[1]/div/ul/li['+str(li[1])+']/div/span').click()

            while True:
                try:
                    test = driver.find_element("xpath",
                        '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[1]/label/span').click()
                    break
                except:
                    time.sleep(1)
            while True:
                try:
                    test = driver.find_element("xpath",
                        '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input')
                    break
                except:
                    time.sleep(1)
            test = driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').get_attribute('value')
            while True:
                if len(test.encode('euc-kr')) > 100:
                    test = test.split(' ')[:-1]
                    test = ' '.join(test)

                else:
                    break

            driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').clear()

            test = driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').send_keys(test)

        if li[0] == '스마트스토어(ncp_1nt5yq_01)':
            driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[1]/div/ul/li['+str(li[1])+']/div/span').click()

            while True:
                try:
                    test = driver.find_element("xpath",
                        '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[1]/label/span').click()
                    break
                except:
                    time.sleep(1)
            while True:
                try:
                    test = driver.find_element("xpath",
                        '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input')
                    break
                except:
                    time.sleep(1)
            test = driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').get_attribute('value')
            while True:
                if len(test.encode('euc-kr')) > 100:
                    test = test.split(' ')[:-1]
                    test = ' '.join(test)

                else:
                    break

            driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').clear()

            test = driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').send_keys(test)


        if li[0] == '인터파크(didutc2)':
            driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[1]/div/ul/li['+str(li[1])+']/div/span').click()

            while True:
                try:
                    test = driver.find_element("xpath",
                        '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[1]/label/span').click()
                    break
                except:
                    time.sleep(1)
            while True:
                try:
                    test = driver.find_element("xpath",
                        '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input')
                    break
                except:
                    time.sleep(1)
            test = driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').get_attribute('value')
            while True:
                if len(test.encode('euc-kr')) > 50:
                    test = test.split(' ')[:-1]
                    test = ' '.join(test)

                else:
                    break

            driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').clear()

            test = driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').send_keys(test)
        if li[0] == '카카오톡 스토어(didutc)':
            driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[1]/div/ul/li['+str(li[1])+']/div/span').click()

            while True:
                try:
                    test = driver.find_element("xpath",
                        '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[1]/label/span').click()
                    break
                except:
                    time.sleep(1)
            while True:
                try:
                    test = driver.find_element("xpath",
                        '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input')
                    break
                except:
                    time.sleep(1)
            test = driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').get_attribute('value')
            while True:
                if len(test) > 50:
                    test = test.split(' ')[:-1]
                    test = ' '.join(test)

                else:
                    break

            driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').clear()

            test = driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').send_keys(test)

        if li[0] == '위메프(didutc)':
            driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[1]/div/ul/li['+str(li[1])+']/div/span').click()

            while True:
                try:
                    test = driver.find_element("xpath",
                        '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[1]/label/span').click()
                    break
                except:
                    time.sleep(1)
            while True:
                try:
                    test = driver.find_element("xpath",
                        '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input')
                    break
                except:
                    time.sleep(1)
            test = driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').get_attribute('value')
            while True:
                if len(test) > 70:
                    test = test.split(' ')[:-1]
                    test = ' '.join(test)

                else:
                    break

            driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').clear()

            test = driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').send_keys(test)
        if li[0] == '티몬(didutc)':
            driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[1]/div/ul/li['+str(li[1])+']/div/span').click()

            while True:
                try:
                    test = driver.find_element("xpath",
                        '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[1]/label/span').click()
                    break
                except:
                    time.sleep(1)
            while True:
                try:
                    test = driver.find_element("xpath",
                        '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input')
                    break
                except:
                    time.sleep(1)
            test = driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').get_attribute('value')
            while True:
                if len(test) > 60:
                    test = test.split(' ')[:-1]
                    test = ' '.join(test)

                else:
                    break

            driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').clear()

            test = driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').send_keys(test)
        if li[0] == '롯데ON(didutc1)':
            driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[1]/div/ul/li['+str(li[1])+']/div/span').click()

            while True:
                try:
                    test = driver.find_element("xpath",
                        '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[1]/label/span').click()
                    break
                except:
                    time.sleep(1)
            while True:
                try:
                    test = driver.find_element("xpath",
                        '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input')
                    break
                except:
                    time.sleep(1)
            test = driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').get_attribute('value')
            while True:
                if len(test.encode('euc-kr')) > 69:
                    test = test.split(' ')[:-1]
                    test = ' '.join(test)

                else:
                    break
            driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').clear()

            driver.find_element("xpath",
                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').send_keys(test)

    # driver.find_element("xpath",
    #     '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').clear()

    # test = driver.find_element("xpath",
    #     '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').send_keys(test)


    # 네이버 끝
    driver.find_element("xpath",
        '/html/body/form[1]/div[7]/a[6]/span').click()
    da = Alert(driver)
    while True:
        try:
            da.accept()
            break
        except:
            time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
  
