from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
driver.get("https://www.youtube.com/")
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input" ).send_keys("selenium")
time.sleep(2)
