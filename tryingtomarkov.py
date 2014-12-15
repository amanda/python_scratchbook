from nltk import word_tokenize
from collections import defaultdict, Counter
from sys import argv
import random
import operator
import bisect
import string

def make_markov_dict(text, ngram):
	words = word_tokenize(text)
	zippy_words = zip(*[words[i:] for i in xrange(ngram)])
	markov_dict = defaultdict(Counter)
	for t in zippy_words:
		a, b = t[:-1], t[-1]
		markov_dict[a[0]][b] += 1
	return markov_dict

def accumulate(iterable, func=operator.add):
	it = iter(iterable)
	total = next(it)
	yield total
	for el in it:
		total = func(total, el)
		yield total

def choose_word(start_key, freq_dict):
	choices, weights = zip(*freq_dict[start_key].iteritems())
	cumulative_distribution = list(accumulate(weights))
	rando = random.random() * cumulative_distribution[-1]
	return choices[bisect.bisect(cumulative_distribution, rando)]

def generate_tweet(markov_dict): #only for ngram 2 so far
	start_key = choose_word('.', markov_dict)
	sentence_length = 0
	sentence = [start_key, ' ']
	while sentence_length < 90:
		next_key = choose_word(sentence[-2], markov_dict)
		sentence_length += len(next_key) + 1
		if next_key in string.punctuation:
			del sentence[-1]
			sentence.append(next_key)
		else:
			sentence.append(next_key)
			sentence.append(' ')
	last_word = sentence[-2]
	for i in xrange(4): #try four times to get a good end of sentence
		if '.' in markov_dict[last_word].values():
			sentence.append('.')
			return ''.join(sentence)
		else:
			last_word = choose_word(last_word, markov_dict)
			continue
	del sentence[-1] 
	sentence.append('.')
	return ''.join(sentence)

if __name__ == '__main__':
	with open(sys.arv[1]) as f:
		my_markov = make_markov_dict(f.read())
	print generate_tweet(my_markov)
