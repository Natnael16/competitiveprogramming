class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def winner(arr,cur,delete):
            leng = len(arr)
            if leng == 1:
                return arr[0]
            else:
                if cur <leng:
                    if delete < leng:
                        arr.pop(delete)
                    else:
                        while delete >= leng:
                            delete = delete - leng
                        arr.pop(delete)
                    cur = delete
                    delete = cur + k-1
                    return winner(arr,cur,delete)
                else:
                    while cur < leng:
                        cur = leng - cur
                    delete = cur + k-1
                    if delete < leng:
                        arr.pop(delete)
                    else:
                        while delete >= leng:
                            delete = delete - leng
                        arr.pop(delete)
                    cur = delete
                    delete = cur + k - 1
                    return winner(arr,cur,delete)
        people = [i for i in range(1,n+1)]
        return winner(people,0,k-1)