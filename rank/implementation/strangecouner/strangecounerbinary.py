def analytics(N):
    binStr = "{:b}".format(N)
    lenght = len(binStr)
    if N <= 3:
        maxi = '11'
    else:
        maxi = '10' + '1' * (lenght - 4) + '01'
    counM = '11' + '0' * (lenght - 2)
    prevMin = int(maxi, 2)
    prevMax = int(counM, 2)
    print("min {} max val prv{}".format(prevMin, prevMax))

    if N == prevMin:
        return 1

    if N < prevMin:
        dist = abs(N - prevMin)
        print("less dist {} max {}".format(dist, prevMax))
        return 1 + dist

    if N > prevMin:
        dist = abs(N - prevMin)
        print("more dist {} max {}".format(dist, prevMax))
        return prevMax - (dist - 1)

    return -1


# lets work out for 21 and more
if __name__ == '__main__':
    N = int(input().strip())
    print(analytics(N))
