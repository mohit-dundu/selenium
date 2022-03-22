#https://www.rahulshettyacademy.com/angularpractice/
import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="D:\\Python Scripts\\Chromedriver\\91\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
#driver.find_element_by_name("name").send_keys("Selenium Practice")
## CSS Example
driver.find_element_by_css_selector("input[name='name']").send_keys("Selenium Practice")
driver.find_element_by_name("email").send_keys("Selenium.Practice@gmail.com")
# Select class for handling dropdowns
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
#dropdown.select_by_visible_text("Female")
# OR
dropdown.select_by_index(0)


driver.find_element_by_id("exampleInputPassword1").send_keys("SeleniumPractice")
## To clear elements in a box
driver.find_element_by_id("exampleInputPassword1").clear()
driver.find_element_by_id("exampleInputPassword1").send_keys("SeleniumPractice")
driver.find_element_by_id("exampleCheck1").click()
#driver.close()
driver.find_element_by_xpath("//input[@type='submit']").click()
message = driver.find_element_by_class_name("alert-success").text
assert "Succsess" in message
