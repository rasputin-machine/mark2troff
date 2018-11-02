#!/usr/bin/env python

import argparse

conversions = {
	'#': {
		1: '.NH',
		2: '.NH 2',
		3: '.NH 3',
		4: '.NH 4',
		5: '.NH 5',
		6: '.NH 6',
	},
	'\n': '.PP',
	
}

def _sect_heading(line):
	line_list = line.split()
	header_level = len(line_list[0])
	header_title = ''.join(line_list[1:])
	print(conversions['#'][header_level])
	print(header_title)

def convert(in_file):
	# grap a list of lines from the file
	with open(in_file, 'r') as f:
		lines = f.readlines()
	lines = [l.strip() for l in lines]
	
	for line in lines:
		_main_parse(line)

def _main_parse(line)
	# first take care of section headers
	if line[0] == '#':
		_sect_heading(line)
	# then we do all the other parsing
	elif line == '':
		print(conversions['\n'])
	else:
		_parse_line(line)
		
def _parse_line(line)
	pass

def arg_parser():
	parser = argparse.ArgumentParser(description='Easily convert markdown into troff.')
	parser.add_argument('file', type=str)
	return parser

def main():
	parser = arg_parser()
	args = vars(parser.parse_args())

	convert(args['file'])

if __name__ == '__main__':
	main()
