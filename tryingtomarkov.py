import nltk
from nltk import word_tokenize
from collections import defaultdict, Counter
from sys import argv
from random import choice

def make_markov_dict(text_file, tokens, ngram):
	with open(text_file) as f:
		words = word_tokenize(f.read())
	zippy_words = zip(*[words[i:] for i in xrange(ngram)])
	markov_dict = defaultdict(Counter)
	for t in zippy_words:
		a, b = t[:-1], t[-1]
		markov_dict[a][b] += 1
	return markov_dict




if __name__ == '__main__':
	#need error checking
	args = argv[:]
	input_file = args[1]
	with open(input_file) as f:
		my_text = ' '.join(f.readlines())
		my_markov_dict = make_markov_dict(my_text)
