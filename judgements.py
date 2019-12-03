import collections
import statistics
import numpy
import input
print("\n========================================")
print("  judgements Ver. 1.30 (20191201)")
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
for i in range(input.count_x):
    for j in range(input.count_y):
        # 自分自身の判定
        if input.data[i][j][1] != 0:
            label = input.data[i][j][1]
        else:
            label = max_label + 1
            max_label += 1

        print("\r", i * input.count_y + j + 1, "/",
              input.count_x * input.count_y, end="   ")
        input.data[i][j][1] = label
        # 上方向
        if j < input.count_y - 2:
            if (input.data[i][j + 1][0] - input.data[i][j][0]) * (input.data[i][j + 1][0] - input.data[i][j][0]) < th:
                if input.data[i][j + 1][1] != 0:
                    samevalue[0].append(label)
                    samevalue[1].append(input.data[i][j + 1][1])
                input.data[i][j + 1][1] = label
        # 右方向
        if i < input.count_x - 2:
            if (input.data[i + 1][j][0] - input.data[i][j][0]) * (input.data[i + 1][j][0] - input.data[i][j][0]) < th:
                if input.data[i + 1][j][1] != 0:
                    samevalue[0].append(label)
                    samevalue[1].append(input.data[i + 1][j][1])
                input.data[i + 1][j][1] = label
        # 右上方向
        if i < input.count_x - 2 and j < input.count_y - 2:
            if (input.data[i + 1][j + 1][0] - input.data[i][j][0]) * (input.data[i + 1][j + 1][0] - input.data[i][j][0]) < th:
                if input.data[i][j + 1][1] != 0:
                    samevalue[0].append(label)
                    samevalue[1].append(input.data[i + 1][j + 1][1])
                input.data[i + 1][j + 1][1] = label
print("処理終了")

print(samevalue[1])

# デバッグ
test = []
for i in range(input.count_x):
    for j in range(input.count_y):
        test.append(input.data[i][j][1])
test.sort()
#mode = statistics.mode(test)
mode_org = collections.Counter(test).most_common()
nokori = []
for i in range(input.count_x):
    nokori.append([])
count_in = 0

for i in range(input.count_y):
    for j in range(input.count_x):
        nokori[j].append([])
        nokori[j][i].append(0)
for k in range(100):
    mode = mode_org[k][0]
    print(mode)
    for i in range(input.count_y):
        for j in range(input.count_x):
            if input.data[j][i][1] == mode:
                count_in += 1
                nokori[j][i][0] = input.data[j][i][0]



'''
        # 上方向
        if j < input.count_y - 2:
            if (input.data[i][j + 1][0] - input.data[i][j][0]) * (input.data[i][j + 1][0] - input.data[i][j][0]) < th:
                if input.data[i][j + 1][1] == 0:
                    input.data[i][j + 1][1] = label
                else:
                    for ii in range(input.count_x):
                        for jj in range(input.count_y):
                            if input.data[ii][jj][1] == input.data[i][j + 1][1]:
                                input.data[ii][jj][1] = label
        # 右方向
        if i < input.count_x - 2:
            if (input.data[i + 1][j][0] - input.data[i][j][0]) * (input.data[i + 1][j][0] - input.data[i][j][0]) < th:
                if input.data[i + 1][j][1] == 0:
                    input.data[i + 1][j][1] = label
                else:
                    for ii in range(input.count_x):
                        for jj in range(input.count_y):
                            if input.data[ii][jj][1] == input.data[i + 1][j][1]:
                                input.data[ii][jj][1] = label
        # 右上方向
        if i < input.count_x - 2 and j < input.count_y - 2:
            if (input.data[i + 1][j + 1][0] - input.data[i][j][0]) * (input.data[i + 1][j + 1][0] - input.data[i][j][0]) < th:
                if input.data[i + 1][j + 1][1] == 0:
                    input.data[i + 1][j + 1][1] = label
                else:
                    for ii in range(input.count_x):
                        for jj in range(input.count_y):
                            if input.data[ii][jj][1] == input.data[i + 1][j + 1][1]:
                                input.data[ii][jj][1] = label
'''
