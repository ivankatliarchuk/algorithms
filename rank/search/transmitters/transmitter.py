def analytics(distance, data):
    transmitter = 0
    index = 0
    length = len(data)
    maxD = 0
    while index < length:
        value = data[index]
        if maxD == 0:
            if index < length - 1:
                valN = data[index + 1]
                if (valN <= (value + distance)):
                    maxD = value + (distance * 2)
                else:
                    maxD = value + distance
            transmitter += 1
        elif maxD >= value:
            # same transmitter
            pass
        elif maxD < value:
            if index < length - 1:
                valN = data[index + 1]
                if (valN <= (value + distance)):
                    maxD = value + (distance * 2)
                else:
                    maxD = value + distance
            transmitter += 1
        index += 1
    return transmitter


if __name__ == '__main__':
    N, K = list(map(int, input().strip().split(' ')))
    data = list(map(int, input().strip().split(' ')))
    data.sort()
    print(analytics(K, data))
