with open('input.txt') as f: print(sorted(list(map(lambda elf: sum(list(map(int,elf.split('\n')))), f.read().split('\n\n'))),reverse=True)[0])