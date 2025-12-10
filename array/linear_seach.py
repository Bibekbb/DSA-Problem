def count_target(arr, target):
    count = 0
    
    for num in arr:
        if num == target:
            count+= 1 
    return count


arr = [1, 2, 3, 2, 4, 2, 5]
target = 2 
print(count_target(arr,target))
    
    