#! /usr/bin/env python 
from __future__ import print_function, division

import collections
import data
import inspect
import random
import sys
import time
import re

if sys.version_info < (3, ):
	input = raw_input

MEMORY = collections.deque(maxlen = 10)


def doc_quiz(deck):
	list_of_names = list(data.DATA[deck])
	while True:
		name = random.choice(list_of_names)
		if name in MEMORY:
			continue
		MEMORY.append(name)
		try:
			if deck in data.DATA:
				doc = data.DATA[deck][name]

			if doc is None:
				print('No flashcards for {0}'.format(name))
				continue

			print('(Ctrl-C to quit)\n\n')
        	
			inp = input(doc + '\n\n> ')	

		except KeyboardInterrupt:
			return

		except Exception as err:
			print(err)
			raise
			
		time.sleep(0.3)
		correct, answer = check_answer(deck, inp, name)
		if correct:
			print('Correct!\n')
			print(answer)
		else:
			print('INCORRECT\n')
			print(answer)
		time.sleep(0.5)

def check_answer(deck, inp, name):
	if deck == 'datatypes':
		answer = name.split('.').pop()
	else:
		answer = name
	return (inp == answer, answer)


def main():
	try:
		while True:
			inp = input('\nWhat would you like to study? \n> ')

			if inp.lower() not in data.DATA:
				print('I\'m afraid I can not do that, Dave')
			else:
				doc_quiz(inp.lower())
	except(KeyboardInterrupt, EOFError):
		quit(0)



if __name__ == '__main__':
	main()