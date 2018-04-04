#!/usr/bin/env python
#job 1

#reducer_1
import sys

node_link={}

for line in sys.stdin:

	"""
		the input is (key, "x y z").

		for each line we compute the conformation in the same line: 

		the the output is (key , [x1 y1 z1, x2 y2 z2, ..., x10 y10 z10])
	"""

	key, value =line.split(',')
	
	if key in node_link.keys():
		# we add the coordinates to the associated confomartion
		node_link[key].append(value)

		if len(node_link[key])==10:
			#if we have ten atoms, we compute the conformation
			print '{},{}'.format(key,node_link[key])
			#and we remove the associated value in the dictionary
			del node_link[key]
	else:
		# we add the coordinates to the associated confomartion
		node_link[key]=[value]
