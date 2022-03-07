class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        visited = set()
        visited.add(start)
        inbound = lambda pos : 0<= pos < len(arr)
        while q:
            cur = q.popleft()
            if arr[cur] == 0:
                return True
            new_left, new_right = cur - arr[cur],cur + arr[cur]
            if inbound(new_left) and new_left not in visited:
                visited.add(new_left)
                q.append(new_left)
            if inbound(new_right) and new_right not in visited:
                visited.add(new_right)
                q.append(new_right)