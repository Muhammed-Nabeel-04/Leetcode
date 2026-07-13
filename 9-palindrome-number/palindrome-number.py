class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x <0 :
        #     return False
        # else:    
        #     y = ''
        #     x = str(x)
        #     for i in range(len(x)-1,-1,-1):
        #         y += str(x[i])
        #     if x == y :
        #         return True  
        #     elif x != y:
        #         return False     

        #short:-
        x = str(x)
        y = x[::-1]
        if x==y:
            return True
        else:
            return False    