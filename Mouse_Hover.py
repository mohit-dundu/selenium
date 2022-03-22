from selenium import webdriver
import time

from selenium.webdriver import ActionChains

path = "D:\Python Scripts\Chromedriver\91\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
hover = driver.find_element_by_id("mousehover")
action = ActionChains(driver)
action.move_to_element(hover).perform()
top = driver.find_element_by_link_text("Top")
action.move_to_element(top).click().perform()

#top double click
action.double_click('element_name').perform()
