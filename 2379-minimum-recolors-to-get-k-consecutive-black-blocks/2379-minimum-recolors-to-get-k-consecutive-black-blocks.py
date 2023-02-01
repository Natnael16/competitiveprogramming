class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        counter = Counter(blocks[:k])
        left , right = 0, k - 1
        cur_used = counter['W']
        while right < len(blocks):
            counter[blocks[left]] -= 1
            right += 1
            left += 1
            if right >= len(blocks):
                break
            counter[blocks[right]] += 1
            cur_used = min(cur_used,counter['W'])
        return cur_used

        

