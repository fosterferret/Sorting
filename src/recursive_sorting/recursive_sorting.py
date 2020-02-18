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

# [2,4,1,3]
# merge [2,4] [1,3]
# [2] [4]
# [2]

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

    if (arr[mid] <= arr[second_start]):
        return

    while (start <= mid and second_start <= end):

        if (arr[start] <= arr[second_start]):
            start += 1
        else:
            value = arr[second_start]
            index = second_start

            while (index != start):
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            start += 1
            mid += 1
            second_start += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO
    [4,2,3,5]
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
