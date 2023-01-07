def sort(arr):
    max_num = max(arr)
    count_arr = [0]*(max_num+1)

    for num in arr:
        count_arr[num] += 1

    for idx in range(0, max_num):
        count_arr[idx+1] = count_arr[idx] + count_arr[idx+1]

    new_arr = [0]*len(arr)  # counting sort is a non-in-place algorithm because it uses a temporary memory
    for num in arr:
        new_index = count_arr[num] - 1
        count_arr[num] = new_index
        new_arr[new_index] = num

    return new_arr


sample_arr = [1, 4, 1, 2, 7, 5, 2, 3, 6, 4]
print(sort(sample_arr))