def doit(input, n):
    for x in range(len(input)):
        for y in range(len(input[x+1:])):
            for z in range(len(input[y+1:])):
                if input[x] + input[y] + input[z] == n:
                    return input[x] * input[y] * input[z]


if __name__ == '__main__':
    with open('day1.txt') as infile:
        numbers = [int(n) for n in infile.readlines()]

    print(doit(numbers, 2020))
