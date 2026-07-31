class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # output = 0
        # store = 0
        # for i in range(len(nums)):
        #     if nums[i] == k:
        #         output +=1
        #     # for j in range(i+1, i+2):
        #     if (i+1 < len(nums)) and (nums[i] + nums[i+1] == k):
        #         output +=1
        #     store += nums[i]
        # if store == k:
        #     output += 1

        # return output         

        # count = 0
        # for i in range(len(nums)):
        #     total_sum = 0
        #     for j in range(i, len(nums)):
        #         total_sum += nums[j]
                
        #         if total_sum == k:
        #            count += 1
        # return count

      

        prefix = {0: 1}
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in prefix:
                count += prefix[prefix_sum - k]

            prefix[prefix_sum] = prefix.get(prefix_sum, 0) + 1

        return count


# [1]
# [1,2]
# [1,2,3]
# [1,2,3,4]

# [2]
# [2,3]
# [2,3,4]

# [3]
# [3,4]

# [4]