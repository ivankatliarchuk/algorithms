def analytics(data, K):
    index = 0
    length = len(data)
    filtered = set()
    while index < length:
        num = index + 1
        while num < length:
            if (data[index] + data[num]) % K != 0:
                print("{} {}".format(data[index], data[num]))
                filtered.add(data[num])
                filtered.add(data[index])
            num += 1
        index += 1
    print(sorted(data))
    print(sorted(filtered))
    return len(filtered)

if __name__ == '__main__':
    N, K = (map(int, input().split()))
    data = list(map(int, input().split()))
    print(analytics(data, K))