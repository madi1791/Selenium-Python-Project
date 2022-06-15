import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Frames.html")
driver.find_element(By.XPATH,"//a[contains(text(),'Single Iframe')]").click()

driver.find_element(By.XPATH,"//input").send_keys("test")

driver.switch_to.frame("//iframe[@id='singleframe']")
#
# time.sleep(5)
# driver.switch_to.default_content()
#
# driver.switch_to.frame('packageFrame')
# driver.find_element(By.LINK_TEXT,"WebDriver").click()
# time.sleep(10)
# driver.quit()