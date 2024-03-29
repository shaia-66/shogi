from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

def kensu():
    print("Kensu start")
    driver = webdriver.Chrome()
    url = 'https://shogidb2.com'
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located)
    s = driver.find_element_by_id('game-count').get_attribute("textContent")
    s = s.translate(str.maketrans({'件': '', ',': ''}))
    driver.quit()
    return int(s)
