from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = 'C:\Program Files (x86)\chromedriver.exe'
url = 'https://sportsbook-nj.tipico.us/live'

options = Options()
options.headless = True
options.add_argument("--start-maximized")

driver = webdriver.Chrome(path, options=options)

# result = requests.get(url)
# doc = BeautifulSoup(result.text, "html.parser")
# print(doc.prettify())

driver.get(url)
time.sleep(3)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html')
print(soup.prettify())