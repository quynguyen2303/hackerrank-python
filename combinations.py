from itertools import combinations

string, k = input().split(" ")
k = int(k)

string = "".join(sorted([c for c in string]))

for i in range (1, k+1):
    for c in list(combinations(string, i)):
        print("".join(c))
