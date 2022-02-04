class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = ""
        while head:
            s += str(head.val)
            head = head.next
        new = s[::-1]
        if int(new) == int(s):
            return True
        else:
            return False