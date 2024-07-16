import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k > 0:
            m = max(gifts)
            i = gifts.index(m)
            gifts[i] = math.floor(math.sqrt(m))
            k-=1
        return sum(gifts)