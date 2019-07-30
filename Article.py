from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

import Write
import test

class Article(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def article(self, link_list):
        print("Article start")
        eval = ""
        # URLの展開
        for link in link_list:
            info_list = []
            kifu_list = []
            eval_list = []
            self.driver.get(link)
            try:
                table = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.table.table-bordered.table-hover.table-sm")))
            except:
                self.driver.quit()

            trs = table.find_elements(By.TAG_NAME, "tr")
            for i in range(len(trs)):
                tds = trs[i].find_elements(By.TAG_NAME, "td")
                for j in range(0, len(tds)):
                    info_list.append(tds[j].text)
            # 不要な情報の削除
            del info_list[5:9]

            # 棋譜の取得
            while True:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located)
                eval = self.driver.find_element_by_css_selector("h4.h5.card-title").get_attribute("textContent")
                # 評価値：値 の形式になるように整形
                eval = eval.replace("プラスは先手有利、マイナスは後手有利", "")
                eval = eval.replace("解説", "")
                # 整形した文字列をリストに格納
                eval_list.append(eval)
                # 次の手をクリック
                self.driver.find_element_by_css_selector("i.fa.fa-forward.fa-2x").click()
                # tspanの親タグID
                t = self.driver.find_element_by_id("SvgjsText1407").get_attribute("textContent")
                kifu_list.append(t)
                if "投了" in t:
                    break

            Write.write(info_list, kifu_list, eval_list)
        self.driver.quit()
