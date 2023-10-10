from collections import OrderedDict

n = int(input())
ordered_dictionary = OrderedDict()
for _ in range(n):
    item, space, price = input().rpartition(' ')
    ordered_dictionary[item] = ordered_dictionary.get(item, 0) + int(price)

for item, price in ordered_dictionary.items():
    print(item, price)
    