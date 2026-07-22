array = [1,3,6,32,325,7,85,3,34,-4]

## Brutal Force Approach
def max_min(arr):
    n = len(arr)
    max_num = arr[0]
    min_num = arr[0]
    for i in range(n):
        if arr[i] > max_num:
            max_num = arr[i]
        if arr[i] < min_num:
            min_num = arr[i]
    return max_num, min_num

print(max_min(array))

## Optimized Approach
def find_max_min(arr):
    max=arr[0]
    min=arr[0]
    for i in arr:
        if i>max:
            max=i
        elif i<min:
            min=i
    return max,min

print(find_max_min(array))