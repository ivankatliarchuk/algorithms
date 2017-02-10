#  +1
#  +2
#  +5
# TODO optimise.we can remove equal values
# TODO optimise it
def calcSteps(data):
    # find min and max
    diff = None
    count = 0
    structure = data
    lastElement = len(data) - 1
    while diff is not 0:
        st = sorted(structure)
        minVal = st[0]
        maxVal = st[lastElement]
        diff = maxVal - minVal
        if diff == 0:
            return count
        elif diff >= 5:
            structure = list(map(lambda n: n + 5, st))
        elif diff >= 2:
            structure = list(map(lambda n: n + 2, st))
        elif diff < 2:
            structure = list(map(lambda n: n + 1, st))
        structure[lastElement] = maxVal
        # print(structure)
        count += 1

def readLineOutputSteps(T):
    for n in range(T):
        int(input().strip())
        chocolates = list(map(int, input().strip().split(' ')))
        print(calcSteps(chocolates))


def readSteps():
    T = int(input().strip())
    readLineOutputSteps(T)

if __name__ == '__main__':
    readSteps()
