array = [1,2,3,4,5,7]
array1 = [1,6,8,10,2,3,4,5,7]


## Brutal Force Approach
def find_missing_number(arr):
    n = len(arr)
    for i in arr:
        if i+1 not in arr:
            return i+1

find_missing_number(array1)
        

## Optimized Approach
def find_missing_number_opt(arr):
    n = len(arr)
    total = (n+1)*(n+2)//2
    sum_arr = sum(arr)
    return total - sum_arr

print(find_missing_number_opt(array1))