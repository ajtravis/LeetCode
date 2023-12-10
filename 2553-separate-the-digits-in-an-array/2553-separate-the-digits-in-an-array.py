class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            num_str = str(num)
            result.extend(map(int, num_str))

        return result