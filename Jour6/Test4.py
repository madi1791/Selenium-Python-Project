
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.switch_to.frame('packageListFrame')
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
time.sleep(5)
driver.switch_to.default_content()

driver.switch_to.frame('packageFrame')
driver.find_element(By.LINK_TEXT,"WebDriver").click()
time.sleep(10)
driver.quit()