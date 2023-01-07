def merge(arr, left, right):

    size_l = len(left)
    size_r = len(right)

    l_idx = r_idx = arr_idx = 0
    while l_idx < size_l and r_idx < size_r:
        if left[l_idx] < right[r_idx]:
            arr[arr_idx] = left[l_idx]
            l_idx += 1
        else:
            arr[arr_idx] = right[r_idx]
            r_idx += 1

        arr_idx += 1

    while l_idx < size_l:
        arr[arr_idx] = left[l_idx]
        l_idx += 1
        arr_idx += 1

    while r_idx < size_r:
        arr[arr_idx] = right[r_idx]
        r_idx += 1
        arr_idx += 1

    return arr


def sort(arr):

    size = len(arr)
    if size < 2:
        return arr

    mid = int(size/2)
    left = sort(arr[:mid])  # recursive method is used to obtain the smallest array for both left and right side
    right = sort(arr[mid:])

    return merge(arr, left, right)


sample_array = [2, 8, 4, 5, 3]
print(sort(sample_array))

