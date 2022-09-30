from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.headless = True
options.add_argument('window-size=1920x1080')

""" Decides whether or not you should bet, prints bet amount and winnings if any

:param site1, site2: American odds from each site
:type site1, site2: tuple
:returns: True for should bet, False for should not bet
:rtype: boolean
"""


def should_bet(site1, site2):
    # calculates decimal odds given American odds and stores in tuple
    odds1 = (calc_odds(site1[0]), calc_odds(site1[1]))
    odds2 = (calc_odds(site2[0]), calc_odds(site2[1]))

    # calculates if implied prob is less than 1
    # split if statement this way so that bet_amount always corresponds x[0] to site 1 and x[1] to site 2
    if 1 / odds1[0] + 1 / odds2[1] < 1:
        x = bet_amount(odds1[0], odds2[1])
        y = bet_amount_for_profit(odds1[0], odds2[1])
        print("If you bet $500, you should bet " + str(x[0]) + " in team 1 on site 1 and " + str(x[1]) + " in team 2 on"
              + " site 2 for a " + str(calc_profit(odds1[0], odds2[1])) + " dollar profit, which is a "
              + str(calc_profit_p(odds1[0], odds2[1])) + "% increase. \n" +
              "If you want to make $50, you should bet $" + str(y[0] + y[1]) + ", $"
              + str(y[0]) + " in team 1 and $" + str(y[1]) + " in team 2.")
        return True
    elif 1 / odds1[1] + 1 / odds2[0] < 1:
        x = bet_amount(odds1[1], odds2[0])
        y = bet_amount_for_profit(odds1[1], odds2[0])
        print("If you bet $500, you should bet " + str(x[0]) + " in team 1 on site 1 and " + str(x[1]) + " in team 2 on"
              + " site 2 for a " + str(calc_profit(odds1[1], odds2[0])) + " dollar profit, which is a "
              + str(calc_profit_p(odds1[1], odds2[0])) + "% increase. \n" +
              "If you want to make $50, you should bet $" + str(y[0] + y[1]) + ", $"
              + str(y[0]) + " in team 1 and $" + str(y[1]) + " in team 2.")
        return True
    return False


""" Calculates decimal odd given American odd for a single team
:param money: American odd from website for a single team
:type money: double 
:returns: Decimal odds for a single team
:rtype: double
"""


def calc_odds(money):
    return (-money + 100) / (-money) if money < 0 else (money + 100) / 100


""" Calculates absolute winnings given decimal odds and bet size

:param odds1, odds2: Decimal odds
:type odds1, odds2: double
:param bet_size: How much bet total
:type bet_size: double
:returns: Absolute winnings
:rtype: double
"""


def calc_profit(odds1, odds2, bet_size=500):
    return round(bet_size * odds2 * odds1 / (odds1 + odds2) - bet_size, 2)


""" Calculates percentage winnings given decimal odds

:param odds1, odds2: Decimal odds for teams 
:type odds1, odds2: double
:returns: percentage winnings * 100
:rtype: double
"""


def calc_profit_p(odds1, odds2):
    return round((odds2 * odds1 / (odds1 + odds2) - 1) * 100, 4)


""" Calculates amount to bet in each website given total desired bet size and odds


:param odds1, odds2: Decimal odds for each site in order of site (odds1 from site1, odds2 from site2) 
:type odds1, odds2: double
:param bet_size: Total desired bet size for entire match
:type bet_size: double
:returns: Amount to bet on each website respectively
:rtype: 2-tuple (first element corresponds to bet on first website, and similarly for second)  
"""


def bet_amount(odds1, odds2, bet_size=500):
    return round(bet_size * odds2 / (odds1 + odds2), 2), round(bet_size * odds1 / (odds1 + odds2), 2)


""" Calculates amount to bet in each website given total desired profit


:param odds1, odds2: Decimal odds for each site in order of site (odds1 from site1, odds2 from site2) 
:type odds1, odds2: double
:param profit: Total desired profit
:type profit: double
:returns: Amount to bet on each website respectively
:rtype: 2-tuple (first element corresponds to bet on first website, and similarly for second)
"""
def bet_amount_for_profit(odds1, odds2, profit=50):
    return bet_amount(odds1, odds2, round(100 * profit / calc_profit_p(odds1, odds2), 2))


# Tested with Federer, Thiem example from https://www.us-odds.com/guides/arbitrage-betting

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    should_bet((-200, 150), (-125, 120))
    should_bet((-125, 120),(-200, 150))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
