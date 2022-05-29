def quicksort(arr:list,l:int,r:int) ->list:
    if r-l <= 1:
        return arr
    pivot,lower,upper = arr[r],l,l
    for i in range(l,r):
        if arr[i]>pivot:
            upper+=1
        else:
            arr[i],arr[lower]=arr[lower],arr[i]
            upper,lower = upper+1,lower+1
    arr[r],arr[lower] = arr[lower],arr[r]
    upper -=1
    quicksort(arr,l,upper)
    quicksort(arr,upper,r-1)
    return arr

