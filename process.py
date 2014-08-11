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

#dataMat = []
#labelMat = []
#coordMat = []

fw = open("./data/dataset.txt","w")

for vec in Vec.items():
	#dataMat.append([vec[1][0]/maxtype[0],vec[1][1]/maxtype[1],vec[1][2]/maxtype[2],vec[1][3]/maxtype[3]])
	fw.write("%f,%f,%f,%f,%d,%d,%d\n" % (vec[1][0],vec[1][1],vec[1][2],vec[1][3],vec[1][4],vec[0][0],vec[0][1]))
	#dataMat.append([vec[1][0],vec[1][1],vec[1][2],vec[1][3]]);
	#labelMat.append(vec[1][4])
	#coordMat.append(vec[0])

fw.close()

fw = open("./data/actual.txt","w")

for item in actualMat:
	fw.write("%d %d\n" % (item[0],item[1]))

fw.close()
#print "actual:",len(actualMat)
#print "predict:",len(predictMat)
#print "data:",len(dataMat)

