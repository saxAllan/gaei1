import collections
import statistics
import numpy
import datinput
print("\n========================================")
print("  judgements Ver. 2.31 (20191203)")
print("========================================\n")


# 初期化
start_x = 0
start_y = 0
label = 0
max_label = 0
samevalue = []
for i in range(2):
    samevalue.append([])
print(samevalue)

print("judgements 処理中...")

th = 1  # しきい値

# ラベリング
for i in range(datinput.count_x):
    for j in range(datinput.count_y):
        # 自分自身の判定
        if datinput.data[i][j][1] != 0:
            label = datinput.data[i][j][1]
        else:
            label = max_label + 1
            max_label += 1

        print("\r", i * datinput.count_y + j + 1, "/",
              datinput.count_x * datinput.count_y, end="   ")
        datinput.data[i][j][1] = label
        # 上方向
        if j < datinput.count_y - 2:
            if (datinput.data[i][j + 1][0] - datinput.data[i][j][0]) * (datinput.data[i][j + 1][0] - datinput.data[i][j][0]) < th:
                if datinput.data[i][j + 1][1] != 0:
                    samevalue[0].append(label)
                    samevalue[1].append(datinput.data[i][j + 1][1])
                datinput.data[i][j + 1][1] = label
        # 右方向
        if i < datinput.count_x - 2:
            if (datinput.data[i + 1][j][0] - datinput.data[i][j][0]) * (datinput.data[i + 1][j][0] - datinput.data[i][j][0]) < th:
                if datinput.data[i + 1][j][1] != 0:
                    samevalue[0].append(label)
                    samevalue[1].append(datinput.data[i + 1][j][1])
                datinput.data[i + 1][j][1] = label
        # 右上方向
        if i < datinput.count_x - 2 and j < datinput.count_y - 2:
            if (datinput.data[i + 1][j + 1][0] - datinput.data[i][j][0]) * (datinput.data[i + 1][j + 1][0] - datinput.data[i][j][0]) < th:
                if datinput.data[i][j + 1][1] != 0:
                    samevalue[0].append(label)
                    samevalue[1].append(datinput.data[i + 1][j + 1][1])
                datinput.data[i + 1][j + 1][1] = label
print("処理終了")

print(samevalue[0][0])

# デバッグ
test = []
for i in range(datinput.count_x):
    for j in range(datinput.count_y):
        test.append(datinput.data[i][j][1])
test.sort()
#mode = statistics.mode(test)
mode_org = collections.Counter(test).most_common()
nokori = []
for i in range(datinput.count_x):
    nokori.append([])
count_in = 0

for i in range(datinput.count_y):
    for j in range(datinput.count_x):
        nokori[j].append([])
        nokori[j][i].append(0)
for k in range(100):
    mode = mode_org[k][0]
    print(mode)
    for i in range(datinput.count_y):
        for j in range(datinput.count_x):
            if datinput.data[j][i][1] == mode:
                count_in += 1
                nokori[j][i][0] = datinput.data[j][i][0]



'''
        # 上方向
        if j < datinput.count_y - 2:
            if (datinput.data[i][j + 1][0] - datinput.data[i][j][0]) * (datinput.data[i][j + 1][0] - datinput.data[i][j][0]) < th:
                if datinput.data[i][j + 1][1] == 0:
                    datinput.data[i][j + 1][1] = label
                else:
                    for ii in range(datinput.count_x):
                        for jj in range(datinput.count_y):
                            if datinput.data[ii][jj][1] == datinput.data[i][j + 1][1]:
                                datinput.data[ii][jj][1] = label
        # 右方向
        if i < datinput.count_x - 2:
            if (datinput.data[i + 1][j][0] - datinput.data[i][j][0]) * (datinput.data[i + 1][j][0] - datinput.data[i][j][0]) < th:
                if datinput.data[i + 1][j][1] == 0:
                    datinput.data[i + 1][j][1] = label
                else:
                    for ii in range(datinput.count_x):
                        for jj in range(datinput.count_y):
                            if datinput.data[ii][jj][1] == datinput.data[i + 1][j][1]:
                                datinput.data[ii][jj][1] = label
        # 右上方向
        if i < datinput.count_x - 2 and j < datinput.count_y - 2:
            if (datinput.data[i + 1][j + 1][0] - datinput.data[i][j][0]) * (datinput.data[i + 1][j + 1][0] - datinput.data[i][j][0]) < th:
                if datinput.data[i + 1][j + 1][1] == 0:
                    datinput.data[i + 1][j + 1][1] = label
                else:
                    for ii in range(datinput.count_x):
                        for jj in range(datinput.count_y):
                            if datinput.data[ii][jj][1] == datinput.data[i + 1][j + 1][1]:
                                datinput.data[ii][jj][1] = label
'''
