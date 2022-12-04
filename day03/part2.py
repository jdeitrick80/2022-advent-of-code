import re
def val(c): return ord(c)-38 if c.isupper() else ord(c)-96
with open('input.txt') as f: print(sum(map(lambda k: val(''.join(set(''.join(set(k[0]).intersection(k[1]))).intersection(k[2]))), map(lambda l: l.split('\n'),re.findall('((?:[^\n]+\n?){1,3})', f.read())))))