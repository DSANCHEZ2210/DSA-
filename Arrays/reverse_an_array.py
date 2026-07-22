array = [1,2,3,4,5,6,7]

## Brutal Force Approach

def revers_arr(arr):
    n = len(arr)
    new_arr = []
    for i in range(n-1,-1,-1):
        new_arr.append(arr[i])
    return new_arr

print(revers_arr(array))

## Optimized Approach

def reverse_array_opt(arr):
    n = len(arr)
    new_arr = [0]*n
    n_1 = n//2
    if n % 2 != 0:
        new_arr[n_1] = arr[n_1]
    for i in range(n//2):
        new_arr[i] = arr[n-1-i]
        new_arr[n-1-i] = arr[i]
            
    return new_arr

print(reverse_array_opt(array))