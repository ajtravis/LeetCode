class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        counter = 0
        for l in grid:
            for num in l:
                if num < 0:
                    counter += 1
        return counter