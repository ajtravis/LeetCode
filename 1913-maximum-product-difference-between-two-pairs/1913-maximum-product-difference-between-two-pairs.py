class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        # Choose the two largest and two smallest numbers
        max1, max2 = nums[n-1], nums[n-2]
        min1, min2 = nums[0], nums[1]

        # Calculate the product differences for the chosen pairs
        product_difference1 = max1 * max2
        product_difference2 = min1 * min2

        return product_difference1 - product_difference2