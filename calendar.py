'''
Task

You are given a date. Your task is to find what the day is on that date.

Input Format

A single line of input containing the space separated month, day and year, respectively, in    format.

Constraints

Output Format

Output the correct day in capital letters.
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
m, d, y = map(int, input().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())
