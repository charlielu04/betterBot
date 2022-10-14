from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_html(path, url):
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
    # print(soup.prettify())

    bets = soup.find_all("span", {"class": "sc-giYglK sc-kqnjJL fMUpmO eeEWlm"})
    teams = soup.find_all("span", {"class": "sc-giYglK fMUpmO sc-bBHHxi gRkMpx"})
    teams2 = soup.find_all("span", {"class": "sc-giYglK fMUpmO sc-bBHHxi emjYgw"})

    for team in teams:
        print(team.contents)
    for team in teams2:
        print(team.contents)
    for bet in bets:
        print(bet.contents)



url = 'https://sportsbook-nj.tipico.us/today'
get_html('/usr/local/bin/chromedriver', url)
