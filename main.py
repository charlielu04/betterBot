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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Charlie! You should be able to see this.')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
