import os

def create_directory(senkei_list):
    print("Create_directory start")
    for senkei in senkei_list:
        path = "shogi/senkei_betu/" + senkei
        if not os.path.exists(path):
            os.mkdir(path)
