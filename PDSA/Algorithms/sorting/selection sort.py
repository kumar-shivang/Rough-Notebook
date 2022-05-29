def selection_sort(L: list):
    n = len(L)
    if n<1:
        return L
    for i in range(n-1):
        mini = i
        for j in range(i+1, n):
            if L[j] < L[mini]:
                mini = j
        L[i], L[mini] = L[mini], L[i]
    return L


L = [5, 6, 7, 3, 2, 1]
print(selection_sort(L))
