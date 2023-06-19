'''Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
'''
def print_formatted(number):
    # your code goes here
    pad = len("{:b}".format(number))

    for i in range(1, number + 1):
        # print("%5d %5o %5X %5b" % (i,i,i,i))
        # print(pad)
        print("{0:>{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w=pad))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)