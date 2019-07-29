import os.path

def test_write(info_list, kifu_list, eval_list):
    info_list[0] = info_list[0].translate(str.maketrans({' ': '-', ':': ''}))
    # info_list[0] = info_list[0].replace(":","")
    date = info_list[0]

    senkei = info_list[5]
    info_list[3] = info_list[3].replace(" ","")
    if info_list[3] in u"3000":
        info_list[3] = info_list[3].replace(u"3000", "")

    sente = info_list[3]
    info_list[4] = info_list[4].replace(" ","")
    if info_list[4] in u"3000":
        info_list[4] = info_list[4].replace(u"3000", "")

    gote = info_list[4]
    path = "shogi/senkei_betu/" + date + "_" + senkei + "_先手_" + sente + "_後手_" + gote + ".txt"

    with open(path, mode="a") as f:
        for i in range(len(kifu_list)):
            # if os.path.isfile(path):
            #     continue
            f.write(kifu_list[i] + '\t\t\t\t' + eval_list[i] + '\n')

    # date = "2019_07_21"
    # senkei = "角換わり"
    # sente = "AAAA"
    # gote = "ZZZZ"
    # path = "shogi/senkei_betu/" + date + "_" + senkei + "_先手_" + sente + "_後手_" + gote + ".txt"
    # text = "test"
    # with open(path, mode="w") as f:
    #     f.write(text)
