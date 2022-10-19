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
    soup = BeautifulSoup(page_source, 'html.parser')
    # print(soup.prettify())

    next_games = {}
    games = soup.find_all("section", {"class": "coupon-content more-info"})
    for game in games:
        teams = game.find_all("span", {"class": "name"})
        bets = game.find_all("span", {"class": "bet-price"})

        title_arr = [""] * 2
        index = 0
        for team in teams:
            title_arr[index] = str(team.contents[0])
            index += 1

        title = title_arr[0] + " | " + title_arr[1]

        bet_arr = [""] * 2
        bet_arr[0] = str(bets[len(bets) - 4].contents[0])
        bet_arr[1] = str(bets[len(bets) - 3].contents[0])

        for i in range(2):
            bet_arr[i] = bet_arr[i][1:len(bet_arr[i])-1]
        next_games[title] = bet_arr

    for key, value in next_games.items():
        print(key, ' : ', value)


website = 'https://www.bovada.lv/sports/basketball'
get_html('/usr/local/bin/chromedriver', website)
