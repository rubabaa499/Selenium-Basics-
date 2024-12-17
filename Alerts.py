from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
#driver.get("https://the-internet.herokuapp.com/javascript_alerts") #open an URL
#time.sleep(2)
#driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
#time.sleep(2)

#Switching between alerts
#alertwindow = driver.switch_to.alert
#print(alertwindow.text)
#alertwindow.send_keys("Welcome")
#time.sleep(5)
#alertwindow.dismiss()
#time.sleep(2)

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(2)

#Switching between browser
driver.switch_to.window()