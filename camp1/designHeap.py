import heapq;
class Solution:
    def buildHeap(self,arr):
        for i in range(len(arr)):
            self.upHeap(arr, i)
        # print(arr)

    def upHeap(self,arr,i):
        back = i
        parent = self.getParent(back)

        while back > 0 and arr[parent] > arr[back]:
            arr[parent], arr[back] = arr[
                back], arr[parent]
            back = parent
            parent = self.getParent(back)

    def downHeap(self, arr, n, i):
        current = i
        left = self.leftChild(arr,i)
        right = self.rightChild(arr,i)

        if (left and left < n and arr[left] < arr[current]):
            current = left

        if (right and right < n and arr[right] < arr[current]):
            current = right

        if (i != current):
            arr[i],arr[current] = arr[current],arr[i]
            self.downHeap(arr, n, current)

    def insert(self,arr, num):
        arr.append(num)
        self.upHeap(arr,len(arr) - 1)
        # print(arr)
    def getMin(self,arr):
        return arr[0]
    def update(self,arr,i,num):
        if i >= len(arr) or i < 0:
            return
        arr[i] = num
        self.heapify(arr,len(arr),i)
    def delete(self,arr,i):
        if i >= len(arr) or i < 0:
            return
        last = arr.pop()
        self.update(arr,i,last)
    def heapify(self,arr,n, i):
        self.upHeap(arr,i)
        self.downHeap(arr,i,n)
        # print(self.a)
    def leftChild(self,arr,index):
        if index * 2  + 1 < len(arr):
            return index * 2  + 1
        else:
            return None
    def getParent(self,index):
        if (index - 1 )// 2 < 0:
            return None
        return (index - 1 )// 2
    def rightChild(self,arr,index):
        if index * 2 + 2 < len(arr):
            return index * 2 + 2
        else:
            return None
    def HeapSort(self, arr, n):
        a = arr
        self.buildHeap(arr)
        for last in range(n-1,-1,-1):
            arr[0], arr[last] = arr[last], arr[0]
            self.downHeap(arr,last,0)



sol = Solution()
b = '932 66 777 426 127 404 63 281 426 317 735 628 543 78 31 811 626 104 389 412 687 296 35 252 441 675 604 770 342 284 917 274 702 46 53 829 450 116 463 229 786 198 857 329 276 888 140 254 992 530 18 31 178 405 284 619 80 240 742 423 876 659 49 931 57 102 760 859 571 575 88 357 773 945 38 401 186 531 655 530 413 673 562 591 79 198 563 159 790 305 582 666 316 984 597 373 86 710 584 9 285 673 718 411 970 757 812 508 288 468 39 701 493 953 644 924 151 559 84 293 864 18 959 532 2 909 257 441 619 842 802 256 515 521 667 837 630 832 346 918 652 385 971 145 690 967'
b = b.split()
b = [int(i) for i in b]
sol.buildHeap(b)
# a = [4,0,1,9, 8, 5, 6, 7, 4, 3, 2, 4,200, 6]

c = [4, 5, 3, 9, 7, 8]
sol.delete(b,len(b) - 20)
# print(b)
sol.buildHeap(b)
# print(b)
sol.delete(b, len(b) - 20)
print(b)
# sol.heapify(c,0)
# print(c)