def partition(arr, start, end):
    pivot = arr[end]
    part_index = start

    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[part_index] = arr[part_index], arr[i]
            part_index += 1

    arr[part_index], arr[end] = arr[end], arr[part_index]
    return part_index


def sort(arr, start, end):

    if start < end:
        pi_index = partition(arr, start, end)
        sort(arr, start, pi_index - 1)
        sort(arr, pi_index, end)
    return arr


sample_arr = [4, 5, 3, 7, 2]
print(sort(sample_arr, 0, 4))

