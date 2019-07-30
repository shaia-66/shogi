import Senkei
import Search
import Article
import Kensu
import Create_directory

# import test
# import sys

def main():
    sk = Senkei.Senkei()
    senkei_list = sk.senkei()
    Create_directory.create_directory(senkei_list)
    kensu = Kensu.kensu()

    sr = Search.Search()
    sr.search(kensu)

if __name__ == "__main__":
    print("Scraping start")
    main()
    print("exe fin")
