def quicksort(arr:list,l:int,r:int) -> list: 
    '''This function takes one list arr and two intigers l and r as arguement and apply quicksort algorithm on the list arr[l:r] '''
    if r-l<=1: #if arr[l:r] has 2 or less elements.
        return arr
    pivot,lower,upper = arr[l],l+1,l+1
    for i in range(l+1,r):
        if arr[i]>pivot: 
            upper +=1 #shifts upper pointer to next element
        else:
            arr[i],arr[lower] = arr[lower],arr[i] #swaps current (i-th) element with last lower element
            upper,lower= upper+1,lower+1 #shifts both pointers to next element respectively.
    arr[l],arr[lower-1] = arr[lower-1],arr[l]
    lower -= 1
    quicksort(arr,l,lower)
    quicksort(arr,lower+1,upper)
    return arr
print(quicksort([2,4,5,1,3,6],0,5))