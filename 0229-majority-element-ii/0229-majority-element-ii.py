class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = {}
        result = []
        u_nums = set(nums)
        for x in u_nums:
            freq[x] = 0
        for y in nums:
            freq[y] +=1
        for j in freq:
            if freq[j] > n/3:
                result.append(j)
        return result