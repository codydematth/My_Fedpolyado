def sort_diff(arr,val):
    i= 0
    j= 0
    while i <len(arr) and j < len(arr):

        if (arr[j] - arr[i]) == val:
            return "Found"
        else:
            i+=1

    if (arr[j] - arr[i]) != val:
        j+=1
    else:
        return " Not Found"


arr = [1,25,5,6,8,10]
val = 15
print(sort_diff(arr,val))
