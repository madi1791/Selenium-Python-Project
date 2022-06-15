# lancer le navigateur
# acceder a https://github.com/madi1791/cv.git
# cliquer sur register
# remplir le formulaire
# cliquer sur le bouton register
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
# driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Regi").click()
driver.find_element(By.ID, "FirstName").send_keys("Braham")
driver.find_element(By.NAME, "LastName").send_keys("Madi")
driver.find_element(By.ID, "Email").send_keys("braham@bdeb.com")
driver.find_element(By.ID, "Password").send_keys("gfgfgfd")
driver.find_element(By.ID, "ConfirmPassword").send_keys("gfgfgfd")
driver.find_element(By.ID,"register-button").submit()

time.sleep(6)
driver.close()