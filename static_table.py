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

##Counting all row and columns

no_of_rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
print(no_of_rows)
no_of_columns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th"))
print(no_of_columns)

#Read specific rows and columns
row = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[5]/td[1]").text
print(row)

#Read all the rows and columns
#print("Printing all the rows and columns data ..........")
#for r in range(2, no_of_rows+1):
#    for c in range(1, no_of_columns+1):
#        data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
#        print(data,end='      ')
#    print()

#Read Data Based on conditionsy
for r in range(2,no_of_rows+1):
    author = (driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]")).text
    if author=="Mukesh":
        bookName= (driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]")).text
        price = (driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]")).text
        print(bookName,"        ",author)

driver.close()

