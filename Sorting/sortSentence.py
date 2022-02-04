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
class Solution:
    def sortSentence(self, s: str) -> str:
        arrayString = s.split()
        indexDict = {}
        for i in arrayString:
            for j in i:
                if j.isdigit():
                    indexDict[j] = i
        sortingNum = indexDict.keys()
        arrayOfNum = []
        for i in sortingNum:
            arrayOfNum.append(int(i)) ### remove this
        sortedNum = countingSort(arrayOfNum)
        stringSorted = ""
        for i in sortedNum:
            stringSorted = stringSorted + indexDict[str(i)] +" "
        stringSorted = stringSorted.rstrip()
        finalSort = ''
        for i in stringSorted:
            if not(str(i).isdigit()):
                print(i)
                finalSort = finalSort + i
        return finalSort    
    print(sortSentence('is2 abebe1 Go5 to4 talking3'))