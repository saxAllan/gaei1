#地面判定
import numpy
import norminput
import statistics

print("\n========================================")
print("  judgements Ver. 4.9 (20200113)")
print("========================================\n")

def master(xstart, xend, ystart, yend, nokori):
    print("(",xstart, xend, ystart, yend,")",end="   ")
    high = []
    for i in range(xstart, xend):
        for j in range(ystart, yend):
            if norminput.data[i][j][0] < 30:
                high.append((norminput.data[i][j][0] // 2) * 2)  # 下から用
                norminput.data[i][j][1] = (norminput.data[i][j][0] // 2) * 2  # 下から用
            else:
                high.append(18)  # 下から用
                norminput.data[i][j][1] = (norminput.data[i][j][0] // 2) * 2  # 下から用
    # 標高差の判定（x方向）
    tmp = 0
    for i in range(ystart, yend):
        tmp += norminput.data[xstart][i][1]
    xstart_ave = tmp / (yend - ystart)
    #print(xstart_ave)
    tmp = 0
    for i in range(ystart, yend):
        tmp += norminput.data[xend-1][i][1]
    xend_ave = tmp / (yend - ystart)
    #print(xend_ave)
    if (xend_ave - xstart_ave) * (xend_ave - xstart_ave) > 144 and xend-xstart>100:
        master(xstart, (xstart + xend) // 2, ystart, yend, nokori)
        master((xstart + xend) // 2, xend, ystart, yend, nokori)
    else:
        # 標高差の判定（y方向）
        tmp = 0
        for i in range(xstart, xend):
            tmp += norminput.data[i][ystart][1]
        ystart_ave = tmp / (xend - xstart)
        #print(ystart_ave)
        tmp = 0
        for i in range(xstart, xend):
            tmp += norminput.data[i][yend-1][1]
        yend_ave = tmp / (yend - ystart)
        #print(yend_ave)
        if (yend_ave - ystart_ave) * (yend_ave - ystart_ave) > 300 and yend-ystart>50:
            master(xstart, xend, ystart, (ystart + yend) // 2, nokori)
            master(xstart, xend, (ystart + yend) // 2, yend, nokori)
        else:
            # 下から
            high_list = []
            mode_high = 4
            for i in range(40):
                high_list.append(high.count(i))
            # print(high_list)
            tmphigh = 0
            for i in range(40):
                tmphigh += high_list[i]
                if tmphigh > 2000:
                    mode_high = i + 3
                    break
            if tmphigh <= 2000:
                mode_high = statistics.mode(high)

            # 四分位数
            print("    下からx:", mode_high, )

            for i in range(ystart, yend):
                for j in range(xstart, xend):
                    if norminput.data[j][i][1] <= mode_high:  # 下から
                        nokori[j][i][0] = norminput.data[j][i][0]
                        norminput.data[j][i][1] = 0
                    else:
                        norminput.data[j][i][1] = 1


# ここからmain
start_x = 0
start_y = 0
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
divide_x = 23
divide_y = 5
tmp = (norminput.count_x // divide_x) + 1
while (tmp < norminput.count_x):
    area_x.append(tmp)
    tmp += (norminput.count_x // divide_x) + 1
if tmp < norminput.count_x + (norminput.count_x // divide_x):
    area_x.append(norminput.count_x)
tmp = (norminput.count_y // divide_y) + 1
while (tmp < norminput.count_y):
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

#余分点削除
for i in range(1, norminput.count_x - 1):
    for j in range(1, norminput.count_y - 1):
        if norminput.data[i][j][1] == 0:            
            tmp0 = norminput.data[i - 1][j + 1][1]
            tmp1 = norminput.data[i][j + 1][1]
            tmp2 = norminput.data[i + 1][j + 1][1]
            tmp3 = norminput.data[i + 1][j][1]
            tmp4 = norminput.data[i + 1][j - 1][1]
            tmp5 = norminput.data[i][j - 1][1]
            tmp6 = norminput.data[i - 1][j - 1][1]
            tmp7 = norminput.data[i - 1][j][1]
            if tmp0 + tmp1 + tmp2 + tmp3 + tmp4 + tmp5 + tmp6 + tmp7 == 8:
                norminput.data[i][j][1] = 1

        


'''メモ
地図の横は1.1kmくらい、縦は0.9kmくらい

＊パラメータの選択肢＊
94-95行目 大本の地図分割数
36、46行目 関数中での判定条件（どれだけの勾配か、どれだけの最低距離か）

１点だけひょこって

'''
