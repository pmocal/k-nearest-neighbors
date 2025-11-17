import fileinput
import numpy

def majority(list):
	dict = {}
	for label, distance in list:
		if label not in dict:
			dict[label] = (1, [distance])
		else:
			dict[label] = (dict[label][0] + 1, dict[label][1] + distance)
	lad = sorted(dict.items(), key = lambda x: (-x[1][0], x[1][1]))
	return lad[0][0]

def knn_validation():
    train_labels = open('digitsDataset/trainLabels.csv', 'r').readlines()
    val_labels = open('digitsDataset/valLabels.csv', 'r').readlines()

    k = 10
    error_count = 0

    train_features = []
    with open('digitsDataset/trainFeatures.csv', 'r') as train_features_old:
        for line in train_features_old:
            train_features.append(numpy.array(tuple(map(float, line.split(',')))))
        predicted_val_labels = []

    with fileinput.input(files=('digitsDataset/valFeatures.csv')) as val_features:
        for val_feature_set in val_features:
            distances = []
            a = numpy.array(tuple(map(float, val_feature_set.split(','))))
            for j, train_feature_set in enumerate(train_features):
                b = train_feature_set
                distances.append((j, numpy.linalg.norm(a - b)))
            distances = sorted(distances, key = lambda x: x[1])
            knn = []
            for l in range(0, k):
                label_index = distances[l][0]
                knn.append((int(train_labels[label_index]), distances[l][1]))
            prediction = majority(knn)
            if prediction != int(val_labels[fileinput.lineno()-1]):
                error_count += 1
                print(f'predicted {prediction}')
                print(predicted_val_labels)
            predicted_val_labels.append(prediction)
        print(error_count)

def knn_test():
    train_labels = open('digitsDataset/trainLabels.csv', 'r').readlines()

    k = 5
    error_count = 0
    
    train_features = []
    with open('digitsDataset/trainFeatures.csv', 'r') as train_features_old:
        for line in train_features_old:
            train_features.append(numpy.array(tuple(map(float, line.split(',')))))

    with fileinput.input(files=('digitsDataset/testFeatures.csv')) as test_features:
        for test_feature_set in test_features:
            distances = []
            a = numpy.array(tuple(map(float, test_feature_set.split(','))))
            for j, train_feature_set in enumerate(train_features):
                b = train_feature_set
                distances.append((j, numpy.linalg.norm(a - b)))
            distances = sorted(distances, key = lambda x: x[1])
            knn = []
            for l in range(0, k):
                label_index = distances[l][0]
                knn.append((int(train_labels[label_index]), distances[l][1]))
            prediction = majority(knn)
            with open('digitsDataset/digitsOutput.csv', 'a') as test_labels:
                test_labels.write(str(prediction) + '\n')