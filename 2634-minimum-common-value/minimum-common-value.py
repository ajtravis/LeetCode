class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # i = 0
        # while i < len(nums1):
        #     if nums1[i] in nums2:
        #         return nums1[i]
        #     else:
        #         i += 1
        s1 = set(nums1)
        s2 = set(nums2)
        if (s1 & s2):   
            return min(list(s1 & s2))
        else:
            return -1