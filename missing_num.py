# A function that finds the missing number in a given sequence of n numbers

def find_miss(arr):
    real_len = len(arr) + 1
    
    #store the real mumbers in an array
    real_arr = []
    i = 1
    while i <= real_len:
        real_arr.append(i)
        i += 1

    #find the missing number
    for num in real_arr:
        if num in arr:
            continue
        else:
            return num


#test our function  if it is working well
arr1 = [1,2,3,5]
nums = find_miss(arr1)
print(nums)    #it will return 4