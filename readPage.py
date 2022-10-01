from selenium import webdriver
import time


driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver')  # Optional argument, if not specified will search path.

driver.get("https://apple.com")
print(driver.title)
time.sleep(10)

driver.quit()
