import re
def checkOverlap(i,j,x,y):
    return int((i>=x and j<=y) or (x>=i and y<=j))
with open('input.txt') as f: print(sum(map(lambda line: checkOverlap(*tuple(map(int,re.split(r"[,-]",line)))),f.read().split('\n'))))