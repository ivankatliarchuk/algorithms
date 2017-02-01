def binary_search(list, item):
    # low and high keep track of which part of the list you'll search in
    low = 0
    high = len(list) - 1
    # while you haven't narrowed it down to one element...
    while low <= high:
        # check the middle lement
        mid = (low + high) // 2
        guess = list[mid]
        # found the item
        if guess == item:
            return mid
        # the quess was too high
        if guess > item:
            high = mid - 1
        # the quess was too low
        else:
            low = mid + 1
    return None

my_list = [1, 2, 3, 8, 23]

print(binary_search(my_list, 8))
print(binary_search(my_list, -1))
