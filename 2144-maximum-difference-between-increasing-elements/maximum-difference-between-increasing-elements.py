class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_dif = -1
        i = 0
        j = 1
        while i < len(nums)-1:
            print(max_dif, i)
            l = nums[i]
            while j < len(nums):
                if nums[j] > nums[i]:
                    r = nums[j]
                    dif = r - l
                    print(l, r, dif)
                    if dif > max_dif:
                        max_dif = dif
                j+=1
            i += 1
            j = i + 1
        return max_dif