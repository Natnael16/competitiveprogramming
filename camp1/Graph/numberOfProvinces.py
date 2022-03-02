class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = set()

        def dfs(city):
            for neighbour in range(len(isConnected[city])):
                if (city, neighbour) in visited:
                    continue
                visited.add((city, neighbour))
                if not isConnected[city][neighbour]:
                    continue
                visited.add((neighbour, city))
                dfs(neighbour)

        for city in range(len(isConnected)):
            if (city, 0) not in visited:
                provinces += 1
            dfs(city)

        return provinces