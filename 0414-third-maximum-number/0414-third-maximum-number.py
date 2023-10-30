class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)

        # Check if there are at least 3 distinct elements
        if len(nums) >= 3:
            return nums[2]
        else:
            return nums[0]