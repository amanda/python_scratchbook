import nltk
from urllib import urlopen
import random

userUrl = raw_input('enter the project gutenberg .txt url: ')

url = str(userUrl)
raw = urlopen(url).read()

tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)

text.generate()