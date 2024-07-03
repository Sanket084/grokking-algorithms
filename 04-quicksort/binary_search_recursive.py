def binarySearch(list, low, high, item):

    if low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        elif guess > item:
            return binarySearch(list, low, mid - 1, item)
        else:
            return binarySearch(list, mid + 1, high, item)
    else:
        return None

my_list = [0, 2, 4, 5]  # Sorted list

print(binarySearch(my_list, 0, len(my_list) - 1, 4))
print(binarySearch(my_list, 0, len(my_list) - 1, -1))
