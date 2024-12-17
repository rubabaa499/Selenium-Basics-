from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2) #Write only once, applicable for all. Can't handle exception handling
driver.get("https://www.google.com/")
#time.sleep(2) # one method of wait_command(). It has to be wriiten on each lines. Also can't handle exception error

###Time Wait###
#searchbox = driver.find_element(By.NAME, "q")
#time.sleep(2)
#searchbox.send_keys("selenium")
#time.sleep(2)
#searchbox.submit()

#driver.find_element(By.XPATH, "//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium']").click()
#time.sleep(2)

###Implicitly Wait###
#searchbox = driver.find_element(By.NAME, "q")
#searchbox.send_keys("selenium")
#searchbox.submit()
#driver.find_element(By.XPATH, "//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium']").click()

###Explicit Wait###
mywait= WebDriverWait(driver,10)
searchbox = driver.find_element(By.NAME, "q")
searchbox.send_keys("selenium")
searchbox.submit()
searchlink= mywait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium']"))).click()
driver.quit()
