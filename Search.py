from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

import Article

class Search(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "https://shogidb2.com"
        self.link_list = []

    # searchのなかで、各URLのページをクリックし、全ての掲載情報を取得する必要がある
    def search(self, kensu):
        print('Search start')
        at = Article.Article()
        for i in range(1, kensu+1):
            # ここでページの切り替え処理
            self.driver.get(self.url + '/latest/page/' + str(i))
            lists = self.driver.find_elements_by_class_name("list-group")
            for list in lists:
                hrefs = list.find_elements_by_tag_name("a")
                # hrefsの展開
                for href in hrefs:
                    # hrefの中にあるhrefタグを格納
                    self.link_list.append(href.get_attribute("href"))

            # ここでArticleを読んで各URLの詳細情報・棋譜情報・評価情報をもらう必要がある
            at.article(self.link_list)
            self.link_list = []
        self.driver.quit()
