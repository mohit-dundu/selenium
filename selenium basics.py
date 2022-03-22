import selenium as se
from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Chrome\\chromedriver_win32 (2)\\chromedriver.exe")
driver.get("https://www.google.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
#driver.close()
driver.get("https://www.netflix.com")
print(driver.title)
print(driver.current_url)
driver.back()
driver.minimize_window()
driver.close()