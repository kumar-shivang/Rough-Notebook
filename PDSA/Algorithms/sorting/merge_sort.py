def merge(A:list,B:list) -> list:
    """This function takes two sorted lists as arguement and return a merged sorted list."""
    (m,n) = len(A),len(B)
    (arr,i,j,k) = ([],0,0,0)
    while m+n>k: #when len(arr)<len(A)+len(B)
        if i==m: #if i reaches end of the list A
            arr.extend(B[j:])
            k += n-j
        elif j==n: #if j reaches end of list B
            arr.extend(A[i:])
            k += m-j
        elif A[i]<B[j]:
            arr.append(A[i])
            i+=1
            k+=1
        else:
            arr.append(B[j])
            j+=1
            k+=1
    return arr
def mergeSort(arr):
    n = len(arr)
    if n<=1:
        return arr
    L = mergeSort(arr[:len(arr)//2])
    R = mergeSort(arr[len(arr)//2:])
    B = merge(L,R)
    return B
print(mergeSort(list(map(int,input("Enter the list - ").split(" ")))))
    
            