from itertools import groupby

string = input()
groups = []
uniquekeys = []
for k, g in groupby(string):
    groups.append(list(g))
    uniquekeys.append(k)

for i in range(len(groups)):
    print((len(groups[i]), int(uniquekeys[i])), end=' ')

