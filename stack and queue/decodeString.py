class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        sta = []
        for i in s:
            if i != ']':
                sta.append(str(i))
            else:
                save=[]
                while sta[-1] != '[':
                    save.insert(0,sta.pop(-1))
                sta.pop(-1)
                num = []
                while len(sta) > 0 and sta[-1].isdigit():
                    num.insert(0,sta.pop(-1))
                number= ''.join(num)
                multiplied = int(number)*save
                string = "".join(multiplied)
                sta.append(string)
        return ''.join(sta)