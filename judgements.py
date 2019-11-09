#filename_i = input("入力ファイル名（拡張子は不要）：")
filename_i = "map_light"
filename_o = "output"

#----------ここからデータ読み込み----------
print(filename_i + ".datを読み込んでいます...  ",end="")
f = open(filename_i + ".dat", "r")
lines = f.readlines()
orgdata = []
for i in lines:
    orgdata.append(list(map(float, i.split())))
f.close()
size_org = len(orgdata)

#デバッグ用
for i in range(10):
    print(orgdata[i])
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
data = [[]] * count_x

#正規化チェック
print("x=",count_x,"y=",count_y)
if count_x * count_y == size_org:
    print("行列は正規化されています")
else:
    print("行列は正規化されていない可能性があります")

#2次元配列化
cdnt_x = 0
cdnt_y = 0
for i in range(size_org):
    data[cdnt_x][cdnt_y]=





'''2代目2次元配列化
for i in range(count_y):
    for j in range(count_x):
        data[j].append(orgdata[(i * count_x) + j][2])
    print("\r", "処理中...", i + 1, "/", count_y, "   ", end="")
print("処理完了")

for i in range(100):
    print(data[i][0])
'''

'''初代二次元配列化
for i in range(count_y):
    for j in range(count_x):
        data[i].append(orgdata[i*count_x+j][2])


for i in range(10):
    print(i,"行目")
    for j in range(10):
        print(data[i][j])
'''

#----------ここまでデータ読み込み----------

#----------ここから判定処理----------
#----------ここまで判定処理----------
