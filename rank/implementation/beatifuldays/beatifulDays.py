

def analytics(I, J, K):
    count = 0
    for num in range(I, J + 1):
        # reverse a string [begin:end:step]
        reverse = str(num)[::-1]
        revInt = int(reverse)
        diff = abs(num - revInt)
        if diff % K == 0:
            count += 1
        # print("{} {} {}".format(num, reverse, diff))

    return count

if __name__ == '__main__':
    (I,J,K) = (map(int, input().split()))
    print(analytics(I, J, K))

# {0, 36, 72, 9, 45, 18, 54, 27, 63}
