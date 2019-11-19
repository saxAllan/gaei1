#judgements Ver. 1.24(20191116)

import input

#初期化
start_x = 0
start_y = 0
label = 0
max_label = 0

print("ラベリング処理中...")

#ラベリング
for i in range(input.count_x):
    for j in range(input.count_y):
        if input.data[i][j][1] != 0:
            label = input.data[i][j][1]
        else:
            label = max_label + 1
            max_label += 1        
        print("\r", i * input.count_y + j + 1, "/", input.count_x * input.count_y, end="   ")
        input.data[i][j][1] = label        
        if j < input.count_y - 2:
            if (input.data[i][j + 1][0] - input.data[i][j][0]) * (input.data[i][j + 1][0] - input.data[i][j][0]) < 0.25:
                input.data[i][j + 1][1] = label
        if i < input.count_x - 2:
            if (input.data[i + 1][j][0] - input.data[i][j][0]) * (input.data[i + 1][j][0] - input.data[i][j][0]) < 0.25:
                input.data[i + 1][j][1] = label
        if i < input.count_x - 2 and j < input.count_y - 2:
            if (input.data[i + 1][j + 1][0] - input.data[i][j][0]) * (input.data[i + 1][j + 1][0] - input.data[i][j][0]) < 0.25:
                input.data[i + 1][j + 1][1] = label
print("処理終了")

#デバッグ
test=[]
for i in range(input.count_x):
    for j in range(input.count_y):
        test.append(input.data[i][j][1])
test.sort()
print(test)