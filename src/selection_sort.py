def sort(arr):
    for i in range(0, len(arr)-1):
        min_index = i
        j = i+1
        while j < len(arr):
            if arr[j] < arr[min_index]:
                min_index = j
            j += 1
        # swap the minimum data with ith data in every loop
        temp_var = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp_var

        # arr[i], arr[min_index] = arr[min_index], arr[i] is another way to swap the numbers in Python.
    return arr


print(sort([20, 12, 10, 15, 2]))


# An application of selection sort for string arrays
def select_sort(arr):
    n = len(arr)
    for i in range(0, n):
        min_index = i
        j = i+1
        while j < n:
            if len(arr[j]) < len(arr[min_index]):
                min_index = j
            j += 1

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


print(select_sort(['ahmet', 'ali', 'huseyin', 'yasin', 'selami']))
