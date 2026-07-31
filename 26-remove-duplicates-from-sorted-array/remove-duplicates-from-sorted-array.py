class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
 
        new_list = []
        while nums:
            new_list.append(nums[0])
            nums.remove(nums[0])

        for i in new_list:
            if i not in nums:
                nums.append(i)
        return len(nums)            

