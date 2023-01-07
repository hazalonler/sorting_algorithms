# an optimized version of bubble sorting if there is no swapping in inner loops
def sort(arr):
    for i in range(0, len(arr)):
        j = 0
        swapped = False
        while j < len(arr)-i-1:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            j += 1
        if not swapped:
            break
    return arr


print(sort([5, 1, 4, 2, 8, 1, 3, 11, 7, 54]))


