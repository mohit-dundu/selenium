from selenium import webdriver

import time

path = "D:\Python Scripts\Chromedriver\91\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
elements = driver.find_elements_by_css_selector("input[type='checkbox']")
print(len(elements))
for box in elements:
    box.click()
    assert box.is_selected()
#select checkbox with only option 2
for box in elements:
    if box.get_attribute("value") == "option2":
        box.click()
        assert box.is_selected()
# Selecting Radion buttons
driver.find_element_by_css_selector("input[value='radio3']").click()

