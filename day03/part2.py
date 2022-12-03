with open('input.txt') as f:
  lines = f.read().split('\n')
sum=0
for i in range(0,len(lines),3):
    common = ''.join(set(''.join(set(lines[i]).intersection(lines[i+1]))).intersection(lines[i+2]))
    if common.isupper(): sum+=ord(common)-65+27
    else: sum+=ord(common)-96
print(sum)