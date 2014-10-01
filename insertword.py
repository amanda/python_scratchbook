def insert_word(sentence, word):
	'''gets all the variations of a sentence
	with a new word added after each existing word'''
	
	sentence = sentence.lower().strip()
	listy_sentence = sentence.split(' ')
	new = [listy_sentence[:i] + [word] + listy_sentence[i:] for i in range(len(listy_sentence))]
	sents = []
	for sent in new:
		sent = (' ').join(sent)
		sents.append(sent)
	return sents

if __name__ == '__main__':
	user_sentence = raw_input('enter a sentence: ')
	user_word = raw_input('enter a word to insert: ')
	print insert_word(user_sentence, user_word)
