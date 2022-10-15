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

    all_games = {}
    games = soup.find_all("div", {"class": "sc-gLEhor dMmBXC"})
    for game in games:
        bets = game.find_all("div", {"class": "sc-czvZiG hxbcXJ"})
        if len(bets) == 0:
            continue
        teams = game.find_all("span", {"class": "sc-giYglK fMUpmO sc-bBHHxi gRkMpx"})
        teams2 = game.find_all("span", {"class": "sc-giYglK fMUpmO sc-bBHHxi emjYgw"})
        bets = game.find_all("span", {"class": "sc-giYglK sc-kqnjJL fMUpmO eeEWlm"})

        title_arr = [""] * 2
        index = 0
        if len(teams) > 0:
            for team in teams:
                title_arr[index] = str(team.contents[0])
                index += 1
        else:
            for team in teams2:
                title_arr[index] = str(team.contents[0])
                index += 1

        title = title_arr[0] + " | " + title_arr[1]

        bet_arr = [""] * 2

        bet_arr[0] = int(str(bets[len(bets) - 2].contents[0]))
        bet_arr[1] = int(str(bets[len(bets) - 1].contents[0]))

        all_games[title] = bet_arr

    for key, value in all_games.items():
        print(key, ' : ', value)


url = 'https://sportsbook-nj.tipico.us/today'
get_html('/usr/local/bin/chromedriver', url)
