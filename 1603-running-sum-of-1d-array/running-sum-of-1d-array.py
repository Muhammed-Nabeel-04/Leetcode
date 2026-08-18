class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_list = []
        total = 0
        for i in nums:
            total += i
            new_list.append(total)
        return new_list    