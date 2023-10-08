def solve(full_name):
    return ' '.join([name.capitalize() for name in full_name.split(' ')])

if __name__ == '__main__':
    full_name = input()
    capitalized_name = solve(full_name)
    print(capitalized_name)