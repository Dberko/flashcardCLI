#! usr/bin/env python
from __future__ import print_function

import collections  # Container or Sized
import inspect  # getdoc
import keyword
import numbers  # Number
import pkgutil
import sys

# Import back ported `pydoc_data.topics` for older versions
if sys.version_info < (2, 7):
    import topics
else:
    import pydoc_data.topics as topics


if not isinstance(__builtins__, dict):
    __builtins__ = vars(__builtins__)

DATA = {}

def check_answer(quiz_type, inp, name):
	if quiz_type == 'datatypes':
		answer = name.split('.').pop()
	else:
		answer = name
	return (inp == answer, answer)

def main():
    import pprint
    pprint.pprint(DATA['keywords'])


if __name__ == '__main__':
    main()