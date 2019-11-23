#outwrl Ver.1.0(20191124)
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
import numpy as np

filename_i=input("入力ファイル名（拡張子は不要):")
filename_o="output"

print(filename_i+".datを読み込んでいます")
f=open(filename_i+".dat","r")
lines=f.readlines()
orgdata=[]
for i in lines:
        orgdata.append(list(map(float,i.split())))
f.close()
"""
for i in range(len(orgdata)):
    print(orgdata[i])
print(" ...",len(orgdata),"個のデータを読み込みました")
"""
newdata=[]
zdata=[]

for i in range(len(orgdata)):
    zdata.append(orgdata[i][2])
    for j in range(2):
        newdata.append(orgdata[i][j])

pts=np.array(newdata).reshape(-1, 2)
ztmp=np.array(zdata)

tri = Delaunay(pts)

newdata=pts.tolist()

for i in range(len(newdata)):
    newdata[i].append(zdata[i])

pts=np.array(newdata)

fig=plt.figure()

print("ドロネー完了")
print(len(pts))
print(len(pts[tri.simplices]))

file = open('norm.wrl', 'w')
start='#VRML V2.0 utf8\n'
file.write(start)
text1='Shape {\ngeometry IndexedFaceSet { \nsolid FALSE\ncoord Coordinate { \npoint [\n'
file.write(text1)

for i in range(len(pts)):
    if i%10000==0:
        print("point ",i)
    for j in range(3):
        file.writelines(str(pts[i][j]))
        if j==0 or j==1:
            space=' '
            file.write(space)
    conma=',\n'
    file.write(conma)

textc=']\n}\ncoordIndex [\n'
file.write(textc)
        
for i in range(len(pts[tri.simplices])):
    if i%10000==0:
        print("coordIndex ",i)
    for j in range(3):
        file.writelines(str(tri.simplices[i][j]))
        conma2=','
        file.write(conma2)
    conma3='-1,\n'
    file.write(conma3)
    
text2=']\n}\nappearance Appearance { \nmaterial\nMaterial {}\n}\n}\n'
file.write(text2)
file.close()
