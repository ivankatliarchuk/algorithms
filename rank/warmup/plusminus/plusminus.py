N = int(input().strip())
data = list(map(int, input().strip().split(' ')))

N = N * 1.00
counter = {'pos': 0, 'neg': 0, "zero": 0}

for num in data:
    if num == 0:
        counter['zero'] += 1
    elif num > 0:
        counter['pos'] += 1
    elif num < 0:
        counter['neg'] += 1


def printLines():
    num = counter['pos'] / N
    print("{0:.6f}".format(num))
    num = counter['neg'] / N
    print("{0:.6f}".format(num))
    num = counter['zero'] / N
    print("{0:.6f}".format(num))

printLines()
