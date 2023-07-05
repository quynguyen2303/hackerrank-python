'''
Input Format

The first line contains , the number of testcases.
Each testcase contains  lines, representing time  and time .

Constraints

Input contains only valid timestamps
.
Output Format

Print the absolute difference  in seconds.
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from datetime import datetime
for _ in range(int(input())):
    t1 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    print(int(abs((t1-t2).total_seconds())))