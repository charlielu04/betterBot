from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# scraping in background
options = Options()
options.headless = True
options.add_argument('window-size=1920x1080') #Headless = True

web = 'https://sports.tipico.de/en/live/soccer'
path = '/Applications/chromedriver' #introduce your file's path inside '...'

#execute chromedriver with edited options
driver = webdriver.Chrome(path, options=options)
driver.get(web)


#Make ChromeDriver click a button
#option 1
accept = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_evidon-accept-button"]')))
#option 2
# time.sleep(2)
# accept = driver.find_element_by_xpath('//*[@id="_evidon-accept-button"]')

#Initialize your storage
teams = []
x12 = []
btts = []
over_under = []
odds_events = []

#select values from dropdown (update 1)
dropdowns = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'SportHeader-styles-drop-down')))

first_dropdown = Select(dropdowns[0])
second_dropdown = Select(dropdowns[1])
third_dropdown = Select(dropdowns[2])

first_dropdown.select_by_visible_text('Both Teams to Score') #update 'Both teams to score?' -> 'Both Teams to Score'
second_dropdown.select_by_visible_text('Over/Under')
third_dropdown.select_by_visible_text('3-Way')

#update 2
#Looking for live events 'Program_LIVE'
box = driver.find_element_by_xpath('//div[contains(@testid, "Program_UPCOMING")]') #updated
#Looking for 'sports titles'
sport_title = box.find_element_by_class_name('SportTitle-styles-sport') #updated

# update 3 (commented code not necesssary anymore)
# for sport in sport_title:
    # selecting only football
#     if sport.text == 'Football':
parent = sport_title.find_element_by_xpath('./..') #immediate parent node
# update 4 (+3 times .find_element_by_xpath('./..'))
grandparent = parent.find_element_by_xpath('./..').find_element_by_xpath('./..').find_element_by_xpath('./..').find_element_by_xpath('./..')
#3. empty groups
try:
    empty_groups = grandparent.find_elements_by_class_name('EventOddGroup-styles-empty-group')
    empty_events = [empty_group.find_element_by_xpath('./..') for empty_group in empty_groups[:]]
except:
    pass


#Looking for single row events
single_row_events = grandparent.find_elements_by_class_name('EventRow-styles-event-row')
#4 Remove empty events from single_row_events
try:
    empty_events
    single_row_events = [single_row_event for single_row_event in single_row_events if single_row_event not in empty_events]
except:
    pass
#Getting data
for match in single_row_events:
    #'odd_events'
    odds_event = match.find_elements_by_class_name('EventOddGroup-styles-odd-groups')
    odds_events.append(odds_event)
    # Team names
    for team in match.find_elements_by_class_name('EventTeams-styles-titles'):
        teams.append(team.text)
#Getting data: the odds
for odds_event in odds_events:
    for n, box in enumerate(odds_event):
        rows = box.find_elements_by_xpath('.//*')
        if n == 0:
            x12.append(rows[0].text)
        #5 over/under + goal line
        if n == 1:
            parent = box.find_element_by_xpath('./..')
            goals = parent.find_element_by_class_name('EventOddGroup-styles-fixed-param-text').text
            over_under.append(goals+'\n'+rows[0].text)
            #6 both teams to score
            if n == 2:
                btts.append(rows[0].text)

driver.quit()

