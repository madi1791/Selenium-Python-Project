# Lancer le navigateur
# Acceder a http://www.google.ca
# Taper selenium dans la barre de recherche
# selectionner le resultat de recherche selimium webdriver

import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.google.ca/")

s = driver.find_element(By.NAME, "q")
s.send_keys("selenium")

time.sleep(3)
res = driver.find_elements(By.XPATH, "//ul[@role='listbox']//li/descendant::div[@class='wM6W7d']")

print(len(res))
for e in res:
    print(e.text)

for e in res:
    if (e.text == "selenium webdriver"):
        e.click()
        break

#time.sleep(6)
#driver.close()