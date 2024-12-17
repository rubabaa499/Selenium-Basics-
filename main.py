# My first test
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
driver.get("https://gormg-v3-staging.skylarksoft.net/login")
time.sleep(2)
driver.find_element(By.ID, "email").send_keys("rubaba@gmail.com")
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("123456")
time.sleep(2)
driver.find_element(By.ID, "login").click()
time.sleep(2)
act_title = driver.title
exp_title = "Dashboard | ERP | PROTRACKER | AQAI | SKYLARK"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login failed")
driver.close()
