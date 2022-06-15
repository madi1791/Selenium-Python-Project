from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://www.opencart.com/index.php?route=account/register")

drop_Country = driver.find_element(By.ID,"input-country")
country = Select(drop_Country)
country.select_by_visible_text("Algeria")

country.select_by_index(5)
country.select_by_value('167')

all_options = country.options
print(len(all_options))
# for e in all_options:
#  print(e.text)

for e in all_options:
     if(e.text == "Canada"):
         e.click()
         break



