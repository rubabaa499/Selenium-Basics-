from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import requests as requests
driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/") #open an URL
time.sleep(2)

#driver.find_element(By.XPATH, "//input[@id='sunday']").click()
#time.sleep(2)

#checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
#print(len(checkboxes))


#To check all the boxes
#for checkbox in checkboxes:
#    checkbox.click()
#time.sleep(2)

#To select multiple checkboxes
#for checkbox in checkboxes:
#    weekname=checkbox.get_attribute('id')
#    if weekname=='monday' or weekname=='sunday':
#        checkbox.click()
#time.sleep(2)

#To select last two checkboxes
#for i in range(len(checkboxes)-2, len(checkboxes)):
#    checkboxes[i].click()
#time.sleep(2)

#To select first 2 checkboxes
#for i in range(len(checkboxes)):
#    if i<2:
#        checkboxes[i].click()
#time.sleep(2)

#To unselect all the checkboxes
#for checkbox in checkboxes:
#    if checkbox.is_selected():
#        checkbox.click()
#time.sleep(2)
#driver.quit()

#Broken links
#allLink = driver.find_elements(By.TAG_NAME, 'a')
#count=0

#for link in allLink:
#    url= link.get_attribute('href')
#    try:
#         res=requests.head(url)
#    except:
#        None
#    if res.status_code>=400:
#        print(url, "   is broken link")
#        count+=1
#    else:
#        print(url, "    is valid link")
#print("Total number of broken links" , count)


drp = Select(driver.find_element(By.XPATH, "//select[@id='country']"))


#drp.select_by_visible_text("India")
#time.sleep(2)



