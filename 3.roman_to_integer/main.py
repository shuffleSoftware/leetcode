class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}

        lenDigits = len(s)
        summ = 0
        index = 0

        while index < lenDigits:
            if index < lenDigits - 1 and numbers[s[index]] < numbers[s[index + 1]]:
                summ += numbers[s[index + 1]] - numbers[s[index]]
                index += 2
            else:
                summ += numbers[s[index]]
                index += 1
        return summ
    
