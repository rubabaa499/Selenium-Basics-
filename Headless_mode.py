from selenium import webdriver
import time

def headless_chrome(): # Same goes for Edge and Firefox
    driver = webdriver.Chrome()
    driver.headless= True
    time.sleep(2)
    return driver
driver=headless_chrome()
driver.get("https://www.nopcommerce.com/en/demo")
print(driver.title)
print(driver.current_url)
driver.close()
