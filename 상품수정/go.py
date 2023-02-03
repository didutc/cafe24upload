
from selenium.webdriver.common.alert import Alert
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
import doubleagent
from selenium.webdriver.support.select import Select
try:
    subprocess.Popen(
        'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/Chrome_debug_temp"')

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)

except Exception as ex:
    print(ex)

    doubleagent.seleupdate(str(ex))
