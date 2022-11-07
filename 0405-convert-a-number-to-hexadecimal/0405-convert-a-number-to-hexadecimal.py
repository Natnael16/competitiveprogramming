class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        map = {10: "a", 11 : "b", 12 : "c", 13 : "d", 14 : "e", 15 : "f"}
        
        if num < 0:
            num += 2**32
        res = []
        binary = bin(num).split("b")[1]
        while len(binary) >= 4:
            last4 = binary[-4:]
            binary = binary[:-4]
            integer = int(last4,base=2) 
            if integer > 9:
                res.append(str(map[integer]))
            else:
                res.append(str(integer))
        if binary:
            integer = int(binary,base=2) 
            if integer > 9:
                res.append(str(map[integer]))
            else:
                res.append(str(integer))
        return "".join(res[::-1])