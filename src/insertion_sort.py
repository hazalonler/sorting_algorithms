def sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        print(key)
        arr[j + 1] = key  # at the end of every step, key must be transmitted to where is last transmitted element
    return arr


print(sort([12, 11, 13, 5, 6]))


# Another solution for insertion sort without using key.
def insert_sort(arr):
    size = len(arr)
    for i in range(0, size - 1):
        j = i
        while j >= 0 and arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += -1
    return arr


print(insert_sort([12, 11, 13, 5, 6]))