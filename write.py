import os.path
import shutil

def write(info_list, kifu_list, eval_list):
    info_list[0] = info_list[0].translate(str.maketrans({' ': '-', ':': ''}))
    date = info_list[0]

    kisen = info_list[1]

    kisen_info = info_list[2]

    info_list[3] = info_list[3].replace(" ","")
    if info_list[3] in u"3000":
        info_list[3] = info_list[3].replace(u"3000", "")
    sente = info_list[3]

    info_list[4] = info_list[4].replace(" ","")
    if info_list[4] in u"3000":
        info_list[4] = info_list[4].replace(u"3000", "")
    gote = info_list[4]

    senkei = info_list[5]

    kifu_path = "shogi/senkei_betu/" + senkei + "/" + date + "_" + senkei + "_先手_" + sente + "_後手_" + gote + ".txt"


    if not os.path.exists(kifu_path):
        with open(kifu_path, mode='w') as f:
            f.write(kisen + '\n')
            f.write(kisen_info + '\n')
            f.write('先手：' + sente + '\t\t' + '後手：' + gote + '\n')
        with open(kifu_path, mode='a') as ff:
            for i in range(len(kifu_list)):
                ff.write(kifu_list[i] + '\t\t' + eval_list[i] + '\n')

    # date = "2019_07_21"
    # senkei = "角換わり"
    # sente = "AAAA"
    # gote = "ZZZZ"
    # path = "shogi/senkei_betu/" + date + "_" + senkei + "_先手_" + sente + "_後手_" + gote + ".txt"
    # text = "test"
    # with open(path, mode="w") as f:
    #     f.write(text)
