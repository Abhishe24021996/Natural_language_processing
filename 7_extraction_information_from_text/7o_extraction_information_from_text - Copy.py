#steps
#sent_token>>word_tokenise>>pos>>EntityREcog>>RElationREcog
#(name, relation, name)

import nltk, re, pprint

def ie_preprocess(document):
  sentences = nltk.sent_tokenize(document)
  sentences = [nltk.word_tokenize(sent) for sent in sentences]
  sentences = [nltk.pos_tag(sent) for sent in sentences]
  
Chunking = "to label two three words together unlike pos which process only one word"
#CHUNKING
sentence = [("the","DT"),("little","JJ"),("DOG","NN"),("barked","VBD"),("at","IN"),("the","DT"),("cat","NN")]

GRAMMER = "NP: {<DT>?<JJ>*<NN>}"

cp = nltk.RegexpParser(grammer)
result = cp.parse(sentence)
print(result)

result.draw()


#nltk.app.chunkparser() use this tool to get help how to chunk

#use regex to combine two words tag to from chunks like Noun chunks or others.

#exploring text corpora
cp = nltk.Regexparser('CHUNK: {<V.*> <TO> <V.*>}')
brown = nltk.corpus.brown
for sent in brown.tagged_sent():
  tree = cp.parse(sent)
  for subtree in tree.subtrees():
    if subtree.node == 'CHUNK':
      print(subtree)
     
#chinking is the process of removing of tokens from chunks

#to chink
grammer = r"""
           NP: 
            {<.*>+} #CHUNK EVERYTHING
            }<VBD|IN>+{ #CHINK SEQ OF VBD AND IN
           """
           
#CHUNK REPRESENTATION
#WE USE tags B FOR BEGIN , I FOR INSIDE AND O FOR OUTSIDE (IOB FORMAT)
#B-NP, I-IN, O-OT, B-NP, I-NN, I-NNS

#cp.evaluate to evaluate a regex against already chunk corpus.

#training a chunker classifier that wil predict B I O of tags
#same use regexexp to run over already chunked sentences of connel data and then use to evalute how well it has predict 

#using unigramtagger or bigram to predict same by trainng

#a classifier MaxentClassifier insteed of NaiveBayes 





#recursion in chunking
#sometime we need to loop over or cascade to fetch chunks that were not detected at first
#cp = nltk.RegexParser(grammer, loop=2)

#to from a tree or family in chunks or tags
#tree1 = nltk.tree(results_from_tagger_chunk)
#tree[i].node
#tree[i].leaves()
#tree.draw

