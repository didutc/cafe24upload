
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
    target = 'P0000QUP'
    firstcurrent = True
    counter = 0
    dock =50
    nameseta = 'SR,갑상선,시스테인'
    nameseta= nameseta.split(',')
    seta = '해독,감기,동맥경화,재생,관절염,발기부전,항염,TAM,새끼,구내염,항암'
    seta = seta.split(',')
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    driver.switch_to.window(driver.window_handles[0])


except Exception as ex:

    doubleagent.errorboy()




tr_lst = driver.find_elements("xpath",
    '/html/body/div[2]/div[3]/div[2]/div[4]/div[2]/div/div[2]/div/div[2]/table/tbody/tr')

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
            '/html/body/div[2]/div[3]/div[2]/div[4]/div[2]/div/div[2]/div/div[2]/table/tbody/tr')
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

            time.sleep(0.3)


    void =driver.find_element("xpath",'/html/body/div[2]/div[3]/div[2]/div[4]/div[2]/div/div[2]/div/div[2]/table/tbody/tr['+str(i)+']/td[5]').text
    print(void)
    if len(void) > 1:
        print('bnb')
        while True:

            try:
                tr_lst = driver.find_element("xpath",
                
                '/html/body/div[2]/div[3]/div[2]/div[4]/div[2]/div/div[2]/div/div[2]/table/tbody/tr['+str(i)+']/td[8]/div/a').click()
                tr_lst = driver.find_element("xpath",
                
                '/html/body/div[2]/div[3]/div[2]/div[4]/div[2]/div/div[2]/div/div[2]/table/tbody/tr['+str(i)+']/td[8]/div/a').click()
                break

            except:

                time.sleep(0.3)
        while True:

            try:
                tr_lst = driver.find_element("xpath",
                
                '/html/body/div[3]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/ul/li/a').click()

                break

            except:

                time.sleep(0.3)
        da = Alert(driver)
        while True:
            try:
                da.accept()
                break
            except:
                time.sleep(1)
        da = Alert(driver)
        while True:
            try:
                da.accept()
                break
            except:
                time.sleep(1)
                
        continue

    
    while True:

        try:
            driver.find_element("xpath",'/html/body/div[2]/div[3]/div[2]/div[4]/div[2]/div/div[2]/div/div[2]/table/tbody/tr['+str(i)+']/td[16]/button').click()
            break
        except:

            time.sleep(1)




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
        '/html/body/form[1]/div[7]/a[3]/span').click()
        

    while True:
        try:
            t = driver.find_element('xpath','/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[1]/label').get_attribute('class')
            if not 'eSelected' in t:
                name_lst = driver.find_element("xpath",

                    '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[1]/label').click()



            break
        except:
            doubleagent.errorboy()
            time.sleep(1)             


    while True:
        try:

            name_lst = driver.find_element("xpath",

                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').get_attribute('value')

 

            break
        except:
            doubleagent.errorboy()
            time.sleep(1)
    nameminus = []
    name_lst=name_lst.split(' ')
    for s in nameseta:

        for li in name_lst:

            if s in li:
                nameminus.append(li)


    namepure = doubleagent.sublist(name_lst,nameminus)

    namepure=' '.join(namepure)

    while True:
        try:

            tt = driver.find_element("xpath",

                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').clear()



            break
        except:
            doubleagent.errorboy()
            time.sleep(1)

    while True:
        try:

            tt = driver.find_element("xpath",

                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]/input').send_keys(namepure)



            break
        except:
            doubleagent.errorboy()
            time.sleep(1)

    while True:
        try:
            driver.execute_script('''window.scrollTo(0, 500)''')
            t = driver.find_element('xpath','/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[12]/td[1]/label').get_attribute('class')
            if not 'eSelected' in t:
                while True:
                    try:

                        name_lst = driver.find_element("xpath",

                            '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[12]/td[1]/label/span').click()

            

                        break
                    except:
                        doubleagent.errorboy()
                        time.sleep(1)             



            break
        except:
            time.sleep(1)
    while True:
        try:

            tt = driver.find_element("xpath",

                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[12]/td[2]/div[2]/input').get_attribute('value')

 

            break
        except:
            doubleagent.errorboy()
            time.sleep(1)
    tt_lst=tt.split(',')
    pure_lst = []
    minus = []
    print(seta)
    for s in seta:

        for li in tt_lst:

            if s in li:
                minus.append(li)


    pure = doubleagent.sublist(tt_lst,minus)

    pure=','.join(pure)

    while True:
        try:

            tt = driver.find_element("xpath",

                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[12]/td[2]/div[2]/input').clear()



            break
        except:
            doubleagent.errorboy()
            time.sleep(1)

    while True:
        try:

            tt = driver.find_element("xpath",

                '/html/body/form[1]/div[3]/div[7]/div[2]/div[23]/div[1]/div[2]/table/tbody/tr[12]/td[2]/div[2]/input').send_keys(pure)



            break
        except:
            doubleagent.errorboy()
            time.sleep(1)

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

