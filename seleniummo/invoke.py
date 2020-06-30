from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\amit\\chromedriver.exe")

driver.get("https://www.google.com/")

print(driver.title)
print(driver.current_url)

driver.minimize_window()








