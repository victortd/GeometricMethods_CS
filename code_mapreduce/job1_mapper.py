#!/usr/bin/env python
#job 1

#mapper_1
import os
import sys

value=[0,0]
for line in sys.stdin:
	"""
	the input line is "key x y z"
	the output is (key, "x y z")
	"""
	#we get the key
	value[0] = line.split(' ')[0]

	#we get the three coordinates
	value[1] = line[line.find(' '):-1]

	#we print the output
	print '{},{}'.format(value[0],value[1])

