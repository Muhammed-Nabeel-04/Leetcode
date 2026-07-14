class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        first = strs[0]
        for i in range(len(first)):
            char = first[i]

            for j in range(1,len(strs)):
                if i>=len(strs[j]) or char != strs[j][i]:
                        return result

            result += char
                
        return result