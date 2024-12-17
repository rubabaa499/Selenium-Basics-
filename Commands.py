from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/") #open an URL
time.sleep(2)

#Application commands
#print(driver.title) #to capture the title
#print(driver.current_url) # to capture current URL
#print(driver.page_source) #to capture source page

#Conditional commands
#searchbox = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
#print("Display status", searchbox.is_displayed())
#print("Enable status", searchbox.is_enabled())

#rd_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
#rd_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")
#print("before selecting radio button status..")
#print(rd_male.is_selected())
#print(rd_female.is_selected())

#rd_male.click()

#print("after selecting radio button status..")
#print(rd_male.is_selected())
#print(rd_female.is_selected())



#Browser command
#driver.find_element(By.LINK_TEXT, "nopCommerce").click()
#driver.close()
#driver.quit()

#Navigational
#driver.get("https://www.flipkart.com/")
#driver.get("https://www.amazon.com/")
#driver.back()
#time.sleep(2)
#driver.forward()
#time.sleep(2)
#driver.refresh()
#time.sleep(2)
#driver.close()

#Find element
#Locator with single element
#element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
#element.send_keys("Apple watch")
#time.sleep(2)

#Locator with multiple web elements
element = driver.find_element(By.XPATH, "//div[@class='footer-block information']//div[@class='title']")
print(element.text)

#Locator with multiple elements
element = driver.find_elements(By.XPATH, "//div[@class='footer-block information']//div[@class='title']")
print(len(element))