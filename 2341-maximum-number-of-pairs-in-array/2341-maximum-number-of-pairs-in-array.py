class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        frequency = {}
    
        # Count the frequency of each integer
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        # Count the number of pairs and leftover integers
        pairs = 0
        for freq in frequency.values():
            pairs += freq // 2

        leftover = len(nums) - 2 * pairs

        return [pairs, leftover]