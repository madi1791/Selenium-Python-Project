from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
#set chromodriver.exe path
driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
driver.get("https://www.google.com/")


element =driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")

element.send_keys("selenium");
element.submit();
""" 
results = driver.find_element(By.XPATH, "//div[@class='g']//div[@class='r']//a[not(@class)]")
for result in results:
    print(result.get_attribute("href"))
"""