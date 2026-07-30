class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for i in s:
            if i.isalnum():
                clean += i.lower()   

        reversed_clean = clean[::-1]
        if clean == reversed_clean:
            return True
        else:
          return  False    


        # pointer = len(clean)
        # for i in range(pointer//2):
        #     left_pointer = i
        #     right_pointer = -(i+1)
        #     if clean[left_pointer] != clean[right_pointer]:
        #         return False
        # return True