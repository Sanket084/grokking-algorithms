# Write a recursive function to count the number of items in a list.

def count(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + count(arr[1:])
    

print (count([2, 3, 5, 6]))