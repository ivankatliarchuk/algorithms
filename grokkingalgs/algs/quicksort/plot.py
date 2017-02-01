def sum(arr):
    total = 0
    for i in arr:
        total += i
    return total


print(sum([12, 33, 4, 12, 89]))


def recSum(arr, total):
    if len(arr) > 0:
        return recSum(arr, total + arr.pop(0))
    else:
        return total

print(recSum([12, 33, 4, 12, 89], 0))

def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

def fromList(list):
    return list[1:]

print(fromList([12, 33, 4, 12, 89]))
