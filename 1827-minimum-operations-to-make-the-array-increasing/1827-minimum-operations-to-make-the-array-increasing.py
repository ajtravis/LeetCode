class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return 0
        ops = 0
        i = 1
        while i < l:
            if nums[i] == nums[i-1]:
                nums[i] += 1
                ops += 1
            elif nums[i] < nums[i-1]:
                dif = (nums[i-1] - nums[i]) + 1
                nums[i] += dif
                ops += dif
            i += 1
        return ops   
            