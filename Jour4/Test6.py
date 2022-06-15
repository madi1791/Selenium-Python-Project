# lancer le navigateur
# acceder a http://www.google.ca
# Taper selenium dans la barre de recherche
# selectionner le resultat de recherche selimium webdriver
#

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.yatra.com/")

s = driver.find_element(By.XPATH, "//*[@id='BE_flight_origin_city']")
s.click()
s.send_keys("Mumb")
s.send_keys(Keys.ENTER)

sa = driver.find_element(By.XPATH, "//*[@id='BE_flight_arrival_city']")
sa.send_keys("New")
time.sleep(8)

res = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")

for e in res:
 print(e.text)

#time.sleep(6)
#driver.close()

