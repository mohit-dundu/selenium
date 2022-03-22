from selenium import webdriver
import time

path = "D:\Python Scripts\Chromedriver\91\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://www.jira.ford.com")
time.sleep(5)
driver.find_element_by_xpath("//*[contains(text(), 'Active Directory')]").click()
driver.find_element_by_id("userNameInput").send_keys("UserID")
driver.find_element_by_id("passwordInput").send_keys("Password")
driver.find_element_by_id("submitButton").click()
