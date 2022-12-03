with open('input.txt') as f:
  lines = f.read().split('\n')
sum=0
for line in lines:
    common = ''.join(set(line[:int(len(line)/2)]).intersection(line[int(len(line)/2):]))
    if common.isupper(): sum+=ord(common)-65+27
    else: sum+=ord(common)-96
print(sum)