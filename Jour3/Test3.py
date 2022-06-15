# Lancer le navigateur
# Acceder a https://www.saucedemo.com/
# Taper dans Username: standard_user
# Taper dans password: secret_sauce
# cliquer sur le bouton Login
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")

driver.find_element(By.ID,"login-button").submit()

driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)").click()

driver.find_element(By.CLASS_NAME,"shopping_cart_badge").click()

driver.find_element(By.ID,"checkout").click()
driver.find_element(By.ID, "first-name").send_keys("Braham")
driver.find_element(By.ID, "last-name").send_keys("Madi")
driver.find_element(By.ID, "postal-code").send_keys("H2S3L8")

driver.find_element(By.ID,"continue").click()
driver.find_element(By.ID,"finish").click()

# driver.find_element(By.ID,"cancel").click()
# time.sleep(6)
# driver.close()