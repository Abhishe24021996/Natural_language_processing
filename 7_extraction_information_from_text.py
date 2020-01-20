#gender identification

def gender_features2(name):
  feautres["firstletter"] = name[0].lower()
  feautres["lastletter"] = name[-1].lower()
  for letter in 'abcdefghijklmnopqrstuvwxyz':
    feautres["count(%s)"%letter] = name.lower().count(letter)
    feautres["has(%s)"%letter] = (letter in name.lower())
  return feautres
  
from nltk.corpus import names
import random
names = ([(name,'male') for name in names.words("male.txt")]+
        [(name,'female') for name in names.words(female.txt)])
        
random.shuffle(names)

train_names = names[1500:]
devtest_names = names[500:1500]
test_names = names[:500]

train_sets = [(gender_features2(n),g) for (n,g) in train_names]
devtest_sets = [(gender_features2(n),g) for (n,g) in devtest_names]
test_sets = [(gender_features2(n),g) for (n,g) in test_names]

classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier,devset_sets)

#to implement new rules by analysing errors
errors = []
for name, tag in devset_names:
  guess = classifier.classify(gender_features2(name))
  if guess != tag:
    error.append((tag, guess, name))
    
for (tag, guess, name) in sorted(errors):
  print('correct=%s guess=%s name=%s'%(tag, guess, name))
  
#other functions
#classifier.show_most_informative_features(5)



##Document classification
from nltk.corpus import movie_reviews
documents = [(list(movie_reviews.words(fileid)), category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000]

def document_features(document):
  document_words = set(document)
  features = {}
  for word in word_features:
    features['contains(%s)' %word] = (word in document_words)
  return features
  
featuresets = [(document_features(d), c) for d, c in documents]
train_sets, test_sets = featuressets[100:] , featuressets[100:]

classifier
#accuracy
#mostindormative 


#featureset for pos tagging
from nltk.corpus import brown
suffix_fdist = nltk.FreqDist()
for word in brown.words():
  word = word.lower()
  suffix_fdist.inc(word[-1:])
  suffix_fdist.inc(word[-2:])
  suffix_fdist.inc(word[-3:])
  
common_suffixes = suffix_fdist.keys()[:100]

def pos_features(word):
  features = {}
  for suffix in common_suffixes:
    features['endswith(%s)' %suffix] = word.lower().endswith(suffix)
  return features
  
#do as same 229
classifier.pseudocode(depth=4)

#exploiting context
def pos_features(sentence,i):
  features = {"suffix(1)" : sentence[i][-1:],
              "suffix(1)" : sentence[i][-2:],
              "suffix(1)" : sentence[i][-3:]}
              
  if i == 0 :
    features["prev-word" = "<START>"
  else:
    features["prev-word"] = sentence[i-1]
return features

             
#sentence segmentor
sents = nltk.corpus.treebank_raw.sents()
tokens =[]
boundaries = set()
offset = 0
for sent in sents:
  tokens.extend(sent)
  offset += len(sent)
  boundaries.add(offset-1)
             
def punct_features(tokens, i ):
  return {'next-word-capitalised' : tokens[i+1][0].isupper(),
          'prevword':tokens[i-1].lower()
          'punct':tokens[i],
          'prev-word-is-one-char': len(tokens[i-1])==1}
             
fs = [(punct_features(tokens,i), (i in boundaries))
      for i in range(1, len(tokens)-1)
      if tokens[i] in '.?!']

#recognising textual entailemnet
def rte_features(rtepair):
  extractor = nltk.RTEFEatureExtractor(rtepair)
  features ={}
  features['word-overlap'] = len(extractor.overlap('word'))
  features['word-hyp-extra'] = len(extractor.hyp_extra('word'))
  features['ne-overlap'] = len(extractor.overlap('ne'))
  features['ne-hyp-extra'] = len(extractor.hyp_extra('ne'))
  return features
