
def calcKangaroo(x1, v1, x2, v2):
    if x2 > x1 and v2 >= v1:
        print("NO")
    else:
        location = x2 - x1
        speed = v1 - v2
        jumps = int(location / speed)
        if (x1 + v1 * jumps) == (x2 + v2 * jumps):
            print('YES')
        else:
            print('NO')



if __name__ == '__main__':
    x1, v1, x2, v2 = input().strip().split(' ')
    x1, v1, x2, v2 = [int(x1), int(v1), int(x2), float(v2)]
    calcKangaroo(x1, v1, x2, v2)