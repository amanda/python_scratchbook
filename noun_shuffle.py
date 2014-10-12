import nltk
from textblob import TextBlob
from textblob.taggers import NLTKTagger
import random
from sys import argv

def make_pos_dict(text):
	nltk_tagger = NLTKTagger()
	blob = TextBlob(text, pos_tagger=nltk_tagger)
	pos_words = dict(blob.pos_tags)
	return pos_words

def get_nouns(posword_dict):
	nouns = [str(k) for k, v in posword_dict.iteritems() if (v == u'NNP' or v == u'NN' or v == u'NNS' or v == u'NNPS')]
	return nouns

# def shuffle_list(some_list): 
#	just use random.shuffle! whoops
# 	insert_where = random.randint(0, len(some_list))
# 	for i in range(0, len(some_list)):
# 		item = some_list.pop(i)
# 		some_list.insert(insert_where, item)
# 	return some_list

def get_indices(token_list, noun_list):
	indices = []
	for i in token_list:
		if i in noun_list:
			indices.append(token_list.index(i))
	return indices

# def get_tokens(text):
# 	with open(text_file) as f:
# 		text = ' '.join(f.readlines())
# 		blob = TextBlob(text)
# 		tokens = list(blob.words)
# 	return tokens


def shuffle_nouns(text_file):
	#needs some error checking
	#maybe make getting tokens a different function
	with open(text_file) as f:
		text = ' '.join(f.readlines())
		blob = TextBlob(text)
		tokens = list(blob.words) #cast WordList as a list
		pos_text = make_pos_dict(text)
		nouns = get_nouns(pos_text) #this is a list
		extra_nouns = nouns[:] #for when a noun occurs more than once
		noun_indices = get_indices(tokens, nouns)
		random.shuffle(nouns)
		random.shuffle(extra_nouns)

		for index in noun_indices:
			if nouns:
				tokens[index] = nouns.pop()
			else:
				tokens[index] = extra_nouns.pop()

		return (' '.join(tokens)).lower()



if __name__ == '__main__':
	args = argv[:]
	input_file = args.pop()
	print shuffle_nouns(input_file)
