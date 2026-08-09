import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        pivot_index = random.randint(0, len(nums) - 1)
        pivot = nums[pivot_index]

        left = []
        right = []
        equal = []
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                equal.append(num)

        return self.sortArray(left) + equal + self.sortArray(right)