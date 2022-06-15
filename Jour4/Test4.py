# lancer le navigateur
import time

from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
# obtenir l url de la page
driver.get("https://demo.nopcommerce.com/")
url_pade = driver.current_url
print(url_pade)

# obtenir le titre page
titre_page = driver.title
print(titre_page)
# obtenir le code source
souce_page = driver.page_source
print(souce_page)

time.sleep(5)