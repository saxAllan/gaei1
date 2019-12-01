print("\n========================================")
print("  judgements Ver. 1.26 (20191126)")
print("========================================\n")
import input
import numpy
import statistics
import concurrent.futures

def modecalc(mode_org, nokori):
    for k in range(150):
        mode = mode_org[k][0]
        print(mode)
        for i in range(input.count_y):
            for j in range(input.count_x):
                if input.data[j][i][1] == mode:
                    #count_in += 1
                    nokori[j][i][0] = input.data[j][i][0]



#初期化
start_x = 0
start_y = 0
label = 0
max_label = 0

print("judgements 処理中...")

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
            if (input.data[i][j + 1][0] - input.data[i][j][0]) * (input.data[i][j + 1][0] - input.data[i][j][0]) < 4:
                input.data[i][j + 1][1] = label
        if i < input.count_x - 2:
            if (input.data[i + 1][j][0] - input.data[i][j][0]) * (input.data[i + 1][j][0] - input.data[i][j][0]) < 4:
                input.data[i + 1][j][1] = label
        if i < input.count_x - 2 and j < input.count_y - 2:
            if (input.data[i + 1][j + 1][0] - input.data[i][j][0]) * (input.data[i + 1][j + 1][0] - input.data[i][j][0]) < 4:
                input.data[i + 1][j + 1][1] = label
print("処理終了")

#デバッグ
test = []
for i in range(input.count_x):
    for j in range(input.count_y):
        test.append(input.data[i][j][1])
test.sort()
#mode = statistics.mode(test)
import collections
mode_org = collections.Counter(test).most_common()
nokori = []
for i in range(input.count_x):
    nokori.append([])

count_in = 0

for i in range(input.count_y):
    for j in range(input.count_x):
        nokori[j].append([])
        nokori[j][i].append(0)

#aaaaaaa
executor = concurrent.futures.ProcessPoolExecutor(max_workers=8)
executor.submit(modecalc, mode_org, nokori)
print(count_in)
#print(nokori)

#test_np = numpy.array(test)


#print(test)