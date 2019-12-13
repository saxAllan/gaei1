import statistics
import numpy
import norminput

print("\n========================================")
print("  judgements Ver. 3.2 (20191208)")
print("========================================\n")

def master(xstart, xend, ystart, yend, nokori):
    high = []
    orghigh = []
    for i in range(xstart, xend):
        for j in range(ystart, yend):
            if norminput.data[i][j][0] < 40:                
                orghigh.append(norminput.data[i][j][0])  #中央値用
                high.append((norminput.data[i][j][0] // 2) * 2)  #最頻値用
                norminput.data[i][j][1] = (norminput.data[i][j][0] // 2) * 2  #最頻値用
            else:
                orghigh.append(10)  #中央値用
                high.append(10)  #最頻値用
                norminput.data[i][j][1] = (norminput.data[i][j][0] // 2) * 2 #最頻値用

    #最頻値
    mode_high = statistics.mode(high)
    high_list = []
    for i in range(40):
        high_list.append(high.count(i))
    #print(high_list)
    tmphigh = 0
    for i in range(40):
        tmphigh += high_list[i]
        if tmphigh > 500:
            mode_high = i + 1
            break
        
    #中央値
    orghigh.sort()
    medi_high = 0
    lengs = len(high)
    if lengs % 2 == 1:
        medi_high = orghigh[(lengs // 4) + 1]
    else:
        medi_high = (orghigh[lengs // 4] + orghigh[(lengs // 4) + 1]) / 2.0

    print("    最頻値:", mode_high, "    中央値:", medi_high)
    
    if mode_high > medi_high:
        for i in range(ystart, yend):
            for j in range(xstart, xend):
                if norminput.data[j][i][1] <= mode_high:  #最頻値
                    nokori[j][i][0] = norminput.data[j][i][0]
    else:
        for i in range(ystart, yend):
            for j in range(xstart, xend):
                if norminput.data[j][i][1] <= medi_high:  #中央値
                    nokori[j][i][0] = norminput.data[j][i][0]

# 初期化
start_x = 0
start_y = 0
label = 0
max_label = 0
print("judgements 処理中...")

# ラベリング
nokori = []
for i in range(norminput.count_x):
    nokori.append([])
for i in range(norminput.count_x):
    for j in range(norminput.count_y):
        nokori[i].append([])
        nokori[i][j].append(0)
  

area_x = [0]
area_y = [0]
divide_x = 18
divide_y = 7
tmp = (norminput.count_x // divide_x) + 1
while (tmp< norminput.count_x):
    area_x.append(tmp)
    tmp += (norminput.count_x // divide_x) + 1
if tmp < norminput.count_x + (norminput.count_x // divide_x):
    area_x.append(norminput.count_x)
tmp = (norminput.count_y // divide_y) + 1
while (tmp< norminput.count_y):
    area_y.append(tmp)
    tmp += (norminput.count_y // divide_y) + 1
if tmp < norminput.count_y + (norminput.count_y // divide_y):
    area_y.append(norminput.count_y)
print(area_x)
print(area_y)

for i in range(divide_x):
    for j in range(divide_y):
        print(i, j, end=" ")
        master(area_x[i], area_x[i + 1], area_y[j], area_y[j + 1], nokori)


'''メモ
第１四分位数を利用
地図の横は1.14kmくらい
　→縦は1kmくらい？
'''