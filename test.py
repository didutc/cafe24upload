

from selenium.webdriver.common.alert import Alert
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
import doubleagent
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
driver.switch_to.window(driver.window_handles[-1])

t = driver.find_element('xpath','/html/body/div[2]/div[3]/div[2]/div[4]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[10]/td[5]').text
print(len(t))
t = driver.find_element('xpath','/html/body/div[2]/div[3]/div[2]/div[4]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[5]/td[5]').text
print(t)

