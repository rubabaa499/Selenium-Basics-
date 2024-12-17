from selenium import webdriver
import time

driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
driver.get("https://www.nopcommerce.com/en/demo") #open an URL
time.sleep(2)

cookies= driver.get_cookies()
print("Size of cookies :", len(cookies)) #4

#for c in cookies:
#    #print(c)
#    print(c.get("name"), ":" , c.get("value"))

#Adding cookies to browser
driver.add_cookie({"name":"My Cookie", "value":"1234"})
cookies=driver.get_cookies()
print("Size of cookies after adding new one:",len(cookies)) #5

#Deleting cookies from browser
driver.delete_cookie("My Cookie")
cookies=driver.get_cookies()
print("size of cookie after delete :" , len(cookies)) #4

#Deleting all cookies
driver.delete_all_cookies()
cookies=driver.get_cookies()
print("size of cookies after deleting all cookies:" , len(cookies))#0

driver.quit()
