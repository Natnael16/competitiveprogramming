from re import M


tc  = int(input())

for _ in range(tc):
    n = int(input())
    arr = list(map(int , input().split()))
    my_set = set(arr)
    unique = len(my_set)

    res = []
    for i in range(n):
        res.append(max(unique, i+1))
    for num in res: print(num, end=' ')