def find_min(arr):
    min=arr[0]
    for i in range (len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min
print(find_min([10,4,8,2,12]))        
