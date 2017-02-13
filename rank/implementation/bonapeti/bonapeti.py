def result(shared, notShared, bill):
    fullPrice = sum(shared)
    if fullPrice / 2 == bill:
        print('Bon Appetit')
    else:
        print(int(bill - fullPrice/2))


if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    B = int(input().strip())
    notShared = numbers.pop(K)
    result(numbers, notShared, B)
