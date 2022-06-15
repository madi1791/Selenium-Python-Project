from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("http://omayo.blogspot.com/")

drop_Country = driver.find_element(By.ID,"multiselect1")
country = Select(drop_Country)
country.select_by_visible_text("Volvo")

country.select_by_index(3)
country.select_by_value('swiftx')

country.deselect_by_visible_text("Swift")

all_options = country.options
print(len(all_options))

for e in all_options:
    print (e.text)

for e in all_options:
     if(e.text == "Volvo"):
         print ("Yesssss")
         break