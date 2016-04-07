import numpy as np

trainFeaturesOld = open('hw12data/digitsDataset/trainFeatures.csv', 'r').readlines()
trainLabels = open('hw12data/digitsDataset/trainLabels.csv', 'r').readlines()
testFeatures = open('hw12data/digitsDataset/testFeatures.csv', 'r').readlines()
testLabels = open('hw12data/digitsDataset/digitsOutput.csv', 'w')

k = 5
errorcount = 0

def majority(list):
	dict = {}
	for label, distance in list:
		if label not in dict:
			dict[label] = (1, [distance])

		else:
			dict[label] = (dict[label][0] + 1, dict[label][1]+distance)
	lad = sorted(dict.items(), key = lambda x: (-x[1][0], x[1][1]))
	return lad[0][0]

trainFeatures = []
for line in trainFeaturesOld:
	trainFeatures.append(np.array(tuple(map(float, line.split(",")))))

for i, valfeatureset in enumerate(testFeatures):
	distances = []
	a = np.array(tuple(map(float, valfeatureset.split(","))))
	for j, trainfeatureset in enumerate(trainFeatures):
		b = trainfeatureset
		distances.append((j, np.linalg.norm(a-b)))
	distances = sorted(distances, key = lambda x: x[1])
	knn = []
	for l in range(0, k):
		indexOfLabel = distances[l][0]
		knn.append((int(trainLabels[indexOfLabel]), distances[l][1]))
	prediction = majority(knn)
	testLabels.write(str(prediction) + "\n")