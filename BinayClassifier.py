import sys
import nltk
import random
from nltk.corpus import PlaintextCorpusReader

def document_features(document, word_features):
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word]=(word in document_words)
	return features

def main(argv):
    l=[]
    with open("C:/Users/10Millionsoul/Desktop/apple-computers.txt") as infile:
    	for line in infile:
    		l=l+[w.lower() for w in line.split() if w.isalpha()]
    with open("C:/Users/10Millionsoul/Desktop/apple-fruit.txt") as infile:
    	for line in infile:
    		l=l+[w.lower() for w in line.split() if w.isalpha()]
    l=set(l)
    all_words = nltk.FreqDist(l)
    word_features=all_words.keys()
    train_set=[]
    with open("C:/Users/10Millionsoul/Desktop/apple-computers.txt") as infile:
    	for line in infile:
    		mylist=[w.lower() for w in line.split() if w.isalpha()]
    		train_set.append((document_features(mylist, word_features), 'computer-company'))
    with open("C:/Users/10Millionsoul/Desktop/apple-fruit.txt") as infile:
    	for line in infile:
    		mylist=[w.lower() for w in line.split() if w.isalpha()]
    		train_set.append((document_features(mylist, word_features), 'fruit'))
    random.shuffle(train_set)

    classifier = nltk.NaiveBayesClassifier.train(train_set)

    n=int(raw_input())
    for i in range(n):
    	s=raw_input()
    	temp=s.split()
    	mylist=[w.lower() for w in temp if w.isalpha()]
    	print classifier.classify(document_features(mylist, word_features))


if __name__ == "__main__":
    main(sys.argv)