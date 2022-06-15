#Test Case
#------------------
# 1) Ouvrir le navigateur(chrome/firefox/Edge)
# 2) Naviguer vers l'url https://opensource-demo.orangehrmlive.com/
# 3) Entrer username (Admin)
# 4) Entrer password (admin123)
# 5) Cliquer sur le bouton Login
# 6) recuperer le titre de la page(titre actuel)
# 7) Verifier le titre de la page: OrangeHRM  (attendu)
# 8) Fermer le navigateur
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

##service_obj = Service("C:\\Users\\madi7\\Downloads\\chromedriver_win32\\chromedriver.exe")

# 1) Ouvrir le navigateur(chrome/firefox/Edge)
##driver = webdriver.Chrome(service=service_obj)

# 2) Naviguer vers l'url https://opensource-demo.orangehrmlive.com/
driver=webdriver.Chrome()
driver.get("https://login.salesforce.com/?locale=fr-ca")
# driver.maximize_window()
# 3) Entrer username (Admin)
driver.find_element(By.ID, "username").send_keys("Admin")
driver.find_element(By.ID, "password").send_keys("Admin")
driver.find_element(By.ID, "Login").click()
act_title =  driver.title
print(act_title)
msg=driver.find_element(By.ID,"error")
print(msg.text)
#exp_title = "OrangeHRM"

#time.sleep(4)
#driver.close()