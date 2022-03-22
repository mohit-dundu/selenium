from selenium import webdriver
import time

path = "D:\Python Scripts\Chromedriver\91\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_css_selector("#name").send_keys("Options")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert()
print(alert.text)
alert.accept() ## .dismiss() to click on "Cancel"
