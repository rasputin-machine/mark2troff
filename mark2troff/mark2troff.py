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

def _print_header(line):
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
		if line == '':
			print(conversions['\n'])
		elif line[0] == '#':
			_print_header(line)
		else:
			print(line)
	
				


def arg_parser():
	parser = argparse.ArgumentParser(
		description='Easily convert markdown into troff.'
	)

	parser.add_argument('file', type=str)
	return parser


if __name__ == '__main__':
	parser = arg_parser()
	args = vars(parser.parse_args())

	convert(args['file'])

