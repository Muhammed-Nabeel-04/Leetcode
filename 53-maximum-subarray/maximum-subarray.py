class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(current_sum, max_sum)
        return max_sum            
        
        
        
        
        # max_sum = nums[0]
        # for i in range(len(nums)):
        #     total_sum = 0
        #     for j in range(i, len(nums)):
        #         total_sum += nums[j]
        #         if max_sum < total_sum:
        #             max_sum = total_sum   
        # return max_sum            