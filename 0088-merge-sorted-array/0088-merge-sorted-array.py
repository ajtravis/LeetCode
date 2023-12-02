class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged = nums1[:m] + nums2
        merged.sort()
        i = 0
        for x in merged:
            nums1[i] = x
            i+=1
                        