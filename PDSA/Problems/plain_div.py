for i in range(int(input())):
    s = set()
    for j in range(int(input())):
        a, b, c = tuple(map(int, input().split(" ")))
        if b != 0:
            slope_intercept = (-a/b, -c/b)
        else:
            slope_intercept = (float('inf'), -c/a)
        s.add(slope_intercept)
    l = list(map(lambda x: x[0], list(s)))
    count = 0
    s2 = set(l)
    for i in s2:
        if l.count(i) > count:
            count = l.count(i)
    print(count)
