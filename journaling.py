import datetime
import os
import os.path
import argparse
import sys

journal_path = os.path.join(os.path.expanduser('~'), 'journal')

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

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('title', type=str, help='note title')
	parser.add_argument('-r', '--read', action='store_true')
	args = parser.parse_args()
	if args.read:
		print read_note(args.title)
	elif os.path.exists(journal_path):
		new_note(journal_path, args.title)
	else:
		make_directory(journal_path)
		new_note(journal_path, args.title)
