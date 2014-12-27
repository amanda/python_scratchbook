from nltk import word_tokenize
from random import choice

PATH_TO_STOP_WORDS = "/Users/amp/Dropbox/amanda/projects/python/python_scratchbook/stopwords_short.txt" #text file
DICT = "/Users/amp/Dropbox/amanda/projects/python/python_scratchbook/dict.txt"

with open(PATH_TO_STOP_WORDS) as f:
	stop_words = word_tokenize(f.read())

with open(DICT) as f:
	all_words = (f.read()).split('\n')

def without_the_e(text):
	'''removes the letter e from 
	words in a string that end with it'''
	tokens = word_tokenize(text)
	new = []
	for token in tokens:
		if token not in stop_words and token[-1] == 'e':
			token = token[:-1]
			new.append(token)
		else:
			new.append(token)
	return ' '.join(new)

def ends_in_e(text):
	'''returns the words that end in e
	in a string'''
	e_words = []
	tokens = word_tokenize(text)
	for token in tokens:
		if token not in stop_words and token[-1] == 'e':
			e_words.append(token)
	return e_words

def taking_back_sunday(wordlist):
	'''makes a potential tbs song from a list
	of words that end in e'''
	word = choice(wordlist)
	song = word + ' without the e (' + word[:-1] + ' from the team)'
	return song

def find_e_words(wordlist):
	'''used to find all the words that end in e
	from a list of words'''
	e_words = []
	for w in wordlist:
		if w[-1] == 'e':
			e_words.append(w)
	return e_words
