class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ''
        length = len(min(strs))
        for i in range(length):
            char = strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i] != char:
                    return output
            output += char
        return output    
