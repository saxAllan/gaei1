import collections
import statistics
import numpy
import norminput

print("\n========================================")
print("  judgements Ver. 3.2 (20191208)")
print("========================================\n")


# 初期化
start_x = 0
start_y = 0
label = 0
max_label = 0
samevalue = []
for i in range(2):
    samevalue.append([])
print("judgements 処理中...")

th = 1  # しきい値

# ラベリング

high = []
orghigh = []
for i in range(norminput.count_x):
    for j in range(norminput.count_y):
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

print(len(samevalue[0]), len(samevalue[1]))
len_same = len(samevalue[0])

nokori = []
for i in range(norminput.count_x):
    nokori.append([])
count_in = 0

for i in range(norminput.count_y):
    for j in range(norminput.count_x):
        nokori[j].append([])
        nokori[j][i].append(0)
        if norminput.data[j][i][0] <= medi_high:  #最頻値 or 中央値
            nokori[j][i][0] = norminput.data[j][i][0]
