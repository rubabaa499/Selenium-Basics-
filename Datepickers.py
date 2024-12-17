from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import requests as requests
driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
#driver.get("https://jqueryui.com/datepicker/") #open an URL
time.sleep(2)

#driver.switch_to.frame(0)
#driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("05/03/2024") #without logic


#year="2022"
#month="March"
#date="30"

#driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

#while True:
#    mon=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
#    yr=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

#    if mon==month and yr==year:
#        break;
#    else:
#        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()

#select dates
#dd=driver.find_element(By.XPATH, "//table[@class='ui-datepicker-calendar']//tbody/tr/td/a")
#for ele in date:
#    if ele==date:
#        ele.click()
#        break

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='dob']").click()

datepicker_month = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
datepicker_month.select_by_visible_text("Dec")

datepicker_yr = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
datepicker_yr.select_by_visible_text("2024")

alldates= driver.find_element(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for date in alldates:
    if date.text=="25":
        date.click()
        break

time.sleep(2)
