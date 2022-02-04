def flipMerge(subarray,thearray):
    length = len(subarray)
    mer = thearray[length:]
    subarray = subarray[::-1]
    subarray += mer
    return subarray
print(flipMerge([1,3,5,6,7],[1,3,5,6,7,3,6,8,2]))
# def flipMerge(subarray,thearray):
#     length = len(subarray)
#     mer = thearray[length:]
#     subarray = subarray[::-1]
#     subarray.extend(mer)
#     print(subarray)
#     return subarray
    
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        output = []
        count = len(arr)-1
        print("here")
        index = len(arr) - 1
        while index > 0:
            
            if sorted(arr) == arr or count == 0:
                print("final")
                break
           
            if arr[0] == max(arr[:count + 1]):
                k = len(arr[:count])
                sub = arr[:k + 1]
                arr = flipMerge(sub,arr)
                # print(arr,"big flip")
                arr = arr[:k + 1:-1]
                print(k,"ind")
                output.append(k+1)
                count -= 1
            else:
                maxval = max(arr[:count])
                # print(arr[:],"find max") #################not functional
                k = arr[:count].index(maxval)
                sub = arr[:k]
                # print(sub,"here",k,"ind")
                arr = flipMerge(sub,arr)
                output.append(k+1)
            print(count,"count")
            index -= 1
        return output