class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}  
        current = 0
        result = 0         
        for i in s:
            if current < values[i]:
                result = result - current
                result += values[i] - current 
            else:    
                result += values[i]
            current = values[i]    
        return result        
