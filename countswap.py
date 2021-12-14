def countSwaps(a):
    swaps = 0
    done = 1
    while done != 0:
        done = 0
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                swaps += 1
                done += 1
    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: { a[0] }")
    print(f"Last Element: { a[-1] }")