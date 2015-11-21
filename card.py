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


def main():
	try:
		while True:
			inp = input('\nWhat would you like to study? \n> ')

			if inp.lower() not in data.DATA:
				print('I\'m afraid I can not do that, Dave')
			else:
				quiz(inp.lower())
	except(KeyboardInterrupt, EOFError):
		quit(0)

if __name__ == '__main__':
	main()