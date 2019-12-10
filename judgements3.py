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
            orghigh.append(norminput.data[i][j][0])  #中央値用
            high.append((norminput.data[i][j][0] // 5) * 5)  #最頻値用
            norminput.data[i][j][1] = (norminput.data[i][j][0] // 5) * 5  #最頻値用
    #最頻値
    mode_high = statistics.mode(high)
    #中央値
    orghigh.sort()
    medi_high = 0
    lengs = len(high)
    if lengs % 2 == 1:
        medi_high = orghigh[(lengs // 2) + 1]
    else:
        medi_high = (orghigh[lengs // 2] + orghigh[(lengs // 2) + 1]) / 2.0

    print("処理終了  最頻値:", mode_high)
    print("処理終了  中央値:", medi_high)

    for i in range(xstart, xend):
        nokori.append([])

    for i in range(ystart, yend):
        for j in range(xstart, xend):
            nokori[j].append([])
            nokori[j][i].append(0)
            if norminput.data[j][i][0] <= medi_high:  #最頻値 or 中央値
                nokori[j][i][0] = norminput.data[j][i][0]

# 初期化
start_x = 0
start_y = 0
label = 0
max_label = 0
print("judgements 処理中...")

th = 1  # しきい値

# ラベリング
nokori = []
area_x = [0]
area_y = [0]
tmp = (norminput.count_x // 5) + 1
while (tmp< norminput.count_x):
    area_x.append(tmp)
    tmp += (norminput.count_x // 5) + 1
if tmp < norminput.count_x + (norminput.count_x // 5):
    area_x.append(norminput.count_x)
tmp = (norminput.count_y // 5) + 1
while (tmp< norminput.count_y):
    area_y.append(tmp)
    tmp += (norminput.count_y // 5) + 1
if tmp < norminput.count_y + (norminput.count_y // 5):
    area_y.append(norminput.count_y)
print(area_x)
print(area_y)

for i in range(5):
    master(area_x[i], area_x[i + 1], area_y[i], area_y[i + 1], nokori)