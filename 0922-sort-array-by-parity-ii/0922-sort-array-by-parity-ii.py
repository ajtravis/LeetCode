class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i = 0
        evens = []
        odds = []
        result = []
        for n in nums:
            if n%2 == 0 or n == 0:
                evens.append(n)
            else:
                odds.append(n)
        while i < len(nums):
            if i%2 == 1:
                n = odds.pop()
                result.append(n)
            else:
                n = evens.pop()
                result.append(n)
            i+=1
        return result