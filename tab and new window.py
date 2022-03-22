from selenium import webdriver
import time

path = "D:\Python Scripts\Chromedriver\91\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_css_selector("a[href='/windows/new']").click()
child_window = driver.window_handles[1]
driver.switch_to.window(child_window)
print(driver.find_element_by_tag_name("h3").text)
driver.close()
driver.switch_to.window(driver.window_handles[0])
text1 = driver.find_element_by_tag_name("h3").text
assert "Opening a new window" == text1