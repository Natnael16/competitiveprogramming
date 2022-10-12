class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #jfk : [kul,nrt]
        #kul : []
        #nrt : [jfk]
        #
        #[jfk,muc,lhr,sfo,sjc]
        #
        #[jfk,]
            
        
        graph = defaultdict(list)
        tickets.sort()
        for from_ , to_ in tickets:
            graph[from_].append(to_)
        
        stack = ["JFK"]
        def dfs(cur_port):
            nonlocal stack
            if len(stack) == len(tickets) + 1:
                return True
            if cur_port not in graph:
                return False
            copy = graph[cur_port][:]
            for i in range(len(copy)):
                stack.append(copy[i])
                poped = graph[cur_port].pop(i)
                
                if not dfs(copy[i]):
                    stack.pop()
                    graph[cur_port].insert(i,poped)
                else:
                    return True
            
                    
                
            
            
        dfs("JFK")
        return stack
            
            
        
        
        
        
        