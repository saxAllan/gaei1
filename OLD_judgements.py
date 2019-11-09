filename_i = input("入力ファイル名（拡張子は不要）：")
filename_o = "output"

#----------ここからデータ読み込み----------
print(filename_i+".datを読み込んでいます")
f = open(filename_i + ".dat", "r")
lines = f.readlines()
orgdata = []
for i in lines:
    orgdata.append(list(map(float, i.split())))
f.close()
for i in range(len(orgdata)):
    orgdata[i].append(0)

#デバッグ用
for i in range(20):
#    print(orgdata[i][0])
    print(orgdata[i])
print("      ...", len(orgdata), "個のデータを読み込みました")

#----------ここまでデータ読み込み----------

#----------ここから判定アルゴリズム----------

orgdata[0][3] = 0
y = orgdata[0][1]
z = orgdata[0][2]
count_tmp = 1
print("判定処理開始")
for i in range(1, len(orgdata)):
    if orgdata[i][1] != y:
        count_tmp += 1
        print("\r", count_tmp, "行目処理中", end="")
        temp = z - orgdata[i][2]
        if 1 > temp and temp > -1:
            orgdata[i][3] = 0
        elif temp >= 1:
            orgdata[i][3] = -1
        else:
            orgdata[i][3] = 1
        y = orgdata[i][1]
        z = orgdata[i][2]
    else:
        temp = orgdata[i - 1][2] - orgdata[i][2]
        if 5 > temp and temp > -5:
            orgdata[i][3] = orgdata[i - 1][3]
        elif temp >= 5:
            orgdata[i][3] = orgdata[i - 1][3] - 1
        else:
            orgdata[i][3] = orgdata[i - 1][3] + 1

#----------ここまで判定アルゴリズム----------

#----------ここから内容生成----------
print("\nファイルの内容を生成しています")
out = "#VRML V2.0 utf8\n"

#テスト用
for i in range(int(len(orgdata)/10)):
    out += str(orgdata[i][0])
    out += str(" ")
    out += str(orgdata[i][1])
    out += str(" ")
    out += str(orgdata[i][3])
    out += "\n"


#----------ここまで内容生成----------



#----------ここからファイル出力----------
f = open(filename_o + ".wrl", mode="w")
f.write(out)
f.close()
print(filename_o+".wrl を出力しました")
#----------ここまでファイル出力----------

'''参考情報
openのときにwith openにするとcloseしなくてよい
https://note.nkmk.me/python-file-io-open-with/
'''