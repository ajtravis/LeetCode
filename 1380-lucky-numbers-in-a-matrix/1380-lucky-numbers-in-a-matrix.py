class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ln = []        
        for x in matrix:
            row_low = min(x)
            i = x.index(row_low)
            col_high = row_low
            for y in matrix:
                if y[i] > col_high:
                    col_high = y[i]
            if row_low == col_high:
                ln.append(row_low)
        return ln