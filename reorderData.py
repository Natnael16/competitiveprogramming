class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            if not log.split()[-1].isdigit():
                id_back = log.split()
                id_back.append(id_back[0])
                id_back[0] = ""
                
                letter_logs.append(" ".join(id_back).strip())
            else:
                digit_logs.append(log)
        letter_logs.sort()
        new_letter_logs = []
        for s_log in letter_logs:
            
            s_arr = s_log.split()
            s_arr = [s_arr[-1]]  + s_arr
            s_arr.pop()
            new_letter_logs.append(" ".join(s_arr))
            
            
        return new_letter_logs + digit_logs
