class Solution:
    def fillCups(self, amount: List[int]) -> int:
        maxi = 0
        total = 0
        for i in range(3):
            total += amount[i]
            maxi = max(maxi, amount[i])
        return max(maxi, (total + 1) // 2)