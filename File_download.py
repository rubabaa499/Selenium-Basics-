from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def chrome_setup(): #for edge and firefox same also
    driver = webdriver.Chrome()
    time.sleep(2)
    return driver

drive = chrome_setup()
drive.get("link")
drive.maximize_window()
drive.find_element(By.XPATH, "path").click()

