class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        answer = []
        i = 1
        while i < len(nums):
            prev = nums[i-1]
            cur = nums[i]
            answer.append(prev | cur)
            i+=1
        return answer