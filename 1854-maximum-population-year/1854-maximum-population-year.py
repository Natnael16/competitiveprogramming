class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        max_pop =  (-inf ,1949)
        for year in range(1950,2051):
            population = 0
            for start ,end in logs:
                if start <= year < end:
                    population += 1
            if population > max_pop[0]:
                max_pop = (population, year)
        return max_pop[1]