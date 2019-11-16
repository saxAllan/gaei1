import input

#----------labelling start----------
def labelling_x(x, y, labelno, list_equal):
    #xについて
    sa = (input.data[x][y][0] - input.data[x + 1][y][0]) * (input.data[x][y][0] - input.data[x + 1][y][0])
    while sa < 0.25:
        input.data[x + 1][y][1] = labelno
        if input.data[x + 1][y][1] != 0: #既にラベリングされてたら、input.data[x + 1][y][1]とlabelnoのデータを二次元配列に格納
            list_equal[0].append(input.data[x + 1][y][1])
            list_equal[1].append(labelno)
        x += 1 #次のxへ
        sa = (input.data[x][y][0] - input.data[x + 1][y][0]) * (input.data[x][y][0] - input.data[x + 1][y][0])
    print("labelling_x", x, y, labelno) #デバッグ

def labelling_base(base_x, base_y, base_label, base_equal):
    #横方向へ
    for i in range(base_x, input.count_x):
        #print(input.data[base_x][base_y][1])
        if (input.data[i][base_y][1] == 0):
            print("入った")
            labelling_x(i, base_y, base_label, base_equal)
    #上方向へ
    for i in range(base_x, input.count_x):
        if base_x == input.count_x - 3 or base_y == input.count_y - 3:
                break
            elif (input.data[base_x][base_y + i][0] - input.data[base_x][base_y + i + 1][0]) * (input.data[base_x][base_y + i][0] - input.data[base_x][base_y + i + 1][0]) < 0.25:
                labelling_base(base_x, base_y + 1, base_label, base_equal)

#----------labelling end----------

#----------main start----------
#初期化
equal = []
for i in range (2):
    equal.append([])
start_x = 0
start_y = 0
pt_x = 0
pt_y = 0
label = 1

#ラベリング
#input.data[pt_x][pt_y][1] = label
for i in range(input.count_x):
    for j in range(input.count_y):
        print(input.data[i][j][1])
        if input.data[i][j][1] == 0:
            labelling_base(pt_x, pt_y, label, equal)
print("ここまで")
#----------main end----------
