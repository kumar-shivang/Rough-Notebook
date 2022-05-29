T = int(input())
for i in range(T):
    tr = int(input())
    tr_list = list(map(int,input().split(" ")))
    dr = int(input())
    dr_list = list(map(int,input().split(" ")))
    ts = int(input())
    ts_list = list(map(int,input().split(" ")))
    ds = int(input())
    ds_list = list(map(int,input().split(" ")))
    flag = True
    for i in ts_list:
        if i not in tr_list:
            flag = False
            break
    for j in ds_list:
        if j not in dr_list:
            flag = False
            break
    if flag:
        print("yes")
    else: print("no")

    
    
    