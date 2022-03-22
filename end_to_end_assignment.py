from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

path = "D:\Python Scripts\Chromedriver\91\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.find_element_by_css_selector("a[href='/angularpractice/shop']").click()
mobile_name = driver.find_element_by_link_text("Blackberry").text
print(mobile_name)
if mobile_name == "Blackberry":
    mobile_name = driver.find_elements_by_xpath("//div[@class='card h-100']")
for mobile in mobile_name:
    #if mobile.find_element_by_link_text("Blackberry").text == "Blackberry":
    if mobile.find_element_by_css_selector("h4.card-title").text == "Blackberry":
        mobile.find_element_by_css_selector("button.btn.btn-info").click()
driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click()
driver.find_element_by_css_selector("button[class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("Ind")
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located(By.LINK_TEXT, "India"))
driver.find_element_by_link_text("India").click()
