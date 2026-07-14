class Solution:
    def isValid(self, s: str) -> bool:
        # brackets = {'(':")", '{':'}', '[':']'}

        # result = bool
        # for i in range(len(s)):
        #     if s[i] in brackets.keys():
        #         if brackets[s[i]] in s:
        #             result = True
        #         else:
        #             result = False

        # return result

                 
        brackets = {')': '(', ']': '[', '}': '{'}      

        stack = []
        char = ""
        for i in range(len(s)):
            char = s[i]
            if char in brackets.values():
              stack.append(char)
            elif stack == []:
                return False
                break     
            elif char in brackets.keys():
              if stack[-1] == brackets[char]:
                 stack.pop()
              else:
                return False   

        return stack == []        