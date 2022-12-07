with open('input.txt') as f:
  lines = f.read().split('\n')
pwd = []
directories = {}
for line in lines:
    line = line.split(' ')
    if(line[0]=='$'):
        if(line[1]=='cd'):
            if(line[2]=='..'): pwd = pwd[:-1]
            else: pwd.append(line[2])
    else:
        try:
            size = int(line[0])
        except:
            size=0
        for i in range(len(pwd)):
            p=''
            if(i==0): p = '/'.join(pwd)
            else: p = '/'.join(pwd[:-i])
            if p in directories: directories[p]+=size
            else: directories[p]=size
total=0
for k in directories:
    if(directories[k]<=100000): total+=directories[k]
print(total)