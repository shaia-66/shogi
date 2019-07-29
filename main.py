import Senkei
import Search
import Article
import Kensu

import test

def main():
    # test.test_write()
    # kensu = test.test_Search()
    # print(type(kensu))

    kensu = Kensu.kensu()
    print(kensu)
    # # インスタンスの作成
    # sk = Senkei.Senkei()
    # # 戦型の結果を取得
    # senkei_list = sk.senkei()
    # インスタンスの作成
    sr = Search.Search()
    # 検索窓にキーワード入力し検索
    sr.search(kensu)

    # test.test_Search(kensu)


    # # url_listをArticleに渡す
    # at = Article.Article()
    # # 各URLを開く
    # info_list, kifu_list, eval_list = at.article(link_list)
    # print(info_list)
    # print(kifu_list)
    # print(eval_list)

if __name__ == "__main__":
    print("Scraping start")
    main()
    # 処理終了時
    print("fin")
