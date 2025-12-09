def reverse_array(arr):
    start = 0
    end = len(arr) -  1 
    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        
        start += 1 
        end -= 1 
    return arr 

print(reverse_array([1,2,4,5,6,7,8,9,1,3,5,6,7]))