import argparse
import os
import re #need to check if valid titlename eventually

def get_argparser():
	parser = argparse.ArgumentParser()
	parser.add_argument('command', type=str)
	parser.add_argument('title', type=str)	
	return parser

def get_lines():
	while True:
		line = raw_input('>')
		if line == 'stop':
			raise StopIteration
		return line

def create(title=None):
	with open(title, 'w') as f:
		lines = get_lines()
		f.write(lines)
	
def edit(title=None):
	if os.path.exists(title):
		with open(title, 'a') as f:
			lines = get_lines()
			f.write(lines)
	else:
		print 'that file doesn\'t exist!'

def delete(title=None):
	os.delete('%s.txt' % title)

def view(title=None):
	with open(title, 'r') as f:
		print f.readlines()

if __name__ == '__main__':
	commands = {
		'create': create,
		'edit': edit,
		'delete': delete,
		'view': view
		}
	parser = get_argparser()
	args = parser.parse_args()
	commands[args.command](args.title)
