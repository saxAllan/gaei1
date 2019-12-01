import collections
import statistics
import numpy
import input
print("\n========================================")
print("  judgements Ver. 1.26 (20191126)")
print("========================================\n")


# 初期化
start_x = 0
start_y = 0
label = 0
max_label = 0

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
        if j < input.count_y - 3:
            if (input.data[i][j + 2][0] - input.data[i][j][0]) * (input.data[i][j + 2][0] - input.data[i][j][0]) < th:
                input.data[i][j + 2][1] = label
                input.data[i][j + 1][1] = label
            elif (input.data[i][j + 1][0] - input.data[i][j][0]) * (input.data[i][j + 1][0] - input.data[i][j][0]) < th:
                input.data[i][j + 1][1] = label
        elif j < input.count_y - 2:
            if (input.data[i][j + 1][0] - input.data[i][j][0]) * (input.data[i][j + 1][0] - input.data[i][j][0]) < th:
                input.data[i][j + 1][1] = label
        # 右方向
        if i < input.count_x - 3:
            if (input.data[i + 2][j][0] - input.data[i][j][0]) * (input.data[i + 2][j][0] - input.data[i][j][0]) < th:
                input.data[i + 2][j][1] = label
                input.data[i + 1][j][1] = label            
            elif (input.data[i + 1][j][0] - input.data[i][j][0]) * (input.data[i + 1][j][0] - input.data[i][j][0]) < th:
                input.data[i + 1][j][1] = label
        elif i < input.count_x - 2:
            if (input.data[i + 1][j][0] - input.data[i][j][0]) * (input.data[i + 1][j][0] - input.data[i][j][0]) < th:
                input.data[i + 1][j][1] = label
        # 右上方向
        if i < input.count_x - 2 and j < input.count_y - 2:
            if (input.data[i + 1][j + 1][0] - input.data[i][j][0]) * (input.data[i + 1][j + 1][0] - input.data[i][j][0]) < th:
                input.data[i + 1][j + 1][1] = label
print("処理終了")

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
for k in range(10):
    mode = mode_org[k][0]
    print(mode)
    for i in range(input.count_y):
        for j in range(input.count_x):
            if input.data[j][i][1] == mode:
                count_in += 1
                nokori[j][i][0] = input.data[j][i][0]

print(count_in)
# print(nokori)

#test_np = numpy.array(test)


# print(test)
