'''
Input Format

The first line contains integers,  and  separated by a space.
The next  lines contains the words belonging to group .
The next  lines contains the words belonging to group .

Constraints




Output Format

Output  lines.
The  line should contain the -indexed positions of the occurrences of the  word separated by spaces.
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d = defaultdict(list)
n, m = map(int, input().split())
for i in range(n):
    d[input()].append(i+1)
for i in range(m):
    print(*d[input()] or [-1])
    
