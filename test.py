from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
import sys
import os

def test_Search():
    driver = webdriver.Chrome()
    url = 'https://shogidb2.com'
    driver.get(url)
    ss = driver.find_element_by_id('game-count').get_attribute("textContent")
    ss = ss.translate(str.maketrans({'件': '', ',': ''}))

    # str = str.replace('件', '')
    # str = str.replace(',', '')
    # str = ','.join(str)
    print(ss)
    return int(ss)


def test_write(kifu_list, eval_list):
    date = "2019_07_21"
    senkei = "角換わり"
    sente = "AAAA"
    gote = "ZZZZ"
    path = "shogi/senkei_betu/" + date + "_" + senkei + "_先手_" + sente + "_後手_" + gote + ".txt"
    text = "test"
    with open(path, mode="a") as f:
        for i in range(len(kifu_list)):
            f.write(kifu_list[i] + '\t\t' + eval_list[i] + '\n')



def test_Article():
    url = "https://shogidb2.com/games/7a7b47fd78ea0665f212f235794dd4c4d9f26e37"
    driver = webdriver.Chrome()
    driver.get(url)
    word = "投了"

    eval_list = []
    kifu_list = []

    WebDriverWait(driver, 2).until(EC.presence_of_element_located)

    while True:
        # 評価値の取得
        eval = driver.find_element_by_css_selector("h4.h5.card-title").get_attribute("textContent")
        # 評価値：値 の形式になるように整形
        eval = eval.replace("プラスは先手有利、マイナスは後手有利", "")
        # 整形した文字列をリストに格納
        eval_list.append(eval)

        print(eval_list[1:])

        driver.find_element_by_css_selector("i.fa.fa-forward.fa-2x").click()
        # tspanの親タグID
        tt = driver.find_element_by_id("SvgjsText1407").get_attribute("textContent")
        kifu_list.append(tt)
        print(kifu_list)
        if word in tt:
            print("終局です > " + tt)
            sys.exit()
