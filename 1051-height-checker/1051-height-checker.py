class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = list(heights)
        expected.sort()
        result = 0
        i = 0
        while i < len(heights):
            if expected[i] != heights[i]:
                result += 1
            i += 1
        return result
            