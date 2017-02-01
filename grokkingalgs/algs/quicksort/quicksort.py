def quickSort(array):
    if len(array) <= 1: # base case, array already sorted
        return array
    else:
        pivot = array[0] # recursive case
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)




print(quickSort([22, 11, -3, 0, 89]))
