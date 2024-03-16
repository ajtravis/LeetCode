class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Greedy
        maxSum = 0
        idx, add = 0, True
        nLen = len(nums)
        while idx<nLen-1: # here we use nLen-1 to avoid index out of range
            if nums[idx]>nums[idx+1] and add:
                maxSum += nums[idx]
                add = not add
            elif nums[idx]<nums[idx+1] and not add:
                maxSum -= nums[idx]
                add = not add
            idx+=1
        maxSum += nums[idx] if add else 0 # determine the last element
        return maxSum