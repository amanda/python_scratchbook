import nltk
from collections import defaultdict
from sys import argv

"""
1. tokenize --> list of strings
2. dictionary
	string: word that comes next, how often
3. current string, randomly pick next word from dictionary of words
"""

#tokenize a text using nltk
def get_words_from(some_file):
	tokens = nltk.wordpunct_tokenize(some_file)
	text = nltk.Text(tokens)
	words = [w.lower() for w in text]
	return words

# #dictionary of word and likeliness of next word
# word_dict = {
# 	"hello": {"there": 5},
# 	"there": {"world": 1}
# }
# #sample reference
# word_dict["hello"][1][1]

# #list of words in the text
# tokens = ["hello", "there", "world", "yeah", "cool"]

#loop through list of tokens to make dictionary of likelihoods

# for x in range(len(words)-1):
# 	if words[x] in word_dict:
# 		if words[x+1] in word_dict[words[x]]
# 			word_dict[words[x]][words[x+1]] += 1
# 		else:
# 			word_dict[words[x]][words[x+1]] = 1
# 	else:
# 		words[x] = {words[x+1]: 1}

def make_markov_dict(some_words):
	'''where the magic happens (i have no idea what i am doing)
	some_words is a list of words (the tokenized text)'''
	zippy_words = zip(some_words, some_words[1:])
	markov_dict = defaultdict(lambda: defaultdict(int))
	for a, b in zippy_words:
		markov_dict[a][b] += 1
	return markov_dict




if __name__ == '__main__':
	#need error checking
	input_file = args[1]
	with open(input_file) as f:
		my_text = ' '.join(f.readlines())
		my_words = get_words_from(my_text)
		my_markov_dict = make_markov_dict(my_words)
	
