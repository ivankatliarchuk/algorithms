T = int(input().strip())
socks = list(map(int, input().strip().split(' ')))

pairs = {}

def findPairs(data):
    for d in data:
        if pairs.get(d) is not None:
            pairs[d] += 1
        else:
            pairs[d] = 1
    count = 0
    for n in pairs:
        count += int(pairs[n] / 2)
    return count

print(findPairs(socks))
