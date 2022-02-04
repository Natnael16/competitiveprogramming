class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        div = len(nums)/3
        output = []
        # for i in nums:
        #     if nums.count(i) > div:
        #         if i not in output:                 O(n**2)
        #             output.append(i)
        # return output
        pairs = {}
        for i in nums:
            if i not in pairs:
                pairs[i] = 1
            elif i in pairs:
                pairs[i] += 1
        myKeys = list(pairs.keys())
        print(type(myKeys))
        print(myKeys)                   ##O(n)
        print(pairs)
        for i in myKeys:
            if pairs[i] > div:
                output.append(i)
        return output