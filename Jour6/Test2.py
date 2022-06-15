
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH, "//button[contains(text(),'Confirm')]").click()

alertWindow = driver.switch_to.alert
print(alertWindow.text)
alertWindow.dismiss()

driver.quit()