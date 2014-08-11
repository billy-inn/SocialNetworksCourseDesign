# calculate some useful value and present them

actualMat = []
predictMat = []

fr = open("./data/actual.txt","r")

for line in fr.readlines():
	arr = line.strip().split()
	actualMat.append((arr[0],arr[1]))

fr.close()
fr = open("./data/predict.txt","r")

for line in fr.readlines():
	arr = line.strip().split()
	predictMat.append((arr[0],arr[1]))

fr.close()

P = 0.0
for item in predictMat:
	if item in actualMat: P += 1.0
print "targets hit:",int(P)
P /= len(predictMat)

R = 0.0
for item in actualMat:
	if item in predictMat: R += 1.0
R /= len(actualMat)

print "actual:",len(actualMat),"predict:",len(predictMat)
print "P:",P,"R:",R

F1 = 2.0*P*R/(P+R)

print "F1:",F1

