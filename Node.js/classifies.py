# Example of Naive Bayes implemented from Scratch in Python
import csv
import random
import math

def loadCsv(filename):
	lines = csv.reader(open(filename, "rb"))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]
	return dataset

def splitDataset(dataset, splitRatio):
	trainSize = int(len(dataset) * splitRatio)
	trainSet = []
	copy = list(dataset)
	while len(trainSet) < trainSize:
		index = random.randrange(len(copy))
		trainSet.append(copy.pop(index))
	return [trainSet, copy]

def separateByClass(dataset):
	separated = {}
	for i in range(len(dataset)):
		vector = dataset[i]
		if (vector[-1] not in separated):
			separated[vector[-1]] = []
		separated[vector[-1]].append(vector)
	return separated

def mean(numbers):
	return sum(numbers)/float(len(numbers))

def stdev(numbers):
	avg = mean(numbers)
	variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
	return math.sqrt(variance)

def summarize(dataset):
	summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
	del summaries[-1]
	return summaries

def summarizeByClass(dataset):
	separated = separateByClass(dataset)
	summaries = {}
	for classValue, instances in separated.iteritems():
		summaries[classValue] = summarize(instances)
	return summaries

def calculateProbability(x, mean, stdev):
	exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
	return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent

def calculateClassProbabilities(summaries, inputVector):
	probabilities = {}
	for classValue, classSummaries in summaries.iteritems():
		probabilities[classValue] = 1
		for i in range(len(classSummaries)):
			mean, stdev = classSummaries[i]
			x = inputVector[i]
			probabilities[classValue] *= calculateProbability(x, mean, stdev)
	return probabilities
			
def predict(summaries, inputVector):
	probabilities = calculateClassProbabilities(summaries, inputVector)
	bestLabel, bestProb = None, -1
	for classValue, probability in probabilities.iteritems():
		if bestLabel is None or probability > bestProb:
			bestProb = probability
			bestLabel = classValue
	return bestLabel

def getPredictions(summaries, testSet):
	predictions = []
	for i in range(len(testSet)):
		result = predict(summaries, testSet[i])
		predictions.append(result)
	return predictions

def getAccuracy(testSet, predictions):
	correct = 0
	for i in range(len(testSet)):
		if testSet[i][-1] == predictions[i]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0

def main():
	filename = 'pima-indians-diabetes.data.csv'
	splitRatio = 0.67
	dataset = loadCsv(filename)
	trainingSet, testSet = splitDataset(dataset, splitRatio)
	print('Split {0} rows into train={1} and test={2} rows').format(len(dataset), len(trainingSet), len(testSet))
	# prepare model
	summaries = summarizeByClass(trainingSet)
	# test model
	predictions = getPredictions(summaries, testSet)
	accuracy = getAccuracy(testSet, predictions)
	print('Accuracy: {0}%').format(accuracy)

main()


s = socket.socket()         # Create a socket object
host = '127.0.0.1'           # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(10)

while 1:
    sc, address = s.accept()
    print ("Connection Established")# Now wait for client connection.
    lines = [line.rstrip('\n') for line in open('C:/Users/Raj/Desktop/movies/temp.txt')]
    #print (lines)
    Example_Text='\n'.join(lines)
    print ((Example_Text))


    picklename = "naivebayes1.pickle"
    classifier_f = open(picklename,"rb")
    classifier = pickle.load(classifier_f)

    revline= Example_Text.splitlines()
    for x in revline:
        print (x)
        doc = word_tokenize(x.lower())
        featurized_doc ={c:True for c in x.split()} #Check this how dictionary is being made
        print(classifier)
        tagged_label = classifier.classify(featurized_doc)
        print(tagged_label)#o/p polarity
        probb = classifier.prob_classify(featurized_doc)
        for sample in probb.samples():
            print("%s probability: %f" % (sample, probb.prob(sample)))
            f = open('C:/Users/Raj/Desktop/movies/sentiment.txt','a')
            f.write(sample+' '+str(probb.prob(sample))+' ')
        f.write('\n')
        f.close()

    #s.sendto("sent".encode(),("127.0.0.1",12345))
    
    sc.close()
    #s.close()













































