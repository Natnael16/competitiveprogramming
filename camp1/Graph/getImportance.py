class Solution:

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hMap = {}
        for i in range(len(employees)):
            hMap[employees[i].id] = i

        def helper(key):
            person = employees[hMap[key]]
            if person.subordinates == []:
                return person.importance
            tot = 0
            for i in person.subordinates:
                tot += helper(i)
            return tot + person.importance

        return helper(id)