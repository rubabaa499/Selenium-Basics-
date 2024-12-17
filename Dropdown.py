from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import requests as requests
driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/") #open an URL
time.sleep(2)

driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()
time.sleep(2)

countries_list = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']")
#print(len(countries_list))

for country in countries_list:
    if country.text=="India":
        country.click()
        break


