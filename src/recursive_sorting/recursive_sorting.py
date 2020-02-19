# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(left, right):
    merged_arr = []
    # TO-DO
    indexLeft = 0
    indexRight = 0
    while indexLeft < len(left) and indexRight < len(right):
        if left[indexLeft] < right[indexRight]:
            merged_arr.append(left[indexLeft])
            indexLeft += 1
        else:
            merged_arr.append(right[indexRight])
            indexRight += 1
    merged_arr = merged_arr + left[indexLeft:] + right[indexRight:]
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    size = len(arr)
    if size < 2:
        return arr
    mid = size // 2
    left = arr[0:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))


print(merge_sort([5, 3, 7, 8, 2, 10, 12, 3, 19]))
# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO
    second_start = mid + 1
    while (start <= mid and second_start <= end):
        if (arr[second_start] >= arr[start]):
            start += 1
        else:
            idx, value = second_start, arr[second_start]
            while (idx != start):
                arr[idx] = arr[idx - 1]
                idx -= 1
            arr[start] = value
            second_start += 1; start += 1; mid += 1
    return arr

    [4, 5, 3, 6, 7]


def merge_sort_in_place(arr, l, r):
    # TO-DO
    if (l < r):
        m = l + (r - l) // 2
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
        merge_in_place(arr, l, m, r)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
