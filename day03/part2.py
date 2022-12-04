import re
def common(s): return ''.join(set(''.join(set(s[0]).intersection(s[1]))).intersection(s[2])) 
def val(c): return ord(c)-38 if c.isupper() else ord(c)-96
with open('input.txt') as f: print(sum(map(lambda k: val(common(k)), map(lambda l: l.split('\n'),re.findall('((?:[^\n]+\n?){1,3})', f.read())))))