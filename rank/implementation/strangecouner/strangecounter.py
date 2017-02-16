start = 3
def analytics(N):
    prevMax = start
    counter = prevMax
    val = -1
    index = 0
    for num in range(0, N):
        if counter == 0:
            prevMax *= 2
            counter = prevMax
        val = counter
        if (val == 1):
            print("{0} num {1} - {1:b} max {2} bin {2:b}".format(index, num+1, prevMax))
            index += 1
        counter -= 1
    return val

if __name__ == '__main__':
    N = int(input().strip())
    print(analytics(N))