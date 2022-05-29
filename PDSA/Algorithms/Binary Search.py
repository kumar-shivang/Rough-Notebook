def binary_search(v,L):
    print(L)
    if L==[]:
        return False
    mid_index = len(L)//2
    if L[mid_index]==v:
        return True
    else:
        if v<L[mid_index]:
            return binary_search(v,L[:mid_index])
        else:
            return binary_search(v,L[mid_index+1:])
L = [2*i for i in range(1000)]
print(binary_search(int(input("Enter the value to find - ")),L))