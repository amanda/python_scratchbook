import datetime
import os
import os.path
import argparse
import sys

JOURNAL_PATH = os.path.join(os.path.expanduser('~'), 'journal')

def make_directory(path):
	try:
		os.mkdir(path)
	except OSError:
		print 'something went wrong!'

def get_lines():
	text = ''
	print 'write your note, then write \'done\' when done.'
	while True:
		line = raw_input('> ')
		if line == 'done':
			break
		text += '%s \n' % line
	return text

def new_note(path, title):
	with open((os.path.join(path, title)), 'w') as f:
		lines = get_lines()
		time = str(datetime.datetime.now())
		f.write(time + '\n' + lines)

def read_note(path, title):
	with open((os.path.join(path, title)), 'r') as f:
		return f.read()

def edit_note(path, title):
	with open((os.path.join(path, title)), 'a') as f:
		lines = get_lines()
		time = str(datetime.datetime.now())
		f.write('\n' + time + '\n' + lines)

def see_all_notes(path):
	return os.listdir(path)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('title', type=str, nargs='?', help='note title')
	parser.add_argument('-r', '--read', action='store_true')
	parser.add_argument('-e', '--edit', action='store_true')
	parser.add_argument('-v', '--view', action='store_true')
	args = parser.parse_args()
	#note = os.path.join(JOURNAL_PATH, args.title)
	if not os.path.exists(JOURNAL_PATH):
		make_directory(JOURNAL_PATH)
		new_note(JOURNAL_PATH, args.title)
	elif args.read:
		try:
			print read_note(JOURNAL_PATH, args.title)
		except IOError:
			print 'that note does not exist.'
	elif args.edit:
		edit_note(JOURNAL_PATH, args.title)
	elif args.view:
		print see_all_notes(JOURNAL_PATH)
	elif os.path.exists(os.path.join(JOURNAL_PATH, args.title)):
		print 'that note already exists, choose a new title.'
	else:
		new_note(JOURNAL_PATH, args.title)
