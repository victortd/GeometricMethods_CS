data='/home/louis/Documents/Data_science/GMDA/dihedral.txt' #aladip_implicit
data_output='/home/louis/Documents/Data_science/GMDA/dihedral_nbr.txt' #aladip_implicit


output = ""
file_name = data


with open(file_name, 'r') as f:
    file_lines = [''.join([str((value+10)//10)+" ",x.strip(),'\n']) for value,x in enumerate(f.readlines())]

with open(data_output, 'w') as f:
    f.writelines(file_lines) 