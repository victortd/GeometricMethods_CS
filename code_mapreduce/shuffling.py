import random
import numpy as np


#path of the job 1 input file
folder ='/home/louis/Documents/Data_science/GMDA/'
input_data='part-00000' 

with open(folder+input_data, 'r') as f:
	# we read each line from the input file 
    file_lines = [''.join([x]) for x in f.readlines()]

#we choose randomly n sample from input file
file_lines=random.sample(file_lines,len(file_lines))


with open(folder+"part_3D_"+str(index), 'w') as f:
    f.writelines(file_lines) 




