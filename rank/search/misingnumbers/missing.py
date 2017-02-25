from collections import Counter

def analytics():
    pass


if __name__ == '__main__':
    int(input().strip())
    first = Counter(list(map(int, input().strip().split(' '))))
    int(input().strip())
    second = Counter(list(map(int, input().strip().split(' '))))
    # print(first)
    first.subtract(second)
    # print(first)
    # print(second)
    data = []
    for n in first.keys():
        if (first.get(n) < 0):
            data.append(n)
    data.sort()
    for num in data:
        print(num, end=' ')

