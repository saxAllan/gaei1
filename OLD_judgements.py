#judgements Ver. 1.24(20191116)

import input

#----------def start----------
def labelling_x(x, y, labelno, list_equal):
    #xについて
    lxx = x
    lxy = y
    sa = (input.data[lxx][lxy][0] - input.data[lxx - 1][lxy][0]) * (input.data[lxx][lxy][0] - input.data[lxx - 1][lxy][0])
    while sa < 0.25:
        #print("labelling_x", lxx, lxy, labelno)  #デバッグ
        if input.data[lxx][lxy][1] != 0: #既にラベリングされてたら、input.data[lxx + 1][lxy][1]とlabelnoのデータを二次元配列に格納
            list_equal[0].append(input.data[lxx][lxy][1])
            list_equal[1].append(labelno)
        input.data[lxx][lxy][1] = labelno
        lxx += 1  #次のxへ
        if lxx == input.count_x - 1:
            break
        sa = (input.data[lxx][lxy][0] - input.data[lxx - 1][lxy][0]) * (input.data[lxx][lxy][0] - input.data[lxx - 1][lxy][0])

def labelling_base(base_x, base_y, base_label, base_equal):
    input.data[base_x][base_y][1] = base_label #スタートの点をラベリング
    #x方向へ
    if (base_x < input.count_x - 2):
        if (input.data[base_x + 1][base_y][1] == 0):
            #print("baseで呼んだよ！", base_x + 1, base_y)
            labelling_x(base_x + 1, base_y, base_label, base_equal)
    #y方向へ
    wi = 0
    if base_y < input.count_y - 1:
        while input.data[base_x + wi][base_y + 1][1] == base_label:
            if (input.data[base_x + wi][base_y + 1][0] - input.data[base_x + wi][base_y][0]) * (input.data[base_x + wi][base_y + 1][0] - input.data[base_x + wi][base_y][0]) < 0.25:
                    #print("yの話！", base_x + wi, base_y + 1)
                    labelling_base(base_x + wi, base_y + 1, base_label, base_equal)  #再帰でもう一度baseを呼ぶ
            wi += 1

#----------def end----------

#----------main start----------
#初期化
equal = []
for i in range (2):
    equal.append([])
start_x = 0
start_y = 0
label = 1

print("ラベリング処理中...")

#ラベリング
for i in range(input.count_x):
    for j in range(input.count_y):
        if input.data[i][j][1] == 0:
            print("\r", i + 1, "/", input.count_x, end="   ")
            labelling_base(i, j, label, equal)
            label += 1
print("処理終了")
#----------main end----------
