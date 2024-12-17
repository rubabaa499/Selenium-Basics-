import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import requests as requests
driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
driver.get("https://www.nopcommerce.com/en/demo") #open an URL
time.sleep(2)

driver.save_screenshot("path + location")
driver.save_screenshot(os.getcwd()+"")
driver.get_screenshot_as_file(os.getcwd()+"")


