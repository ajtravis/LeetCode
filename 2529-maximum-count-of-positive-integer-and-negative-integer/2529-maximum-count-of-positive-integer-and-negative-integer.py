class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = filter(lambda x: x > 0, nums)
        neg = filter(lambda x: x < 0, nums)
        pl = len(list(pos))
        nl = len(list(neg))
        return max(pl, nl)