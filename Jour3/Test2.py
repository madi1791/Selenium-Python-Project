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
driver.find_element(By.CLASS_NAME,"ico-login").click()
driver.find_element(By.ID, "Email").send_keys("braham@bdeb.com")
driver.find_element(By.ID, "Password").send_keys("gfgfgfd")
# driver.find_element(By.CLASS_NAME,"button-1 login-button").submit()
driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()

time.sleep(6)
driver.close()