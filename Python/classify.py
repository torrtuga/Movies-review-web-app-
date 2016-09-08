#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import string
from itertools import chain
from nltk.corpus import movie_reviews
#from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize
#from nltk.probability import FreqDist
#from nltk.classify import NaiveBayesClassifier as nbc
from nltk.classify import apply_features
#from nltk.corpus import CategorizedPlaintextCorpusReader
from textblob import TextBlob
import pickle
import nltk
import sys




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
        print(tagged_label)
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
