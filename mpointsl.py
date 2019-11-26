print("\n========================================")
print("  mpointsl Ver. 1.3 (20191126)")
print("========================================\n")

import input

data2=input.data[:]
for i in range(input.count_y):
    for j in range(input.count_x):
        if input.data[j][i][0]+9999<1:
                input.data[j][i][0]=input.data[j-1][i][0]
for i in range(input.count_x):
    for j in range(input.count_y):
        if data2[i][j][0]+9999<1:
                data2[i][j][0]=data2[i][j-1][0]
for i in range(input.count_y):
    for j in range(input.count_x):
        if input.data[j][i][0]>data2[j][i][0]:    
                input.data[j][i][0]=data2[j][i][0]

print("欠損点処理完了")