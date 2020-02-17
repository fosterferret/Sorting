# STRETCH: implement Linear Search
def linear_search(arr, target):

    # TO-DO: add missing code
    i = 0
    while i < len(arr):
        if arr[i] == target:
            return i
        else:
            i += 1
    return -1   # not found

# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1
    while low <= high:
        middle = low + (high - low) // 2
        curr = arr[middle]
        if curr == target:
            return arr.index(curr)
        elif target < curr:
            high = middle - 1
        else:
            low = middle + 1
    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):
    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
    middle = low + (high - low) // 2
    curr = arr[middle]
    if curr == target:
        return arr.index(curr)
    elif target < curr:
        return binary_search_recursive(arr, target, low, middle - 1)
    else:
        return binary_search_recursive(arr, target, middle + 1, high)
