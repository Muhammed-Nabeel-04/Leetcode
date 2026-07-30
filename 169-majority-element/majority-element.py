class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        remove_dublicates = set(nums)
        
        max_count = 0
        for element in remove_dublicates:
            count = 0
            for num in nums:
              if element == num:
                count += 1

            if count > max_count:
                max_count = count
                output = element
        return output      