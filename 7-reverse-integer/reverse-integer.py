class Solution:
    def reverse(self, x: int) -> int:

        if x<0:
          positive_x = x*-1
        else:
          positive_x = x

        z = str(positive_x)
        y = z[::-1]
        y = int(y)

        if x<0:
            y = -(y)   

        if y < -2147483648 or y > 2147483647:
            return 0
        return y 
        

        # negative = x<0
        # x = abs(x)

        # result = 0
        # while x != 0:
        #     digit = x%10
        #     x = x//10
        #     result = result * 10 + digit

        # if negative:
        #     result = -result
        # return result    