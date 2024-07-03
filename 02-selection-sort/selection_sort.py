def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 2, 6, 1, 4]))


# documentation for array.pop:
# example: pop([i])
# Removes the item with the index i from the array and returns it. The optional argument defaults to -1, so that by default the last item is removed and returned.