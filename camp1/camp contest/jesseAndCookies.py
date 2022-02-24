import heapq
def cookies(k, A):
    so = sorted(A)
    heapq.heapify(A)
    sumA = 0
    if len(A) == 1:
        if A[0] < k:
            return -1
        elif A[0] >= k:
            return 0

    count = 0
    while len(A) > 1 and A[0] <= k:
        num1 = heapq.heappop(A)
        num2 = heapq.heappop(A)
        heapq.heappush(A, num1 + (2 * num2))
        count += 1
    # for i in range(len(A)-1):
    #     sumA += (so[i] + so[i + 1]*2)
    # # print(sumA)
    if A[0] < k:
        return -1
    return count