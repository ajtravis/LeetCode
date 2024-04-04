class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        top, front, side = 0,0,0

        for i in range(len(grid)):
            max_row = max(grid[i])
            front += max_row
            for j in range(len(grid[i])):
                if grid[i][j] > 0:
                    top += 1
        columns = [[row[i] for row in grid] for i in range(len(grid[0]))]
        for c in columns:
            side  += max(c)
        return top + front + side