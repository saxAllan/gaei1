import input

#----------labelling start----------
def labelling_x(x, y, labelno, list_equal):
    #xについて
    sa = (input.data[x][y][0] - input.data[x + 1][y][0]) * (input.data[x][y][0] - input.data[x + 1][y][0])
    while sa < 0.25:
        if input.data[x + 1][y][1] != 0:
            #input.data[x + 1][y][1]とlabelnoのデータを二次元配列に格納
            list_equal[0].append(input.data[x + 1][y][1])
            list_equal[1].append(labelno)
        input.data[x + 1][y][1] = labelno
        x += 1
        sa = (input.data[x][y][0] - input.data[x + 1][y][0]) * (input.data[x][y][0] - input.data[x + 1][y][0])

def labelling_y(x, y, labelno, list_equal):
    #yについて
    sa = (input.data[x][y][0] - input.data[x][y + 1][0]) * (input.data[x][y][0] - input.data[x][y + 1][0])
    while sa < 0.25:
        if input.data[x + 1][y][1] != 0:
            #input.data[x][y + 1][1]とlabelnoのデータを二次元配列に格納
            list_equal[0].append(input.data[x][y + 1][1])
            list_equal[1].append(labelno)
        input.data[x][y + 1][1] = labelno
        y += 1
        sa = (input.data[x][y][0] - input.data[x][y + 1][0]) * (input.data[x][y][0] - input.data[x][y + 1][0])

def labelling_base(base_x, base_y, base_label,base_equal):
    for i in range(input.count_x):
        if(input.data[base_x][base_y][1]==0):
            labelling_x(base_x, base_y, base_label, base_equal)
            if (input.data[base_x][base_y + i][0] - input.data[base_x][base_y + i + 1][0]) * (input.data[base_x][base_y + i][0] - input.data[base_x][base_y + i + 1][0]) < 0.25:
                labelling_x(base_x, base_y + 1, base_label, base_equal)
                


#----------labelling end----------

#----------main start----------
start_x = 0
start_y = 0
pt_x = 0
pt_y = 0
label = 1
equal = []
for i in range (2):
    equal.append([])

input.data[pt_x][pt_y][1] = label
for i in range(input.count_y):
    for j in range(input.count_x):
        if input.data[i][j][1] == 0:
            labelling_base(pt_x, pt_y, label, equal)
print("ここまで")
#----------main end----------
'''2019年11月12日メモ
input.data[][][1]を0で初期化してない
'''