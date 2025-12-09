def find_max(arr):

    maximum = arr[0]

    for num in arr:
        if num > maximum:
            maximum = num
    return maximum  

print(find_max([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))