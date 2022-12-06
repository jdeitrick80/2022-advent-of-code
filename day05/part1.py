with open('input.txt') as f:
  start,moves = tuple(map(lambda l: l.split('\n'), f.read().split('\n\n')))
stacks = {}
for i in range(len(start)-2,-1,-1):
    for j in range(1,len(start[i]),4):
      n=int((j+3)/4)
      if(start[i][j]!=" "): 
        if n in stacks:
          stacks[n]+=start[i][j]
        else:
          stacks[n]=start[i][j]
for m in moves:
  t=m.split(" ")
  for x in range(int(t[1])):
    stacks[int(t[5])]+=stacks[int(t[3])][-1]
    stacks[int(t[3])]=stacks[int(t[3])][:-1]
top=""
for i in range(1,len(stacks)+1,1):
  top+=stacks[i][-1]
print(top)