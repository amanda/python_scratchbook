import nltk
from urllib import urlopen
import random

def simpletextgenerator():
	userUrl = raw_input('enter the project gutenberg .txt url: ')

	url = str(userUrl)
	raw = urlopen(url).read()

	tokens = nltk.word_tokenize(raw)
	text = nltk.Text(tokens)

	text.generate()

if __name__ == '__main__':
	print simpletextgenerator()