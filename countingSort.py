
def countingSort(arr):
        n = max(arr) + 2
        counterArray = [0]*n
        for i in arr:
            counterArray[i] = counterArray[i] + 1
        sortedList = []
        j = 0
        while j < 100:
            if counterArray[j] != 0:
                sortedList.append(j)
                counterArray[j] -= 1
                continue
            if len(sortedList)==len(arr):
                break
            j += 1
        return sortedList