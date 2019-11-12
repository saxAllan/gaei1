import input

#----------labelling start----------
def labelling_x(x, y, labelno, list_equal):
    #xについて
    tmpx = x
    tmpy = y
    cnt=0
    sa = (input.data[tmpx][tmpy][0] - input.data[tmpx + 1][tmpy][0]) * (input.data[tmpx][tmpy][0] - input.data[tmpx + 1][tmpy][0])
    while sa < 0.25:
        if input.data[tmpx + 1][tmpy][1] != 0:
            #input.data[tmpx + 1][tmpy][1]とlabelnoのデータを二次元配列に格納
            list_equal[0].append(input.data[tmpx + 1][tmpy][1])
            list_equal[1].append(labelno)
        input.data[tmpx + 1][tmpy][1] = labelno
        tmpx += 1
        sa = (input.data[tmpx][tmpy][0] - input.data[tmpx + 1][tmpy][0]) * (input.data[tmpx][tmpy][0] - input.data[tmpx + 1][tmpy][0])

def labelling_y(x, y, labelno, list_equal):
    #yについて
    tmpx = x
    tmpx = y
    sa = (input.data[tmpx][tmpy][0] - input.data[tmpx][tmpy + 1][0]) * (input.data[tmpx][tmpy][0] - input.data[tmpx][tmpy + 1][0])
    while sa < 0.25:
        if input.data[tmpx + 1][tmpy][1] != 0:
            #input.data[tmpx][tmpy + 1][1]とlabelnoのデータを二次元配列に格納
            list_equal[0].append(input.data[tmpx][tmpy + 1][1])
            list_equal[1].append(labelno)

        input.data[tmpx][tmpy + 1][1] = labelno
        tmpy += 1
        sa = (input.data[tmpx][tmpy][0] - input.data[tmpx][tmpy + 1][0]) * (input.data[tmpx][tmpy][0] - input.data[tmpx][tmpy + 1][0])
#----------labelling end----------

#----------main end----------
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


labelling_x(pt_x, pt_y, label,)
#----------main end----------
