import datetime
import os.path
import argparse
from collections import defaultdict

# use a database eventually
ENTRIES = []

def _get_lines():
	while True:
		line = raw_input('> ')
		if line == '\n':
			break
		yield line

def create(title):
	'''creates a journal file in the current directory'''
	with open(title, 'w') as f:
		time = str(datetime.datetime.now())
		f.write(time + '\n')
		lines = _get_lines()
		f.write(lines)
		ENTRIES.append(time)

def new_entry(title):
	'''opens journal.txt for writing, adds a date, time'''
	with open(title, 'a') as f:
		time = str(datetime.datetime.now())
		f.write(time + '\n')
		lines = _get_lines()
		f.write(lines)
		ENTRIES.append(time)

def read_last_note():
	'''allows you to read last note 
	todo: index notes by date? number?'''
	title = ENTRIES[-1]
	with open(title, 'r') as f:
		return f.read()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('title', type=str)
	parser.add_argument('-r', '--read', action='store_true')
	args = parser.parse_args()
	if args.read:
		print read_last_note()
	elif os.path.exists(args.title):
		new_entry(args.title)
	else:
		create('journal.txt')