class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        matches = 0
        for cookie in s:
            i = 0
            while i < len(g):
                if cookie >= g[i]:
                    matches += 1
                    g = g[i+1:]
                    break
                i+=1
        return matches