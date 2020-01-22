#recognising textual entailemnet
#require pair of sentences to do hypothesis
def rte_features(rtepair):
  extractor = nltk.RTEFEatureExtractor(rtepair)
  features ={}
  features['word-overlap'] = len(extractor.overlap('word'))
  features['word-hyp-extra'] = len(extractor.hyp_extra('word'))
  features['ne-overlap'] = len(extractor.overlap('ne'))
  features['ne-hyp-extra'] = len(extractor.hyp_extra('ne'))
  return features

#nltk.classify.rte_classify            
             
#nltk.ConfusionMatrix(gold,test)