'''Task

 is a shoe shop owner. His shop has  number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

Your task is to compute how much money  earned.

Input Format

The first line contains , the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers.
The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.

Constraints





Output Format

Print the amount of money earned by .
'''
from collections import Counter


def main():
    x = int(input())
    shoes = Counter(map(int, input().split()))
    n = int(input())
    total = 0

    for i in range(n):
        size, price = map(int, input().split())
        if shoes[size]:
            total += price
            shoes[size] -= 1

    print(total)