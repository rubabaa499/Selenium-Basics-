from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
driver.get("https://money.rediff.com/gainers")
time.sleep(2)
#text_msg =  driver.find_element(By.XPATH, "//a[contains(text(), 'ASM Technologies Ltd')]/self::a").text
#print(text_msg)

#text_msg =  driver.find_element(By.XPATH, "//a[contains(text(), 'ASM Technologies Ltd')]/parent::td").text
#print(text_msg)

#text_msg =  driver.find_element(By.XPATH, "//a[contains(text(), 'ASM Technologies Ltd')]/ancestor::tr/child :: td")
#print(text_msg)

text_msg=driver.find_element(By.XPATH,  "//a[contains(text(),'Hittco Tools Ltd.')]/ancestor::tr").text
print(text_msg)

#descendants=driver.find_elements(By.XPATH,  "//a[contains(text(),'IDBI Bank')]/ancestor::tr/descendant::*")
#print(len(descendants))

#followings=driver.find_elements(By.XPATH,  "//a[contains(text(),'IDBI Bank')]/ancestor::tr/following::*")
#print(len(followings))

#followingsiblings=driver.find_elements(By.XPATH,  "//a[contains(text(),'IDBI Bank')]/ancestor::tr/following-sibling::*")
#print(len(followingsiblings))

#precedings=driver.find_elements(By.XPATH,  "//a[contains(text(),'IDBI Bank')]/ancestor::tr/preceding::*")
#print(len(precedings))

#precedingsiblings=driver.find_elements(By.XPATH,  "//a[contains(text(),'IDBI Bank')]/ancestor::tr/preceding-sibling::*")
#print(len(precedingsiblings))