import nltk
import re
import os

class ConsecutiveNPChunkTagger(nltk.TaggerI):
	def __init__(self, train_sents):
		train_set = []
		for tagged_sent in train_sents:
			untagged_sent = nltk.tag.untag(tagged_sent)
			history = []
			for i , (word,tag) in enumerate(tagged_sent):
				featureset = npchunk_features