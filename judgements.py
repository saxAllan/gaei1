import input

#----------labelling start----------
def labelling(x, y, labelno):
    #xについて
    tmpx = x
    tmpx = y
    sa = (input.data[tmpx][tmpy][0] - input.data[tmpx + 1][tmpy][0]) * (input.data[tmpx][tmpy][0] - input.data[tmpx + 1][tmpy][0])
    while sa<0.25:
        input.data[tmpx + 1][tmpy][1] = labelno
        tmpx += 1
        sa = (input.data[tmpx][tmpy][0] - input.data[tmpx + 1][tmpy][0]) * (input.data[tmpx][tmpy][0] - input.data[tmpx + 1][tmpy][0])
    #yについて
    tmpx = x
    tmpx = y
    sa = (input.data[tmpx][tmpy][0] - input.data[tmpx][tmpy + 1][0]) * (input.data[tmpx][tmpy][0] - input.data[tmpx][tmpy + 1][0])
    while sa < 0.25:
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
chkcount = 0

input.data[pt_x][pt_y][1] = label

while chkcount < input.count_x * input.count_y:
    labelling(pt_x, pt_y, label)
    
#----------main end----------
