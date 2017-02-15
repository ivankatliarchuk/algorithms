def analytics(data):
    length = len(data)
    step = 0
    i = 0
    while i < length:
        # print("{} {}".format(i, step))
        if (i+2) <= (length - 1) and data[i+2] != 1:
            jump = 2
        elif (i+1) <= length - 1 and data[i+1] != 1:
            jump = 1
        else:
            break
        i += jump
        step += 1
    return step


if __name__ == '__main__':
    N = int(input().strip())
    clouds = list(map(int, input().strip().split(' ')))
    print(analytics(clouds))
