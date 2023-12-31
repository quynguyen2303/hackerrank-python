'''
itertools.product()

This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
'''
from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Print out the cartesian product of A and B
print(*product(A, B))