data = {}


def sumPairs(K, numbers):
    counter = 0
    for num in numbers:
        if data.get(num) is None:
            data[num] = 1
        else:
            data[num] += 1
    keys = list(data.keys())
    length = len(keys)
    for key in range(length):
        value = keys[key]
        for k in range(key, length):
            if (value + keys[k]) % 3 == 0:
                counter = counter + (data.get(value) + data.get(keys[k])) / 2
            elif (value + keys[k]) % 3 == 0:
                counter = counter + (data.get(value) + data.get(keys[k])) / 2
    print(int(counter))


if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    sumPairs(K, numbers)
