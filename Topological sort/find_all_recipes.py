class Solution:

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]],
                       supplies: List[str]) -> List[str]:
        ings = defaultdict(set)
        indegree = [0] * len(recipes)

        for i in range(len(ingredients)):
            count = 0
            for j in range(len(ingredients[i])):
                count += 1
                ings[ingredients[i][j]].add(i)
            indegree[i] += count

        q = deque()

        for s in supplies:
            q.append(s)

        res = []
        while q:
            cur = q.popleft()

            for ing in ings[cur]:
                indegree[ing] -= 1
                if not indegree[ing]:
                    q.append(recipes[ing])
                    res.append(recipes[ing])

        return res