class Solution:
    def intToRoman(self, num: int) -> str:
        valueSymbol = {
                1   : 'I',
                4   : 'IV',
                5   : 'V',
                9   : 'IX',
                10  : 'X',
                40  : 'XL',
                50  : 'L',
                90  : 'XC',
                100 : 'C',
                400 : 'CD',
                500 : 'D',
                900 : 'CM',
                1000: 'M',
        }
        values = sorted(valueSymbol.keys(),reverse = True)
        roman = ''
        while num > 0:
            for value in values:
                if value <= num:
                    break
            roman += valueSymbol[value]
            num = num - value
           
            
        return roman
            
            