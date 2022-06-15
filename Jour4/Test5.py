# lancer le navigateur
import time

from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
# driver.maximize_window()
# obtenir l url de la page
driver.get("https://demo.nopcommerce.com/")
time.sleep(3)
driver.get("http://google.com/")
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
time.sleep(3)
