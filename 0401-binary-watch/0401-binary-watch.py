class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        answer = []
        for hour in range(12):
            for minute in range(60):
                cur_time = bin(hour).split("b")[1] + bin(minute).split("b")[1]
                if cur_time.count("1") == turnedOn:
                    if minute < 10:
                        minute = "0{}".format(minute)
                    answer.append("{}:{}".format(hour,minute))
        return answer
                    
                
            
            
            
            
        
        