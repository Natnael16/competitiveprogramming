class Solution:
    def restoreIpAddresses(self, ip: str) -> List[str]:
        def validIp(stringNum): # len will be > 1
            if len(stringNum) == 1: return True
            if len(stringNum) == 2 and stringNum[0] != '0': return True
            elif stringNum[0] == '0': return False
            return  0 <= int(stringNum) <= 255

        ans = []
        def backtrack(ind,dots,address):

            if ind >= len(ip): return
            if dots < 0: return
            if dots <= 0 and  not validIp(ip[ind:]): return
            elif dots == 0 and validIp(ip[ind:]):
                ans.append(address + ip[ind:])

            backtrack(ind + 1, dots - 1, address + str(ip[ind]) + '.')
            if ind + 2 < len(ip):
                if validIp(ip[ind:ind+2]):
                    backtrack(ind + 2,dots - 1, address + str(ip[ind:ind+2]) + '.')
            if ind + 3 < len(ip):
                if validIp(ip[ind:ind+3]):

                    backtrack(ind + 3,dots - 1, address + str(ip[ind:ind+3]) + '.')
        backtrack(0,3,'')
        return ans