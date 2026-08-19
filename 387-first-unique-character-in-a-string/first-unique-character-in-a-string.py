class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        for i in range(len(s)):
            found = False
            for j in range(len(s)):
                if i != j and s[i] == s[j]:
                    found = True
                    break
                     
            if found == False:
               return i         
        return -1

        
        # for i in range(len(s)):
        #     count = 0
        #     for j in range(len(s)):
        #         if s[i] == s[j]:
        #             count += 1
                     
        #     if count > 1:
        #        return i         
        # return -1