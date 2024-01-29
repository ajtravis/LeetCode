class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratios = {}
        total = 0
        for r in rectangles:
            ratio = r[0]/r[1]
            if ratio in ratios.keys():
                total += len(ratios[ratio])
                ratios[ratio].append(r)
            else:
                ratios[ratio] = [r]
        return total