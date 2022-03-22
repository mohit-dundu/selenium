#Types:
#1. Implicit wait
#2. Explicit wait
#3. pause the test using sleep

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

path = "D:\Python Scripts\Chromedriver\91\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
print(driver.find_elements_by_xpath("//div[@class='products']/div"))
print(count)
add_to_cart = driver.find_elements_by_xpath("//div[@class='products']//div[@class='product-action']//button")
for items in add_to_cart:
    items.click()
cart_icon = driver.find_element_by_xpath("//img[@alt='Cart']").click()
checkout = driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()


wait = WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
promo_code = driver.find_element_by_xpath("//div//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element_by_xpath("//button[@class='promoBtn']").click()
print(driver.find_element_by_css_selector("span.promoinfo").text)
# promo_code = driver.find_element_by_class_name('promoCode').send_keys("rahulshettyacademy")
