from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="D:\\Chrome\\chromedriver_win32 (2)\\chromedriver.exe")
driver.get("https://www.amazon.in/")
time.sleep(5)
# driver.find_element_by_class_name("_2QfC02").click()
# time.sleep(5)
#driver.find_element_by_xpath('//*[@id="nav-xshop"]/a[1]').click()
audio_el = driver.find_element_by_xpath('//*[@id="nav-subnav"]/a[5]/span[1]')
#action
time.sleep(5)