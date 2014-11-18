from bs4 import BeautifulSoup
from urllib2 import urlopen
import wordfarmer

def scrape_for_nouns():
	input_url = raw_input('enter a website to extract text from: ')
	soup = BeautifulSoup(urlopen(input_url).read())
	url_text = soup.get_text()
	url_pos_dict = wordfarmer.make_pos_dict(url_text)
	url_nouns = wordfarmer.get_nouns(url_pos_dict)
	return url_nouns

if __name__ == '__main__':
	print scrape_for_nouns() #need to deal with unicode errors
	