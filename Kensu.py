from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

def kensu():
    driver = webdriver.Chrome()
    url = 'https://shogidb2.com'
    driver.get(url)
    time.sleep(3)
    s = driver.find_element_by_id('game-count').get_attribute("textContent")
    s = s.translate(str.maketrans({'件': '', ',': ''}))
    driver.quit()
    return int(s)
