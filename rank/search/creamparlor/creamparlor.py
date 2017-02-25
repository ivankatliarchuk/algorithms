def analytics(M, data):
    left = 0
    length = len(data)
    while left < length - 1:
        right = length - 1
        lValue = data[left]
        while right > left:
            rValue = data[right]
            if lValue + rValue == M:
                return (left + 1, right + 1)
            right -= 1
        left += 1
    return (-1, -1)


if __name__ == '__main__':
    T = int(input().strip())
    for test in range(T):
        M = int(input().strip())
        N = int(input().strip())
        data = list(map(int, input().strip().split(' ')))
        result = analytics(M, data)
        print("{} {}".format(result[0], result[1]))
