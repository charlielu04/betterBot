from selenium import webdriver

driver = webdriver.chrome
PATH = "/Applications/chromedriver"

driver = webdriver.Chrome(PATH)
driver.get("https://apple.com")