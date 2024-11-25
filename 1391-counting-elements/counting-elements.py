class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        for x in arr:
            n = x+1
            if n in arr:
                count += 1
        return count