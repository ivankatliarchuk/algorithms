
distances = {}
prev_index = {}

def analytics(data):
    minimum = -1
    for index, val in enumerate(data):
        if prev_index.get(val) is None:
            prev_index[val] = index
            distances[val] = 0
        else:
            # cal abs distance
            prev = prev_index[val]
            # print("{} {}".format(prev, index))
            distance = abs(prev - index)
            if distance > distances[val]:
                distances[val] = distance
                if distance < minimum or minimum :
                    minimum = distance
            prev_index[val] = index
    # print(distances)
    return minimum

if __name__ == '__main__':
    N = int(input().strip())
    data = [int(source) for source in input().strip().split(' ')]
    print(analytics(data))

