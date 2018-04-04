#!/usr/bin/env python
#job 2

#mapper_1

import os
import sys
import unittest
import argparse
import numpy as np
from IRMSD import Conformations
from IRMSD import align_array
import IRMSD

# the path of IRMSD library
sys.path.insert(0, '/home/louis/Documents/Data_science/GMDA/ToMATo_code/ToMATo/IRMSD-master/python/IRMSD')

parser = argparse.ArgumentParser()
parser.add_argument("prunning", help="number of distance the output file keeps",
                    type=int, default=15000)
parser.add_argument("sample", help="number of sample from the input file",
                    type=int, default=100000)
parser.add_argument("output", help="format of output file 'matrix' or 'dictionnary'", default="matrix")
args = parser.parse_args()


m=args.sample #nbr of input conformation
dim=3 #space dimension
n=10 #nbr of atom for one conformation
k=args.prunning #nbr of distance we keep

#we create a one dimensional array with all data
conformation=[0]*1420738*dim*10
key=[]

li=0
for line in sys.stdin:

	""" the input is (key, '[x1 y1 z1],[x2 y2 z2],...,[x10 y10 z10]')

	here we compute the rmsd distance between each pairwise conformation:
	output:

	([key 1, key 2], rmsd(confo_1, confo_2))
	"""
	
	# we get the input 
	key_value1 = line.split(',')

	
	for atom in range(n):
		
		for coord in range(dim):
			conformation[dim*n*li+n*coord+atom]=float(key_value1[atom+1][3+coord*7:9+coord*7])
			
			#data.append(float(key_value1[atom+1][3+coord*7:9+coord*7]))
	key.append(key_value1[0])	
	li+=1
# we convert data into numpy array
conformation=np.array(conformation)
#we reshape the one dimensional array into 100000 x 3 x 10
conformation=conformation.reshape((len(conformation)/3/n,n,3))

# we create conformation array
confs = align_array(conformation[0:m], 'atom')
# we create conformation object
conf_obj = Conformations(confs, 'atom', 10)

# we create conformation array
confs_part = align_array(conformation[0:k], 'atom')
# we create conformation object
conf_obj_part = Conformations(confs_part, 'atom', 10)

del conformation
del confs
del confs_part


if args.output=="dictionnary":
	#for each conformation
	for i in range(m): #data_frame.shape[0]/n

		rmsd_dic={}
		# we compute the rmsd between conformation i and all other confomations
		rmsds = conf_obj_part.rmsds_to_reference(conf_obj,i)
		# we sort the conformation 
		rmsds_sorted=sorted(rmsds)

		#we keep only the k nearest conformation
		for l in range(k):
			rmsd_dic[l]=rmsds_sorted[l]

		# we print output
		print '{},{}'.format(i,rmsd_dic)

elif args.output=="matrix":

	for i in range(m): 

		
		# we compute the rmsd between conformation i and all other confomations
		rmsds = conf_obj_part.rmsds_to_reference(conf_obj,i)
		rmsds_sorted=sorted(rmsd)
		line=key[i]+","
		for d in range(k):
			line += str(rmsds_sorted[d])+" "
		print '{}'.format(line)

	

