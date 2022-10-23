class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM' ,'M']
        values =  [1,4,5,9,10,40,50,90,100,400,500,900 ,1000]
        roman = ''
        back = len(values) - 1
        while num > 0:
            for index in range(back,-1,-1):
                if values[index] <= num:
                    break
            roman += symbols[index]
            num = num - values[index]
     
        return roman
            
            