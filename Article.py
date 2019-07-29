from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

import write
import test

class Article(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        # 対局情報
        self.info_list = []
        # 棋譜情報
        self.kifu_list = []
        # 評価値情報
        self.eval_list = []

    def article(self, link_list):
        print("Article start")
        # URLの展開
        for link in link_list:
            self.info_list = []
            self.kifu_list = []
            self.eval_list = []
            #  ex) https://shogidb2.com/games/7a7b47fd78ea0665f212f235794dd4c4d9f26e37
            self.driver.get(link)
            time.sleep(1)
            # tableの取得
            table = self.driver.find_element_by_css_selector("table.table.table-bordered.table-hover.table-sm")
            # trタグの取得
            trs = table.find_elements(By.TAG_NAME, "tr")
            # trsの展開
            for i in range(len(trs)):
                # tdタグの取得
                tds = trs[i].find_elements(By.TAG_NAME, "td")
                # tdsの展開
                for j in range(0, len(tds)):
                    # リストに追加
                    self.info_list.append(tds[j].text)
            # 不要な情報の削除
            del self.info_list[5:9]

            # 棋譜の取得
            while True:
                # 評価値の取得
                eval = self.driver.find_element_by_css_selector("h4.h5.card-title").get_attribute("textContent")
                # 評価値：値 の形式になるように整形
                # eval = eval.replace("プラスは先手有利、マイナスは後手有利", "")
                # eval = eval.replace("解説","")
                # 整形した文字列をリストに格納
                self.eval_list.append(eval)
                # 次の手をクリック
                self.driver.find_element_by_css_selector("i.fa.fa-forward.fa-2x").click()
                # tspanの親タグID
                t = self.driver.find_element_by_id("SvgjsText1407").get_attribute("textContent")
                self.kifu_list.append(t)
                # print(self.eval_list)
                if "投了" in t:
                    break

            # return self.info_list, self.kifu_list, self.eval_list
            # ファイルに書き込もう
            # write.test_write(self.info_list, self.kifu_list, self.eval_list)
            test.test_write(self.kifu_list, self.eval_list)
