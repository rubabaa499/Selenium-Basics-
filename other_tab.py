from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
import time
import requests as requests
driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
driver.get("https://www.nopcommerce.com/en/demo") #open an URL
time.sleep(2)

#opening a button on other tab but stays on first tab
#link=Keys.CONTROL+Keys.RETURN
#driver.find_element(By.XPATH, "//a[@class='btn admin-button']").send_keys(link)
#time.sleep(2)

#switching to new tab/window
#driver.get("https://www.nopcommerce.com/en/demo")
#driver.switch_to.new_window("window") #for different window
#driver.switch_to.new_window("tab") #for different tab
#driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
#time.sleep(2)