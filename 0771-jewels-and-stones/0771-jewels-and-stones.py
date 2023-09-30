class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jc = list(jewels)
        sc = list(stones)
        used = []
        count = 0
        
        for i in jc:
            if i not in used:
                used.append(i)
                if i in sc:
                    count += sc.count(i)
        
        return count