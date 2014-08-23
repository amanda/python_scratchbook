from textblob import TextBlob
from textblob.taggers import NLTKTagger

def make_pos_dict(some_text):
	nltk_tagger = NLTKTagger()
	blob = TextBlob(some_text, pos_tagger=nltk_tagger)
	pos_words = dict(blob.pos_tags)
	return pos_words

def get_nouns(posword_dict):
	nouns = [str(k) for k, v in posword_dict.iteritems() if (v == u'NNP' or v == u'NN' or v == u'NNS' or v == u'NNPS')]
	return nouns

def get_verbs(posword_dict):
	verbs = [k for k, v in posword_dict.iteritems() if (v == u'VB' or v == u'VBD' or v == u'VBG' or v == u'VBN' or v == u'VBP' or v == u'VBZ')]
	return verbs	

def get_adjs(posword_dict):
	adjs = [k for k, v in posword_dict.iteritems() if (v == u'JJ' or v == u'JJR' or v == u'JJS')]
	return adjs