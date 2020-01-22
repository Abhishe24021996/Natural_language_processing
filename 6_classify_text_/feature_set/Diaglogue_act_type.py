#example posts = nltk.corpus.nps_chat.xml_posts()[:10000]

def dialogue_act_features(post):
	features = {}
	for word in nltk.word_tokenize(post):
		features['contains(%s)' %word.lower()] = True
	return features

