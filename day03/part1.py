def common(s): return ''.join(set(s[:int(len(s)/2)]).intersection(s[int(len(s)/2):]))
def val(c): return ord(c)-38 if c.isupper() else ord(c)-96
with open('input.txt') as f: print(sum(map(lambda l: val(common(l)), f.read().split('\n'))))