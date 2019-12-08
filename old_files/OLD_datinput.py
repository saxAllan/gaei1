print("\n========================================")
print("  datinput Ver. 2.1 (20191203)")
print("========================================\n")


filename_i = input("入力ファイル名（拡張子は不要）：")

print(filename_i + ".datを読み込み中...  ")
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
    print("正規化：〇")
else:
    print("正規化：×")

#2次元配列化
print("二次元配列化処理中...")
for i in range(count_y):
    for j in range(count_x):
        temp = float(orgdata[(i * count_x) + j][2])
        data[j].append([])
        data[j][i].append(temp)
        data[j][i].append(0)
    print("\r", i + 1, "/", count_y, "   ", end="")
print("処理完了")