from numpy import *
import logRegres

fr = open("./data/out.txt","r")
Vec = {}

for line in fr.readlines():
	featureArr = line.strip().split()
	userId = int(featureArr[0])
	goodId = int(featureArr[1])
	typeId = int(featureArr[2])
	date = int(featureArr[3])
	if(date > 200): continue 
	coordinate = (userId,goodId)
	if not Vec.has_key(coordinate):
		Vec[coordinate] = [0,0,0,0,0]
	Vec[coordinate][typeId] += 1

fr.close()
fr = open("./data/out.txt","r")

actualMat = []
isexist = set()

for line in fr.readlines():
	featureArr = line.strip().split()
	userId = int(featureArr[0])
	goodId = int(featureArr[1])
	typeId = int(featureArr[2])
	date = int(featureArr[3])
	if(date <= 200): continue
	coordinate = (userId,goodId)
	if Vec.has_key(coordinate) and typeId == 1:
		Vec[coordinate][4] = 1
		if coordinate not in isexist:
			actualMat.append(coordinate)
			isexist.add(coordinate)

fr.close()

maxtype = [0, 0, 0, 0]

for vec in Vec.items():
	for i in range(4):
		maxtype[i] = max(maxtype[i],vec[1][i])

dataMat = []
labelMat = []
coordMat = []

fr = open("./data/dataset.txt","w")

for vec in Vec.items():
	#dataMat.append([vec[1][0]/maxtype[0],vec[1][1]/maxtype[1],vec[1][2]/maxtype[2],vec[1][3]/maxtype[3]])
	fr.write("%f,%f,%f,%f,%f,%d,%d\n" % (vec[1][0],vec[1][1],vec[1][2],vec[1][3],vec[1][4],vec[0][1],vec[0][1]))
	dataMat.append([vec[1][0],vec[1][1],vec[1][2],vec[1][3]]);
	labelMat.append(vec[1][4])
	coordMat.append(vec[0])

fr.close()

weights = logRegres.gradAscent(dataMat,labelMat)
predictMat = []

for i in range(len(dataMat)):
	predictClass = logRegres.classifyVector(dataMat[i],weights)
	if int(predictClass) == 1:
		predictMat.append(coordMat[i])

#print "actual:",len(actualMat)
#print "predict:",len(predictMat)
#print "data:",len(dataMat)

P = 0.0
for item in predictMat:
	if item in actualMat: P += 1.0
P /= len(predictMat)

R = 0.0
for item in actualMat:
	if item in predictMat: R += 1.0
R /= len(actualMat)

#print P,R

F1 = 2.0*P*R/(P+R)

#print F1

