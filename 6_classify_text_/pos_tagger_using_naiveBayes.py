import nltk
import os
import sys


#tagged_sents = [(word,tag),.....] a sentence

def pos_features(sentence,i,history):
	features = {"suffix(1)":sentence[i][-1:],
				"suffix(2)":sentence[i][-2:],
				"suffix(3)": sentence[i][-3:]}

	if i == 0:
		features["prev-word"] = "<START>"
		features["prev-tag"]  = "<START>"
	else:
		features["prev-word"] = sentence[i-1]
		features["prev-tag"]  = sentence[i-1]
	return features

class ConsecutivePosTagger(nltk.TaggerI):
	def __init__(elf,train_sents):
		train_set = []
		for tagged_sent in train_sents:
			untagged_sent = nltl.tag.untag(tagged_sent)
			history = []
			for i ,(word,tag) in ennumerate(tagged_sents):
				fs = pos_features(untagged_sent, i , history)
				train_set.append((fs,tag))
				history.append(tag)
		self.classifier = nltk.NaiveBayesClassifier.train(train_set)
	def tag(self,sentence):
		history=[]
		for i, word in ennumerate(sentence):
			fs = pos_features(sentence, i , history)
			tag =self.classifier.classify(fs)
			history.append(tag)
		return zip(sentence, history)


#tagger.evaluate(test_Sents)

#nltk.DecisionTreeClassifier can also be used
#classifier.pseudocode(depth=4)
