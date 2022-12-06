with open('input.txt') as f:
    line = f.read()
for i in range(4,len(line)):
    if(len(''.join(set(line[i-4:i])))==4):
        print(i)
        break