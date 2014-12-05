from random import choice

FIRST = ['Negotiating', 'Performative', 'Navigating', 'Reconstructing']
SECOND = ['Identities', 'Gazes', 'Absence', 'Structures']
THIRD = ['Othered', 'Negated', 'Narrative', 'Structural']
FOURTH = ['Masculinities', 'Boundaries', 'Spaces', 'Constructivities']

def generate_thesis():
	title = choice(FIRST) + ' ' + choice(SECOND) + ' in ' + choice(THIRD) + ' ' + choice(FOURTH)
	return title
