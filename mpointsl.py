#欠損点削除
import input

data2=input.data[:]
for i in range(input.count_y):
    for j in range(input.count_x):
        if input.data[i][j][0]+9999<1:
                input.data[i][j][0]=input.data[i][j-1][0]
for i in range(input.count_x):
    for j in range(input.count_y):
        if data2[i][j][0]+9999<1:
                data2[i][j][0]=data2[i][j-1][0]
for i in range(input.count_y):
    for j in range(input.count_x):
        if input.data[i][j][0]>data2[i][j][0]:    
                input.data[i][j][0]=data2[i][j][0]