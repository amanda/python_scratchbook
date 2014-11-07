CARDS = {'ace of cups': 'feasting, banquet, good cheer',
		 'ace of pentacles': 'perfect contentment, felicity, prosperity, triumph',
		 'ace of swords': 'triumph, fecundity, fertility, prosperity',
		 'ace of wands': 'birth, commencement, beginning, origin, source',
		 'death': 'death, change, transformation, alteration for the worse',
		 'eight of cups': 'a fair girl, friendship, attachment, tenderness',
		 'eight of pentacles': 'a dark girl, beauty, candour, chastity, innocence, modesty',
		 'eight of swords': 'sickness, calumny, criticism, blame',
		 'eight of wands': 'understanding, observation, direction',
		 'five of cups': 'union, junction, marriage, inheritance',
		 'five of pentacles': 'lover or mistress, love, sweetness, affection, pure and chaste love',
		 'five of swords': 'mourning, sadness, affliction',
		 'five of wands': 'gold, opulence, gain, heritage, riches, fortune, money',
		 'four of cups': 'ennui, displeasure, discontent, dissatisfaction',
		 'four of pentacles': 'pleasure, gaiety, enjoyment, satisfaction',
		 'four of swords': 'solitude, retreat, abandonment, solitary, hermit',
		 'four of wands': 'society, union, association, concord, harmony',
		 'judgment': 'renewal, result, determination of a matter',
		 'justice': 'equity, rightness, probity, executive; triumph of the deserving side in law',
		 'king of cups': 'a fair man, goodness, kindness, liberality, generosity',
		 'king of pentacles': 'a dark man, victory, bravery, courage, success',
		 'king of swords': 'a lawyer, a man of law, power, command, superiority, authority',
		 'king of wands': 'man living in the country, country gentleman, knowledge, education',
		 'knight of cups': 'arrival, approach, advance',
		 'knight of pentacles': 'a useful man, trustworthy, wisdom, economy, order, regulation',
		 'knight of swords': 'a soldier, a man whose profession is arms, skilfulness, capacity, address, promptitude',
		 'knight of wands': 'departure, separation, disunion',
		 'nine of cups': 'victory, advantage, success, triumph, difficulties surmounted',
		 'nine of pentacles': 'discretion, circumspection, prudence, discernment',
		 'nine of swords': 'an ecclesiastic, a priest, conscience. probity, good faith, integrity',
		 'nine of wands': 'order, discipline, good arrangement, disposition',
		 'page of cups': 'a fair youth, confidence, probity, discretion, integrity',
		 'page of pentacles': 'a dark youth, economy, order, rule, management',
		 'page of swords': 'a spy, overlooking, authority',
		 'page of wands': 'a good stranger, good news, pleasure, satisfaction',
		 'queen of cups': 'a fair woman, success, happiness, advantage, pleasure',
		 'queen of pentacles': 'a dark woman, a generous woman, liberality, greatness of soul, generosity',
		 'queen of swords': 'widowhood, loss, privation, absence, separation',
		 'queen of wands': 'woman living in the country, lady of the manor, love of money, avarice, usury',
		 'seven of cups': 'idea, sentiment, reflection, project',
		 'seven of pentacles': 'money, finance, treasure, gain, profit',
		 'seven of swords': 'hope, confidence, desire, attempt, wish',
		 'seven of wands': 'success, gain, advantage, profit, victory',
		 'six of cups': 'the past, passed by, faded, vanished, disappeared',
		 'six of pentacles': 'presents, gifts, gratification',
		 'six of swords': 'envoy, messenger, voyage, travel',
		 'six of wands': 'attempt, hope, desire, wish, expectation',
		 'strength': 'power, energy, action, courage, magnanimity; also complete success and honours',
		 'temperance': 'economy, moderation, frugality, management, accommodation',
		 'ten of cups': 'the town wherein one resides, honour, consideration, esteem, virtue, glory, reputation',
		 'ten of pentacles': 'house, dwelling, habitation, family',
		 'ten of swords': 'tears, affliction, grief, sorrow',
		 'ten of wands': 'confidence, security, honour, good faith',
		 'the chariot': 'succour, providence also war, triumph, presumption, vengeance, trouble',
		 'the devil': 'ravage, violence, vehemence, extraordinary efforts, force, fatality; that which is predestined but is not for this reason evil',
		 'the emperor': 'stability, power, protection, realization; a great person; aid, reason, conviction; also authority and will',
		 'the empress': 'fruitfulness, action, initiative, length of days; the unknown, clandestine; also difficulty, doubt, ignorance',
		 'the fool': 'folly, mania, extravagance, intoxication, delirium, frenzy, bewrayment',
		 'the hanged man': 'wisdom, circumspection, discernment, trials, sacrifice, intuition, divination, prophecy',
		 'the hermit': 'prudence, circumspection; also and especially treason, dissimulation, roguery, corruption',
		 'the hierophant': 'marriage, alliance, captivity, servitude; by another account, mercy and goodness; inspiration',
		 'the high priestess': 'secrets, mystery, the future as yet unrevealed; the person who interests the querent',
		 'the lovers': 'attraction, love, beauty, trials overcome',
		 'the magician': 'skill, diplomacy, address, subtlety; sickness, pain, loss, disaster, snares of enemies; self-confidence, will',
		 'the moon': 'hidden enemies, danger, calumny, darkness, terror, deception, occult forces, error',
		 'the star': 'hope, expectation, bright promises',
		 'the sun': 'happiness, content, joy',
		 'the tower': 'ruin, disruption, over-throw, loss, bankruptcy',
		 'the wheel of fortune': 'destiny, fortune, success, elevation, luck, felicity',
		 'the world': 'assured success, recompense, voyage, route, emigration, flight, change of place',
		 'three of cups': 'success, triumph, victory, favourable issue',
		 'three of pentacles': 'nobility, elevation, dignity, rank, power',
		 'three of swords': 'a nun, separation, removal, rupture, quarrel',
		 'three of wands': 'enterprise, undertaking, commerce, trade, negotiation',
		 'two of cups': 'love, attachment, friendship, sincerity, affection',
		 'two of pentacles': 'embarrassment, worry, difficulties',
		 'two of swords': 'friendship, valour, firmness, courage',
		 'two of wands': 'riches, fortune, opulence, magnificence, grandeur'}


INVERTED = {'ace of cups': 'change, novelty, metamorphosis, inconstancy',
			 'ace of pentacles': 'purse of gold, money, gain, help, profit, riches',
			 'ace of swords': 'embarrassment, foolish and hopeless love, obstacle, hindrance',
			 'ace of wands': 'persecution, pursuits voilence, vexation, cruelty, tyranny',
			 'death': 'inertia, sleep, lethargy, petrifaction, somnambulism; hope destroyed',
			 'eight of cups': 'gaiety, feasting, joy, pleasure',
			 'eight of pentacles': 'flattery, usury, hypocrisy, shifty',
			 'eight of swords': 'treachery in the past, event, accident, remarkable incident',
			 'eight of wands': 'quarrels, intestine disputes, discord',
			 'five of cups': 'arrival, return, news, surprise, false projects',
			 'five of pentacles': 'disgraceful love, imprudence, license, profligacy',
			 'five of swords': 'losses trouble (same signification, whether reversed or not)',
			 'five of wands': 'legal proceedings, judgment, law, lawyer, tribunal',
			 'four of cups': 'new acquaintance, conjecture, sign, presentiment',
			 'four of pentacles': 'obstacles, hindrances',
			 'four of swords': 'economy, precaution, regulation of expenditure',
			 'four of wands': 'prosperity, success, happiness, advantage',
			 'judgment': 'weakness, pusillanimity, simplicity; also deliberation, decision, sentence',
			 'justice': 'law in all its departments, legal complications, bigotry, bias, excessive severity',
			 'king of cups': 'a man of good position, but shifty in his dealings, distrust, doubt, suspicion',
			 'king of pentacles': 'an old and vicious man, a dangerous man, doubt, fear, peril, danger',
			 'king of swords': 'a wicked man, chagrin, worry, grief, fear, disturbance',
			 'king of wands': 'a naturally good but severe man, counsel, advice, deliberation',
			 'knight of cups': 'duplicity, abuse of confidence, fraud, cunning',
			 'knight of pentacles': 'a brave man, but out of employment, idle, unemployed, negligent',
			 'knight of swords': 'a conceited fool, ingenuousness, simplicity',
			 'knight of wands': 'rupture, discord, quarrel',
			 'nine of cups': 'faults, errors, mistakes, imperfections',
			 'nine of pentacles': 'deceit, bad faith, artifices, deception',
			 'nine of swords': 'wise distrust, suspicion, fear, doubt, shady character',
			 'nine of wands': 'obstacles, crosses, delay, displeasure',
			 'page of cups': 'a flatterer, deception, artifice',
			 'page of pentacles': 'prodigality, profusion, waste, dissipation',
			 'page of swords': 'that which is unforeseen, vigilance, support',
			 'page of wands': 'ill news, displeasure, chagrin, worry',
			 'queen of cups': 'a woman in good position, but intermeddling, and to be distrusted; success, but with some attendant trouble',
			 'queen of pentacles': 'certain evil, a suspicious woman, a woman justly regarded with suspicion, doubt, mistrust',
			 'queen of swords': 'a bad woman, ill-tempered and bigoted, riches and discord, abundance together with worry, joy with grief',
			 'queen of wands': 'a good a virtuous woman, but strict and economical, obstacles, resistance, opposition',
			 'seven of cups': 'plan, design, resolution, decision',
			 'seven of pentacles': 'disturbance, worry, anxiety, melancholy',
			 'seven of swords': 'wise advice, good counsel, wisdom, prudence, circumspection',
			 'seven of wands': 'indecision, doubt, hesitation, embarrassment, anxiety',
			 'six of cups': 'the future, that which is to come, shortly, soon',
			 'six of pentacles': 'ambition, desire, passion, aim, longing',
			 'six of swords': 'declaration, love proposed, revelation, surprise',
			 'six of wands': 'infidelity, treachery, disloyalty, perfidy',
			 'strength': 'despotism, abuse if power, weakness, discord, sometimes even disgrace',
			 'temperance': 'ill-advised combinations, disunion, clashing interests, etc.',
			 'ten of cups': 'combat, strife, opposition, differences, dispute',
			 'ten of pentacles': 'gambling, dissipation, robbery, loss',
			 'ten of swords': 'passing success, momentary advantage',
			 'ten of wands': 'treachery, subterfuge, duplicity, bar',
			 'the chariot': 'riot, quarrel, dispute, litigation, defeat',
			 'the devil': 'evil fatality, weakness, pettiness, blindness',
			 'the emperor': 'benevolence, compassion, credit; also confusion to enemies, obstruction, immaturity',
			 'the empress': 'light, truth, the unravelling of involved matters, public rejoicings; according to another reading, vacillation',
			 'the fool': 'negligence, absence, distribution, carelessness, apathy, nullity, vanity',
			 'the hanged man': 'selfishness, the crowd, body politic',
			 'the hermit': 'concealment, disguise, policy, fear, unreasoned caution',
			 'the hierophant': 'society, good understanding, concord, overkindness, weakness',
			 'the high priestess': 'passion, moral or physical ardour, conceit, surface knowledge',
			 'the lovers': 'failure, foolish designs. another account speaks of marriage frustrated and contrarieties of all kinds',
			 'the magician': 'physician, magus, mental disease, disgrace, disquiet',
			 'the moon': 'fluctuation, slight deceptions, trifling mistakes',
			 'the star': 'arrogance, haughtiness, impotence',
			 'the sun': 'happiness, content, joy (in a lesser degree)',
			 'the tower': 'ruin, disruption, loss in a lesser degree; oppression, imprisonment, tyranny',
			 'the wheel of fortune': 'increase, abundance, superfluity',
			 'the world': 'inertia, fixity, stagnation, permanence',
			 'three of cups': 'expedition of business, quickness, celerity, vigilance',
			 'three of pentacles': 'children, sons, daughters, youths, commencement',
			 'three of swords': 'error, confusion, misrule, disorder',
			 'three of wands': 'hope, desire, attempt, wish',
			 'two of cups': 'crossed desires, obstacles, opposition, hindrance',
			 'two of pentacles': 'letter, missive, epistle, message.',
			 'two of swords': 'false friends, treachery, lies',
			 'two of wands': 'surprise, astonishment, event, extraordinary occurrence'}



def get_card():
	card = raw_input('card name: ').lower()
	is_inverted = raw_input('is the card upside-down? enter y or n: ').lower()
	if is_inverted == 'y':
		meaning = INVERTED[card]
		return meaning
	else:
		meaning = CARDS[card]
		return meaning

def over_again():
	again = raw_input('would you like to look up another card? enter y or n: ').lower()
	if again == 'n':
		return False
	if again != 'y' or 'n':
		print 'please enter y or n'
		play_again()

if __name__ == '__main__':
	while True:
		try:
			print get_card()
			again = over_again()
			if again == False:
				break
		except KeyError:
			print 'sorry, that card does not exist, or maybe you spelled it wrong?'
			again = over_again()
			if again == False:
				break
