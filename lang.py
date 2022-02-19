from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

import nltk
from nltk.corpus import conll2000
from nltk.chunk import conlltags2tree, tree2conlltags
from nltk.chunk import ne_chunk
from nltk import pos_tag

ex = 'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices'


def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent


sent = preprocess(ex)
# print(sent)

pattern = 'NP: {<DT>?<JJ>*<NN>}'
cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)
# print(cs)

from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint

iob_tagged = tree2conlltags(cs)
# pprint(iob_tagged)

ne_tree = ne_chunk(pos_tag(word_tokenize(ex)))
print(ne_tree)

import spacy
from spacy import displacy
from collections import Counter
# import en_core_web_sm

nlp = spacy.load("en_core_web_lg")


doc = nlp(
    'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices')
pprint([(X.text, X.label_) for X in doc.ents])
