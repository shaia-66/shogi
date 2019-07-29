from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

import Article

class Search(object):
    def __init__(self):
        # driverの紐付け
        self.driver = webdriver.Chrome()
        # 将棋DB2のトップページ
        self.url = "https://shogidb2.com"
        self.link_list = []

    # searchのなかで、各URLのページをクリックし、全ての掲載情報を取得する必要がある
    def search(self, kensu):
        print('Search start')
        page_cnt = 5
        at = Article.Article()
        time.sleep(3)
        for i in range(1, kensu+1):
            # ここでページの切り替え処理
            self.driver.get(self.url + '/latest/page/' + str(i))
            time.sleep(3)
            print("iのなかみ > " + str(i))

            # for j in range(page_cnt):
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
            # print("jのなかみ > " + str(j))
        self.driver.quit()




        # print("Search start")
        # # ページを開く
        # self.driver.get(self.url)
        # # 5秒まで待機
        # WebDriverWait(self.driver, 2).until(EC.presence_of_element_located)
        # # 最低件数
        # low = 0
        # # 最大件数
        # high = 20
        # # ページ数
        # page = 1
        #
        # at = Article.Article()
        #
        # # keysを展開
        # for key in keys:
        #     # 検索窓の取得
        #     search_get = self.driver.find_element_by_name("q")
        #     # 展開したキーワードを検索窓に書き込み
        #     search_get.send_keys(key)
        #     # 検索ボタンの実行
        #     self.driver.find_element_by_css_selector('button.btn').click()
        #
        #     # 最大件数の取得
        #     max = self.driver.find_element_by_css_selector("h1.h2.mb-4").get_attribute("textContent")
        #     print(max)
        #     max = max.replace("「" + key + "」の検索結果 ", "")
        #     max = max.replace("件中" + str(low) + "〜" + str(high) + "件", "")
        #     print(max)
        #
        #     low += 20
        #     high += 20
        #
        #     # 1ページ終わったら次のページへ
        #     for j in range(0, int(max), 20):
        #         # list-group内の情報を取得
        #         lists = self.driver.find_elements_by_class_name("list-group")
        #         # listsを展開
        #         for list in lists:
        #             # listの中にあるaタグの取得
        #             hrefs = list.find_elements_by_tag_name("a")
        #             # hrefsの展開
        #             for href in hrefs:
        #                 # hrefの中にあるhrefタグを格納
        #                 self.link_list.append(href.get_attribute("href"))
        #             # ここでArticleを読んで各URLの詳細情報・棋譜情報・評価情報をもらう必要がある
        #             at.article(self.link_list)
        #
        #         page += 1
        #         # 次のページへ進む
        #         self.driver.get(self.url + "/search?q=" + key + "&page=" + str(page))
        #
        #
        # self.driver.quit()
        # # 戦型ごとに取得したURLを渡す
        # # return self.link_list
