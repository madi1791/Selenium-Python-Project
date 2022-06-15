import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
parentWindowId = driver.current_window_handle
#l'identifiant de la fentre principale est : CDwindow-84CF82CAF8E524F1E894C3E1C8415E7D
print(parentWindowId)

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()

windowHandlesIds = driver.window_handles
parentWindowId = windowHandlesIds[0]
childWindowId = windowHandlesIds[1]
print("Parent: ", parentWindowId)
print("Child: ",childWindowId)
driver.switch_to.window(childWindowId)
url1= driver.current_url
tiltle1 = driver.title
print(url1)
print(tiltle1)

# 2 eme approche
for winId in windowHandlesIds:
    driver.switch_to.window(winId)
    if driver.title == tiltle1:
        driver.close()

time.sleep(10)
driver.quit()