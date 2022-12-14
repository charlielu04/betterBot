from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# scraping in background
options = Options()
options.headless = False
options.add_argument("--start-maximized")

web = 'https://sportsbook-nj.tipico.us/home'
path = 'C:\Program Files (x86)\chromedriver.exe' #introduce your file's path inside '...'

#execute chromedriver with edited options
driver = webdriver.Chrome(path, options=options)
driver.get(web)

name = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[1]/div/main/div/div[1]/div/ul/li[1]/a/div/div[2]/div[1]/div[1]/div/span')

print(name)
driver.quit()