
#maximu entrop >>> hetrogenous data
#min >> more homogenous data
#segmentatio ndone on the basis of enmtropy reduction

import math
def entropy(labels):
	freqdist = nltk.FreqDist(labels)
	probs = [freqdist.freq(l) for l in nltk.FreqDist(labels)]
	return -sum([p*math.log(p,2) for p in probs])