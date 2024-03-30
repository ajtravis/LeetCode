class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
       

        BIG = 10**9 + 7 

        
        H = max(max(hs) for hs in hats) + 1
        P = len(hats)

        people = [[] for _ in range(H)] # people[h] are the people that can wear h
        for p, hs in enumerate(hats):
            for h in hs:
                people[h].append(p)


        ALL = (1 << (P+1)) - 1 # P+1 b/c they're 1-indexed in `hats`

        @cache
        def ways(h: int, r: int, rem: int) -> int:
            """Returns ways to assign r of hats h..H-1 to hatless people, bit-encoded as rem"""

            if r > H-h: return 0 # can't assign more than H-h hats
            if r == 0: return 1

            ans = ways(h+1, r, rem) # ways that don't involve assigning h
            for p in people[h]:
                b = 1 << p
                if rem & b:
                    ans += ways(h+1, r-1, rem ^ b) # assign h to p (encoded as b) and continue

            return ans % BIG

        return ways(h=1, r=P, rem=ALL)