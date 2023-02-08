class Solution:
    from collections import defaultdict, deque
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
            
        if source == target:
            return 0
        
        graph = defaultdict(set)
        
       
        for bus_number, route in enumerate(routes):
            for stop in route:
                graph[stop].add(bus_number)
        
        queue = deque([(source, 0)])
        
        visited_route = set()
        visited_buses = set()
        
        while queue:
            stop, count = queue.popleft()
            if stop == target:
                    return count
                
            for bus_number in graph[stop]:
                if bus_number not in visited_buses:
                    visited_buses.add(bus_number)
      
                    for stop in routes[bus_number]:
                        if stop not in visited_route:
                            visited_route.add(stop)
                            queue.append((stop, count + 1))
        return -1
                
            
            