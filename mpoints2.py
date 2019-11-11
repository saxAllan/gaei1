#欠損点削除
filename_i1=input("入力ファイル名1（拡張子は不要）：")
filename_i2=input("入力ファイル名2（拡張子は不要）：")
filename_o=input("出力ファイル名（拡張子は不要）：")

#----------ここからデータ読み込み----------
print(filename_i1+".datを読み込んでいます")
f=open(filename_i1+".dat","r")
lines=f.readlines()
orgdata1=[]
for i in lines:
    orgdata1.append(list(map(float, i.split())))
f.close()

for i in range(20):
    print(orgdata1[i])

print("      ...",len(orgdata1),"個のデータを読み込みました")

print(filename_i2+".datを読み込んでいます")
f=open(filename_i2+".dat","r")
lines=f.readlines()
orgdata2=[]
for i in lines:
    orgdata2.append(list(map(float, i.split())))
f.close()
for i in range(len(orgdata2)):
    orgdata2[i].append(0)

for i in range(20):
    print(orgdata2[i])

print("      ...",len(orgdata2),"個のデータを読み込みました")
#----------ここからデータ読み込み----------

#----------ここから欠損点処理----------
out = str("")
for i in range(len(orgdata1)):
    if orgdata1[i][2]+9999<1:
            orgdata1[i][3]=1
            orgdata1[i][2]=orgdata1[i-1][2]
for i in range(len(orgdata2)):
    if orgdata2[i][2]+9999<1:
            orgdata2[i][3]=1
            orgdata2[i][2]=orgdata2[i-1][2]
from operator import itemgetter
b=sorted(orgdata2,key=itemgetter(0))
for i in range(len(orgdata1)):
    if orgdata1[i][2]>b[i][2]:
            orgdata1[i][2]=b[i][2]
    out += str(orgdata1[i][0])+" "
    out += str(orgdata1[i][1])+" "
    out += str(orgdata1[i][2])+" "
    out += str(orgdata1[i][3])+" "
    out += str("\n")
#----------ここまで欠損点処理----------

f=open(filename_o+".dat",mode="w")
f.write(out)
f.close()
print(filename_o+".dat を出力しました")