#filename_i = input("入力ファイル名（拡張子は不要）：")
filename_i = "mpoints6"
filename_o = "output"

#----------ここからデータ読み込み----------
#Belle Carte input (Ver. 1.0)
print(filename_i + ".datを読み込んでいます...  ")
f = open(filename_i + ".dat", "r")
lines = f.readlines()
orgdata = []
for i in lines:
    orgdata.append(list(map(float, i.split())))
f.close()
size_org = len(orgdata)
print("読込完了 (", size_org, "行)")

#座標カウント
y = orgdata[0][1]
i = 0
j = 0
count_x = 0
count_y = 0
while orgdata[i][1] == y:
    count_x += 1
    i += 1
count_y = size_org // count_x
#data = [[0]*count_y] * count_x
#data = [[]] * count_x
data = []
for i in range(count_x):
    data.append([])

#正規化チェック
print("x=",count_x,"y=",count_y)
if count_x * count_y == size_org:
    print("行列は正規化されています")
else:
    print("行列は正規化されていない可能性があります")

#2代目2次元配列化
for i in range(count_y):
    for j in range(count_x):
        temp = float(orgdata[(i * count_x) + j][2])
        #print(temp)
        data[j].append(temp)
    print("\r", "処理中...", i + 1, "/", count_y, "   ", end="")
print("処理完了")

'''デバッグ
for i in range(100):
    print(data[0][i])
'''
#----------ここまでデータ読み込み----------
'''説明
このinputは、data[(x座標)][(y座標)]に(x,y)の標高データが格納されます。
filename_i を入力ファイル名に適宜変更してください。
'''