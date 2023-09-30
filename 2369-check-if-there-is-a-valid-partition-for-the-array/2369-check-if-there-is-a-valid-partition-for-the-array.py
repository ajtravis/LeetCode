class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [False for _ in range(len(nums))]
        if nums[0] == nums[1]: dp[1] = True
        if len(nums) == 2: return dp[1]
        if nums[0] == nums[1] == nums[2] or (nums[0] + 1 == nums[1] and nums[1] + 1 == nums[2]): dp[2] = True
        if len(nums) == 3: return dp[2]




        for i in range(3, len(nums)):
            # case 1
            if i >= 1 and nums[i-1] == nums[i]:
                dp[i] |= dp[i-2]
            # case 2
            if i >= 2 and nums[i-2] == nums[i-1] == nums[i]:
                dp[i] |= dp[i - 3]
            # case 3
            if i >= 2 and nums[i-2] + 1 == nums[i-1] and nums[i-1] + 1 == nums[i]: 
                dp[i] |= dp[i-3]
        
        return dp[-1]