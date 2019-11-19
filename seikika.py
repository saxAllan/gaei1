filename_i = input("入力ファイル名（拡張子は不要）：")

print(filename_i + ".datを読み込んでいます...  ")
f = open(filename_i + ".dat", "r")
lines = f.readlines()
orgdata = []
for i in lines:
    orgdata.append(list(map(float, i.split())))
f.close()
size_org = len(orgdata)
print("読込完了 (", size_org, "行)")


num=len(orgdata)

cnt1=[]
cnt2=[]
del1=[]
del2=[]
a=0
b=0
cnt1.append(1)
cnt2.append(1)
for i in range(1,len(orgdata)):
    print("\r",i,end="  ")
    if orgdata[i][1]!=orgdata[i-1][1]:
        cnt1.append(1)
        a+=1
    else:
        cnt1[a]+=1
from operator import itemgetter
orgdata=sorted(orgdata,key=itemgetter(0))
for i in range(1,len(orgdata)):
    print("\r",i,end="  ")
    if orgdata[i][0]!=orgdata[i-1][0]:
        cnt2.append(1)
        b+=1
    else:
        cnt2[b]+=1
        
for i in range(len(cnt1)):
    if cnt1[i]!=max(cnt1):
        del1.append(cnt1[i])
for i in range(len(cnt2)):
    if cnt2[i]!=max(cnt2):
        del2.append(cnt2[i])

for i in range(len(del1)):
    for j in range(num):
        print("\r",i,end="  ")
        if orgdata[j][1]==del1[i]:
            orgdata.pop(j)

num=len(orgdata)

for i in range(len(del2)):
    for j in range(num):
        print("\r",i,end="  ")
        if orgdata[j][0]==del2[i]:
            orgdata.pop(j)

out=str("")
for i in range(len(orgdata)):
    print("\r",i,end="  ")
    if orgdata[i][2]>b[i][2]:
            orgdata[i][2]=b[i][2]
    out += str(orgdata[i][0])+" "
    out += str(orgdata[i][1])+" "
    out += str(orgdata[i][2])+" "
    #out += str(orgdata[i][3])+" "
    out += str("\n")

f=open(filename_o+".dat",mode="w")
f.write(out)
f.close()
print(filename_o+".dat を出力しました")
