
#path of the job 1 input file
folder ='/home/louis/Documents/Data_science/GMDA/'
input_data='output_1'

fin = open(folder+input_data)
fout = open('rmsd.txt', 'w')
print('data processing...')
lines = fin.readlines()
for line in lines:
    fout.write(line.split(",")[1])
fout.close()
fin.close()
