def GCD(m,n):
    a,b = max((m,n)),min((m,n))
    if a%b == 0:
        return b
    else:
        return GCD(a%b,b)
print(GCD(int(input("Enter 1st Value- ")),int(input("Enter 2nd value- "))))