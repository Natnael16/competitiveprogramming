class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort(reverse= True)
        left , right = 0, len(people)-1
        boat = 0
        while left <= right:
            if people[left] >= limit:
                boat += 1
                left += 1
            elif people[left] < limit:
                if people[left] + people[right] <= limit:
                    boat +=1
                    left += 1
                    right -= 1
                else:
                    boat += 1
                    left +=1
        return boat