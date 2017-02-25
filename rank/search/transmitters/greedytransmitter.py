transmitters = {}


def analytics(d, data):
    transmitter = 0
    left = -1
    right = -1
    index = 0
    length = len(data)
    #
    distance = data[0]
    if index == 0:
        transmitter += 1
        left = distance + d
        transmitters[transmitter] = [distance]
        index = 1
    #
    while index < length:
        distance = data[index]
        if left > 0 and right < 0:
            if distance < left:
                # covered by transmitter
                houses = transmitters.get(transmitter)
                if houses is not None:
                    houses.append(distance)
            elif distance == left:
                # will bi covered by same transmitter
                left = -1
                right = distance + d
                houses = transmitters.get(transmitter)
                if houses is not None:
                    houses.append(distance)
            elif distance > left:
                # get back to previous and update distance
                left = -1
                distance = data[index - 1]
                right = distance + d

                if right >= data[index]:
                    houses = transmitters.get(transmitter)
                    if houses is not None:
                        houses.append(distance)
                else:
                    right = -1
                    left = data[index] + d
                    transmitter += 1
                    transmitters[transmitter] = [data[index]]
        elif right > 0 and left < 0:
            if distance < right:
                houses = transmitters.get(transmitter)
                if houses is not None:
                    houses.append(distance)
            elif distance == right:
                right = -1
                houses = transmitters.get(transmitter)
                if houses is not None:
                    houses.append(distance)
                if (index + 1) < length:
                    left = data[index + 1] + d
                    transmitter += 1
                    transmitters[transmitter] = []
            elif distance > right:
                # get back to previous index and update distance
                right = -1
                if (index + 1) <= length:
                    left = distance + d
                    transmitter += 1
                    transmitters[transmitter] = []
                    index -= 1
        index += 1
    printer(transmitters, d)
    return transmitter


def printer(structure, d):
    for key, value in structure.items():
        difference = max(value) - min(value)
        if d * 2 - difference <= 0:
            print("{0} min{1}, max{2}".format(difference, min(value), max(value)))


if __name__ == '__main__':
    N, K = list(map(int, input().strip().split(' ')))
    data = list(map(int, input().strip().split(' ')))
    duplicates = set(data)
    data = list(duplicates)
    data.sort()
    print(analytics(K, data))

'''
3 2
7 9 11
'''
