from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
import numpy as np
import norminput
import mpointsl
import judgements

print("\n========================================")
print("  out Ver. 1.3 (20191124-7)")
print("========================================\n")


newdata = []
zdata = []
for i in range(norminput.count_y):
    for j in range(norminput.count_x):
        zdata.append(judgements.nokori[j][i][0])
        newdata.append(j)
        newdata.append(i)

print("Delaunay 処理中(多少時間がかかります)")
pts = np.array(newdata).reshape(-1, 2)
ztmp = np.array(zdata)
tri = Delaunay(pts)
newdata = pts.tolist()

temp_len = len(newdata)
for i in range(temp_len):
    newdata[i].append(zdata[i])
pts = np.array(newdata)
fig = plt.figure()
print("Delaunay 処理完了   (len(pts)=", len(pts), "), (len(pts[tri.simplices])=", len(pts[tri.simplices]), ")")

#出力
filename_o = "output"
outfile = open(filename_o + '.wrl', 'w')
print(filename_o + ".wrl として出力中...")

start = '#VRML V2.0 utf8\n'
outfile.write(start)
text1 = 'Shape {\ngeometry IndexedFaceSet { \nsolid FALSE\ncoord Coordinate { \npoint [\n'
outfile.write(text1)

temp_len=len(pts)
for i in range(temp_len):
    if i % 10000 == 0:
        print("\rpoint ", i // 10000, "/", temp_len // 10000, end="")
    for j in range(3):
        outfile.writelines(str(pts[i][j]))
        if j == 0 or j == 1:
            space = ' '
            outfile.write(space)
    conma = ',\n'
    outfile.write(conma)
print("   処理完了")

textc = ']\n}\ncoordIndex [\n'
outfile.write(textc)
temp_len=len(pts[tri.simplices])
for i in range(temp_len):
    if i % 10000 == 0:
        print("\rcoordIndex ", i // 10000, "/", temp_len // 10000, end="")
    for j in range(3):
        outfile.writelines(str(tri.simplices[i][j]))
        conma2 = ','
        outfile.write(conma2)
    conma3 = '-1,\n'
    outfile.write(conma3)
print("処理完了")
text2 = ']\n}\nappearance Appearance { \nmaterial\nMaterial {}\n}\n}\n'
outfile.write(text2)
outfile.close()

print("\n出力完了 ("+filename_o + ".wrl )\n")
