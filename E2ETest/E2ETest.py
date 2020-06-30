from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\amit\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/shop")

driver.implicitly_wait(10)

shop = driver.find_element_by_xpath("//a[@href='/angularpractice/shop']")

shop.click()

products = driver.find_elements_by_xpath("//div[@class='card h-100']")


for product in products:
    productName = product.find_element_by_xpath("div/h4/a").text
    if productName == "Blackberry":
        product.find_element_by_xpath("div/button").click()


driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']")
driver.find_element_by_css_selector("button[class*='btn-success']").click()
driver.find_element_by_css_selector("#country").send_keys("ind")
wait= WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located(By.LINK_TEXT, "India"))
driver.find_element_by_link_text("India").click()








