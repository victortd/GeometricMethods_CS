import sys
from math import sqrt
import unittest
import numpy as np
from IRMSD import Conformations
from IRMSD import align_array
import IRMSD
import time
import argparse
sys.path.insert(0, '/home/louis/Documents/Data_science/GMDA/ToMATo_code/ToMATo/IRMSD-master/python/IRMSD')

folder='/home/louis/Documents/Data_science/GMDA/'
input_data='aladip_implicit.txt' #aladip_implicit

parser = argparse.ArgumentParser()

parser.add_argument("sample", help="number of sample from the input file",
                    type=int, default=5000)
parser.add_argument("kept", help="number of distance we keep",
                    type=int, default=5000)
args = parser.parse_args()


print('loading data ...')
#load data
data_frame=np.loadtxt(folder+input_data)

dim=3 #nbr of dimension
n=10 #nbr of atom for one conformation
#data_frame=np.transpose(data_frame)
m=args.sample # nbr of sample
k=args.kept #nbr of distance we keep

#key
key=np.array([(value+10)//10 for value in range(14207380)])
data_frame=np.c_[key,data_frame]

conformation=data_frame.reshape((data_frame.shape[0]/n,n,dim+1))
del data_frame

#shuffle conformation
conformation=np.take(conformation,np.random.permutation(conformation.shape[0]),axis=0,out=conformation)


#keep only m sample
conformation=conformation[:m]
#keep only k sample in order to keep k distance
conformation_part=conformation[:k]

#create conformation object
confs = align_array(conformation[:,:,1:], 'atom')
conf_obj = Conformations(confs, 'atom', 10)

confs_part = align_array(conformation_part[:,:,1:], 'atom')
conf_obj_part = Conformations(confs, 'atom', 10)

del conformation_part
del confs
del confs_part

fout = open(folder+"output_1", 'w')
for i in range(m): 
	# we compute the rmsd between conformation i and all other confomations
	rmsds = conf_obj_part.rmsds_to_reference(conf_obj,i)
	line=str(conformation[i,0,0])+"," # we add key for each line
	#rmsds_sorted=sorted(rmsds)
	for d in range(k):
		line += str(rmsds[d])+" "
	line+='\n'
	print('computing the '+str(i)+' th  rmsd distance')
	fout.write(line) 

fout.close()





