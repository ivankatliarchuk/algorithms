def analytics(clouds, K):
    index = 0
    length = len(clouds)
    e = 100
    while index < length:
        if (index + K) < length:
            val = clouds[index + K]
            if val == 1:
                e -= 3
            else:
                e -= 1
            index += K
        else:
            if clouds[0] == 1:
                e -= 3
            else:
                e -= 1
            break
    return e

if __name__ == '__main__':
    N, K =  N = (map(int, input().strip().split(' ')))
    data = [int(source) for source in input().strip().split(' ')]
    print(analytics(data, K))