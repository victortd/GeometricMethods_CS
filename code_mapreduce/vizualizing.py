
import random
import numpy as np
import argparse
import matplotlib.pyplot as plt

#path of the job 1 input file
folder ='/home/louis/Documents/Data_science/GMDA/'
input_data='output_1'
cluster_data = 'ToMATo_code/ToMATo/clusters.txt'
dihedral_data ='dihedral.txt'

print('loading data...')

#we select only key from input file
with open(folder+input_data, 'r') as f:
	# we read each line from the input file 
    file_lines = [''.join([x.split(",")[0]]) for x in f.readlines()]

# we load cluster file as np array
clusters=np.loadtxt(cluster_data)
m=clusters.shape[0]

#we load 2d projection of adaline
dihedral=np.loadtxt(dihedral_data)


vizualize_data=np.zeros((m,3))
#for each line we add [x, y, cluster]
for line in range(m):
	vizualize_data[line,0]=dihedral[int(file_lines[line][:-2]),0]
	vizualize_data[line,1]=dihedral[int(file_lines[line][:-2]),1]
	try :
		vizualize_data[line,2]=int(clusters[line])
	except:
		vizualize_data[line,2]=0
del clusters
del dihedral
del file_lines

#color is associated to clusters
c=vizualize_data[:,2]

print('plotting clusters...')
#we plot the figure
plt.scatter(vizualize_data[:,0],vizualize_data[:,1],c=c,s=1)
plt.title('5 classes of metastable conformations')
plt.xlabel('phi')
plt.ylabel('psi')
plt.show()
