class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        if len(nums) == 1:
            nums[0].sort()
            return nums[0]
        common = []
        i = 0
        while i < len(nums[0]):
            c = nums[0][i]
            j = 1
            while j < len(nums):
                
                if c not in nums[j]:
                    break
                elif j == len(nums) - 1:
                    common.append(c)
                j+=1
            i+=1
        common.sort()
        return common
                    
                
            