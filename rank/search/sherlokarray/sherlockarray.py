def analytics(data):
    totalSum = sum(data)
    leftSum = 0
    index = 0
    length = len(data)
    if length == 1:
        return 'YES'
    while index < length - 1:
        val = data[index]
        excl = data[index + 1]
        leftSum += val
        rightSum = totalSum - leftSum - excl
        # print("index {}. left {}. ex {}. right {}".format(index, leftSum, excl, rightSum))
        if leftSum == rightSum:
            return 'YES'
        index += 1
    return 'NO'


if __name__ == '__main__':
    N = int(input().strip())
    for test in range(N):
        int(input().strip())
        data = list(map(int, input().strip().split(' ')))
        print(analytics(data))
