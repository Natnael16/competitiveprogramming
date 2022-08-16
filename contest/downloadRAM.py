tc = int(input())

for _ in range(tc):
    gain_table = {}
    no_software , cur_ram = list(map(int, input().split()))
    required = list(map(int, input().split()))
    to_get= list(map(int, input().split()))
    min_first = []
    for ind , ram in enumerate(to_get):
        min_first.append((required[ind] , ram))

    min_first.sort()
    max_gain = cur_ram
    for possible , perm in min_first:
        if possible <= max_gain:
            max_gain += perm
        else:
            break
    print(max_gain)


