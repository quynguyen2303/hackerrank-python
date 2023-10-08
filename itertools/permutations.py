from itertools import permutations
string, k = input().split(" ")

# pers = sorted(list(permutations(string, int(k))))
# print(pers)

for p in sorted(list(permutations(string, int(k)))):
    print("".join(p))

