from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import requests as requests
driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
#driver.get("https://www.aiub.edu/") #open an URL , mouse hover
#time.sleep(2)

#academic=driver.find_element(By.XPATH, "//ul[contains(@class,'menu-1')]//li//a[contains(@href,'#')][normalize-space()='Academics']")
#tution=driver.find_element(By.XPATH, "//li[contains(@class,'menu-item')]//a[normalize-space()='Tuition Fee']")

#action=ActionChains(driver)
#MouseHover Action
#action.move_to_element(academic).move_to_element(tution).click().perform()
#time.sleep(2)

#Right Click Action
#driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html") #open an URL , right click
#time.sleep(2)
#button=driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

#action=ActionChains(driver)
#action.context_click(button).perform()
#time.sleep(2)

#Double click - couldn't find the website, just see the tutorial

#Drag and Drop
#driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
#time.sleep(2)

#source= driver.find_element(By.ID, "box1")
#target= driver.find_element(By.ID, "box101")

#act=ActionChains(driver)
#act.drag_and_drop(source,target).perform()
#time.sleep(2)

#Sliders
#driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
#time.sleep(2)

#min_slider= driver.find_element(By.XPATH, "//span[1]") #{'x': 59, 'y': 250}
#max_slider= driver.find_element(By.XPATH, "//span[2]") #{'x': 545, 'y': 250}
#print("Location before sliding.....")
#print(min_slider.location)
#print(max_slider.location)

#act= ActionChains(driver)
#act.drag_and_drop_by_offset(min_slider,100,0).perform()
#act.drag_and_drop_by_offset(max_slider,-39,0).perform()

#print("Location after sliding.....")
#print(min_slider.location) #{'x': 161, 'y': 250}
#print(max_slider.location) #{'x': 506, 'y': 250}

###Scrolling###
#1.Scroll down page by Pixel
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
time.sleep(2)
#driver.execute_script("window.scrollBy(0,3000)", " ")
#value=driver.execute_script("return window.pageYOffset;")
#print("number of pixel moved", value)

#2. Scroll down page till the element is visible
#flag= driver.find_element(By.XPATH, "//img[@alt='Flag of Bangladesh']")
#driver.execute_script("arguments[0].scrollIntoView();" , flag)
#value=driver.execute_script("return window.pageYOffset;")
#print("number of pixel moved", value)

#3. Scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)
value=driver.execute_script("return window.pageYOffset;")
time.sleep(2)
print("number of pixel moved", value)