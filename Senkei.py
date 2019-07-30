from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

class Senkei(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "https://shogidb2.com/strategies"
        self.senkei_list = []

    def senkei(self):
        print("Senkei start")
        data = []
        self.driver.get(self.url)
        # spanタグの取得(find_elementsで複数取得)
        items = self.driver.find_elements_by_tag_name("span")
        # 取得したspanタグの文字列を展開
        for item in items:
            # 展開した文字列を追加
            data.append(item.text)

        # 要素0〜data[最大値]までループを回し、2ずつ飛ばす
        for i in range(2, len(data), 2):
            # data[i]の結果を格納
            self.senkei_list.append(data[i])

        self.driver.quit()
        # 戦型の結果が入ったリストを返す
        return self.senkei_list
