from sys import argv
from textblob import TextBlob
from textblob.taggers import NLTKTagger
import random

def make_pos_dict(some_text):
	nltk_tagger = NLTKTagger()
	blob = TextBlob(some_text, pos_tagger=nltk_tagger)
	pos_words = dict(blob.pos_tags)
	return pos_words

def get_nouns(posword_dict):
	nouns = [str(k) for k, v in posword_dict.iteritems() if (v == u'NNP' or v == u'NN' or v == u'NNS' or v == u'NNPS')]
	return nouns

def get_adjs(posword_dict):
	adjs = [k for k, v in posword_dict.iteritems() if (v == u'JJ' or v == u'JJR' or v == u'JJS')]
	return adjs


if __name__ == '__main__':
	with open(argv[1]) as f:
		text = ' '.join(f.readlines())
		pos_text = make_pos_dict(text)
		adjs = get_adjs(pos_text)
		nouns = get_nouns(pos_text)
		print random.choice(adjs) + ' ' + random.choice(nouns)
