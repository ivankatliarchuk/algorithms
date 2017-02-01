def findSmallest(arr):
    """
    function to find smallest element in an array
    """
    smallest = arr[0]  # stores the smallest value
    smallest_index = 0  # stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    """
    sorts an array
    """
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([45, 4356, 33, 0, 34, 56]))
