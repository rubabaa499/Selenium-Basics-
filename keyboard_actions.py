from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select
import time
import requests as requests
driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
driver.get("https://text-compare.com/") #open an URL
time.sleep(2)


inpu1=driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
input2=driver.find_element(By.XPATH, "//textarea[@id='inputText2']")
inpu1.send_keys("Welcome")
time.sleep(2)

act=ActionChains(driver)

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform() #ctrl+a
time.sleep(2)
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform() #ctrl+c
time.sleep(2)
act.send_keys(Keys.TAB).perform()
time.sleep(2)#TAB
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform() #ctrl+v
time.sleep